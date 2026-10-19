"""Benchmark harness — VaultNote cache performance.

Spec: _nbdev_development/specs/CODING_STANDARDS/performance.md (canonical recipe).
Usage:  python bench_vault_cache.py [--size N [N ...]]   (default: 100)

Prints one line per target per size: median of 3 timed runs after 1 warmup,
each timed run on a fresh deterministic vault. Targets:
  link_pass  — all_links_in_vault (full-vault read pass; audit §2.2)
  delete     — cold-cache VaultNote(name=...).delete() (lazy rebuild + single-entry remove)
  rename     — cold-cache VaultNote(name=...).rename(...) (audit §2.3, full-cache sweep)
"""
import argparse
import shutil
import statistics
import tempfile
import time
from pathlib import Path

from trouver.obsidian.vault import VaultNote
from trouver.obsidian.vault_and_links import all_links_in_vault


def make_sized_vault(dest: Path, n: int) -> Path:
    """Deterministic n-note vault at `dest`: note_i links to note_(i+1)."""
    dest.mkdir(parents=True, exist_ok=True)
    for i in range(n):
        link = f"[[note_{i + 1}]]" if i + 1 < n else ""
        (dest / f"note_{i}.md").write_text(f"# note {i}\n\n{link}\n", encoding="utf-8")
    return dest


def _target_link_pass(vault: Path) -> None:
    all_links_in_vault(vault)


def _target_delete(vault: Path) -> None:
    VaultNote.clear_cache()  # cold start: name lookup triggers lazy rebuild
    VaultNote(vault=vault, name="note_0").delete()


def _target_rename(vault: Path) -> None:
    VaultNote.clear_cache()  # cold start: rename sweeps the (rebuilt) whole cache
    VaultNote(vault=vault, name="note_0").rename("note_0_renamed")


TARGETS = {
    "link_pass": _target_link_pass,
    "delete": _target_delete,
    "rename": _target_rename,
}


def bench(name: str, size: int, runs: int = 3) -> float:
    """Warmup on one vault, then median of `runs` timed calls on fresh vaults."""
    base = Path(tempfile.mkdtemp(prefix="bench_vault_cache_"))
    try:
        TARGETS[name](make_sized_vault(base / "warmup", size))  # warmup: imports, disk cache
        times = []
        for i in range(runs):
            vault = make_sized_vault(base / f"run_{i}", size)
            start = time.perf_counter()
            TARGETS[name](vault)
            times.append(time.perf_counter() - start)
        return statistics.median(times)
    finally:
        shutil.rmtree(base, ignore_errors=True)


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--size", nargs="+", type=int, default=[100],
                        help="vault sizes to measure (use two for the scaling test)")
    args = parser.parse_args()
    for name in TARGETS:
        for size in args.size:
            med = bench(name, size)
            print(f"{name}\tsize={size}\tmedian={med:.4f}s")


if __name__ == "__main__":
    main()
