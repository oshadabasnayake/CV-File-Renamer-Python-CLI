# CV File Renamer (Python CLI)

A lightweight Python CLI tool to rename CV files for job applications.

> ⚠️ Note:  
> This tool **only renames the file**. It does **not** modify the content of the CV in any way.

---

## Why This Tool Exists

When applying for multiple jobs, repeatedly renaming your CV file becomes a small but frustrating task.

This tool removes that friction by:
- Standardizing CV filenames
- Reducing manual effort
- Preventing typos during job applications

It is intentionally designed to be **simple, fast, and practical**.

---

## How It Works

1. Place **only one CV file** in a temporary folder
2. Run the script inside that folder
3. Enter the job title when prompted
4. The file is renamed instantly

---

## What This Tool Does

- Automatically detects the single file in the folder
- Converts job titles into underscore-separated format
- Preserves the original file extension
- Prevents overwriting by appending `_2`, `_3`, etc. if needed

---

## What This Tool Does NOT Do

- Does not edit CV content
- Does not change formatting or metadata
- Does not modify the document internally

---

## Requirements

- Python 3.8 or higher
- macOS, Linux, or Windows
- No external dependencies

---

## Usage

```bash
python3 cv_rename_onefile.py

Then enter the job title when prompted, for example:

Site Reliability Engineer

FIRST = "Oshada"
LAST = "Basnayake"
TAIL = "CV"


License

MIT License

Author

Oshada Basnayake
DevOps / Cloud / Automation Engineer

Good automation removes friction instead of adding complexity.


---

## ✅ After saving, do this

```bash
git add README.md
git commit -m "Add README documentation"
git push

