# activity-gen

A lightweight Python command-line tool for recording **real project work** in a dated activity log.

This repository previously contained only a list of contribution dates. A date list does not demonstrate what was built, and it cannot verify that work took place. This version replaces that list with a usable tracker. It does not generate fake GitHub commits, backdate activity, or manufacture contribution streaks.

## What it does

- Records the local date and time when you log work.
- Captures the project, task completed, and outcome.
- Stores entries in a local CSV file.
- Lists previous entries and summarizes the number of logged work days.
- Uses only the Python standard library.

## Requirements

- Python 3.9+
- No external packages

## Quick start

Clone or download this repository, then run these commands from the project folder.

**Windows (PowerShell):**

```powershell
py activity_gen.py add --project "activity-gen" --task "Implemented the activity logger" --outcome "The CLI now saves dated work records"
py activity_gen.py list
py activity_gen.py stats
```

**macOS / Linux:**

```bash
python3 activity_gen.py add --project "activity-gen" --task "Implemented the activity logger" --outcome "The CLI now saves dated work records"
python3 activity_gen.py list
python3 activity_gen.py stats
```

Use `--help` to see all available commands.

## Example

```text
$ py activity_gen.py add --project "My project" --task "Fixed CSV validation" --outcome "Invalid rows are now rejected"
Logged work for 2026-11-23.
Saved to activity_log.csv.
```

The displayed date is taken from your computer's local clock at the time the entry is created. The program intentionally has no option to backdate entries.

## Project structure

```text
activity-gen/
├── activity_gen.py
├── activity_log.csv
├── tests/
│   └── test_activity_gen.py
├── .github/
│   └── workflows/
│       └── tests.yml
├── .gitignore
└── README.md
```

## GitHub contributions

Logging an entry changes the local CSV file; it does not itself create a GitHub contribution. To publish genuine work, review your changes and commit them with Git:

```bash
git add activity_gen.py activity_log.csv
git commit -m "Log completed project work"
git push
```

Only commit work you actually completed. GitHub applies its own rules for which commits count toward the contribution graph.

## License

MIT
