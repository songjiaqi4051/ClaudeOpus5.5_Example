#!/usr/bin/env python3
"""Import pinned public repositories without executing their code.

The index is populated directly from upstream Git trees. Never stage the
imported directories with `git add`: doing so may apply nested attributes.
"""

from __future__ import annotations

import argparse
from datetime import datetime, timezone
import json
import os
from pathlib import Path
import re
import subprocess
import sys

TARGET = "songjiaqi4051/ClaudeOpus5.5_Example"
ROOT = Path(__file__).resolve().parents[1]


def git(*args: str, capture: bool = True) -> str:
    result = subprocess.run(
        ["git", "-c", "core.autocrlf=false", *args],
        cwd=ROOT, check=True, text=True,
        stdout=subprocess.PIPE if capture else None,
    )
    return result.stdout.strip() if capture else ""


def tree_stats(tree: str) -> tuple[int, int]:
    data = subprocess.check_output(
        ["git", "ls-tree", "-rlz", tree], cwd=ROOT
    )
    count = size = 0
    for entry in data.split(b"\0"):
        if not entry:
            continue
        meta, _ = entry.split(b"\t", 1)
        mode, kind, sha, length = meta.split()
        if kind != b"blob":
            raise RuntimeError(f"Unsupported Git entry: {kind!r} {sha!r}")
        count += 1
        size += int(length)
    return count, size


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--publish", action="store_true")
    parser.add_argument("--local-sources", type=Path)
    args = parser.parse_args()

    if args.publish and os.environ.get("GITHUB_REPOSITORY") != TARGET:
        raise RuntimeError("Publishing is limited to the intended GitHub repository")
    if git("status", "--porcelain"):
        raise RuntimeError("Start from a clean working tree and index")

    catalog = json.loads((ROOT / "catalog.json").read_text(encoding="utf-8"))
    repos = catalog["repositories"]
    initial_head = git("rev-parse", "HEAD")
    checked = []

    # Fetch and verify every snapshot before writing any imported directory.
    for repo in repos:
        name = repo["repo"]
        commit = repo["commit"]
        prefix = repo["local_path"].rstrip("/")
        if not re.fullmatch(r"[A-Za-z0-9_.-]+/[A-Za-z0-9_.-]+", name):
            raise ValueError(f"Invalid repository name: {name}")
        if not re.fullmatch(r"[0-9a-f]{40}", commit):
            raise ValueError(f"Invalid commit for {name}")
        if prefix != "examples/" + name.replace("/", "__"):
            raise ValueError(f"Unexpected destination for {name}: {prefix}")
        if repo["stars"] <= 500:
            raise ValueError(f"Star threshold is not satisfied: {name}")
        if (ROOT / prefix).exists():
            raise RuntimeError(f"Destination already exists: {prefix}")

        source = (str(args.local_sources / name.replace("/", "__"))
                  if args.local_sources else f"https://github.com/{name}.git")
        print(f"Fetching {name} at {commit}", flush=True)
        git("-c", "http.https://github.com/.extraheader=", "fetch", "--quiet",
            "--no-tags", "--depth=1", "--no-write-fetch-head",
            source, commit, capture=False)
        tree = git("rev-parse", commit + "^{tree}")
        files, size = tree_stats(tree)
        if (tree, files, size) != (repo["tree"], repo["files"], repo["bytes"]):
            raise RuntimeError(f"Snapshot does not match the verified catalog: {name}")
        checked.append({
            "repo": name, "commit": commit, "tree": tree,
            "files": files, "bytes": size, "local_path": prefix,
        })

    for repo in checked:
        print(f"Importing {repo['repo']}: {repo['files']} files", flush=True)
        git("read-tree", "--prefix=" + repo["local_path"] + "/", "-u", repo["tree"])

    index_tree = git("write-tree")
    for repo in checked:
        imported = git("rev-parse", index_tree + ":" + repo["local_path"])
        if imported != repo["tree"]:
            raise RuntimeError(f"Imported tree differs from upstream: {repo['repo']}")
        repo["imported_tree"] = imported
        repo["tree_matches_upstream"] = True

    report = {
        "schema_version": 1,
        "verified_at": datetime.now(timezone.utc).isoformat(),
        "target_repository": TARGET,
        "base_commit": initial_head,
        "verification": "Every imported subtree has the exact upstream Git tree SHA.",
        "repository_count": len(checked),
        "total_files": sum(r["files"] for r in checked),
        "total_bytes": sum(r["bytes"] for r in checked),
        "repositories": checked,
    }
    report_path = ROOT / "sources" / "import-report.json"
    report_path.parent.mkdir(parents=True, exist_ok=True)
    report_path.write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    git("add", "--", "sources/import-report.json")
    git("config", "user.name", "github-actions[bot]")
    git("config", "user.email", "41898282+github-actions[bot]@users.noreply.github.com")
    git("commit", "--quiet", "--no-gpg-sign", "-m",
        f"Import {len(checked)} verified Claude Opus 5.5 frontend repositories",
        "-m", "Preserve all tracked source, assets, file modes, and license notices. "
              "Verify every subtree against its pinned upstream Git tree SHA.", capture=False)
    for repo in checked:
        if git("rev-parse", "HEAD:" + repo["local_path"]) != repo["tree"]:
            raise RuntimeError(f"Committed tree mismatch: {repo['repo']}")

    if args.publish:
        # A normal fast-forward push protects changes made during the import.
        git("push", "origin", "HEAD:refs/heads/main", capture=False)
    print(json.dumps({
        "commit": git("rev-parse", "HEAD"),
        "repositories": len(checked),
        "files": report["total_files"],
        "bytes": report["total_bytes"],
        "published": args.publish,
    }), flush=True)


if __name__ == "__main__":
    main()
