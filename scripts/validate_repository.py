#!/usr/bin/env python3
"""Validate layout and compile native parallel programs."""

from __future__ import annotations

import re
import platform
import shutil
import subprocess
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
IMPLEMENTATIONS = (
    "openmp/thread-count", "openmp/consensus", "mpi/consensus",
    "hybrid/parallel-search", "mapreduce/word-count",
    "mapreduce/max-temperature", "mapreduce/keyword-analysis",
    "mapreduce/comment-length",
)


def command(args: list[str], source: Path, errors: list[str]) -> None:
    result = subprocess.run(args + [str(source)], cwd=source.parent, text=True, capture_output=True)
    if result.returncode:
        errors.append(f"compile check failed: {source.relative_to(ROOT)}\n{result.stderr}")


def main() -> int:
    errors: list[str] = []
    for relative in IMPLEMENTATIONS:
        directory = ROOT / relative
        if not (directory / "README.md").is_file():
            errors.append(f"missing README: {relative}")
        if not any((directory / "src").glob("*")):
            errors.append(f"missing source: {relative}/src")

    tracked = subprocess.check_output(["git", "ls-files"], cwd=ROOT, text=True).splitlines()
    for value in tracked:
        if Path(value).suffix.lower() in {".class", ".jar", ".o", ".out"}:
            errors.append(f"generated artifact is tracked: {value}")

    image_pattern = re.compile(r'<img\s+[^>]*src=["\']([^"\']+)["\']', re.IGNORECASE)
    for readme in ROOT.rglob("README.md"):
        for image in image_pattern.findall(readme.read_text(encoding="utf-8")):
            if not image.startswith(("http://", "https://")) and not (readme.parent / image).is_file():
                errors.append(f"broken image: {readme.relative_to(ROOT)} -> {image}")

    cxx = shutil.which("g++") or shutil.which("c++")
    mpi = shutil.which("mpic++")
    if cxx and platform.system() == "Linux":
        for source in sorted((ROOT / "openmp").glob("**/*.cpp")):
            command([cxx, "-std=c++17", "-fopenmp", "-fsyntax-only"], source, errors)
    if mpi:
        for source in sorted((ROOT / "mpi").glob("**/*.cpp")):
            command([mpi, "-std=c++17", "-fsyntax-only"], source, errors)
        for source in sorted((ROOT / "hybrid").glob("**/*.cpp")):
            command([mpi, "-std=c++17", "-fopenmp", "-fsyntax-only"], source, errors)

    if errors:
        print("Repository validation failed:")
        for error in errors:
            print(f"- {error}")
        return 1
    print(f"Validated {len(IMPLEMENTATIONS)} parallel and distributed implementations.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
