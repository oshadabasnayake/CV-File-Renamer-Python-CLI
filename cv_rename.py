#!/usr/bin/env python3
import re
from pathlib import Path

FIRST = "Oshada"
LAST = "Basnayake"
TAIL = "CV"

def slug_words(text: str) -> str:
    text = text.strip()
    text = re.sub(r"\s+", " ", text)          # collapse multiple spaces
    text = text.replace(" ", "_")             # spaces -> underscores
    text = re.sub(r"[^A-Za-z0-9_\-]+", "", text)  # remove weird chars
    text = re.sub(r"_+", "_", text)           # collapse __
    return text

def unique_path(p: Path) -> Path:
    if not p.exists():
        return p
    i = 2
    while True:
        candidate = p.with_name(f"{p.stem}_{i}{p.suffix}")
        if not candidate.exists():
            return candidate
        i += 1

def find_single_target_file(folder: Path) -> Path:
    # Ignore hidden files, folders, and this script file
    script_name = Path(__file__).name
    candidates = []
    for p in folder.iterdir():
        if p.name.startswith("."):
            continue
        if p.is_dir():
            continue
        if p.name == script_name:
            continue
        candidates.append(p)

    if len(candidates) == 0:
        raise FileNotFoundError("No file found to rename in this folder.")
    if len(candidates) > 1:
        names = "\n".join(f"- {c.name}" for c in candidates)
        raise RuntimeError(
            "More than one file found in this folder. Keep ONLY the CV file here.\n"
            f"Found:\n{names}"
        )
    return candidates[0]

def main():
    folder = Path.cwd()  # <-- current folder (where you run it)
    try:
        target_file = find_single_target_file(folder)
    except Exception as e:
        print(f"ERROR: {e}")
        return

    job_name = input("Enter job name (e.g., Site Reliability Engineer): ").strip()
    if not job_name:
        print("ERROR: Job name cannot be empty.")
        return

    job_slug = slug_words(job_name)
    ext = target_file.suffix  # keep original extension

    new_name = f"{FIRST}_{LAST}_{job_slug}_{TAIL}{ext}"
    destination = unique_path(folder / new_name)

    target_file.rename(destination)

    print("Rename successfully ✅")
    print(f"File name is - {destination.name}")

if __name__ == "__main__":
    main()

