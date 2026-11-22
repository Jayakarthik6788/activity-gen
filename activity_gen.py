#!/usr/bin/env python3
"""Record genuine project work in a local CSV activity log.

This tool records the local date/time when an entry is created. It does not
create Git commits, backdate entries, or manufacture GitHub contributions.
"""
from __future__ import annotations

import argparse
import csv
from datetime import date, datetime, timedelta
from pathlib import Path
from typing import Iterable

ROOT = Path(__file__).resolve().parent
LOG_FILE = ROOT / "activity_log.csv"
FIELDS = ("date", "time", "project", "task", "outcome")


def ensure_log(path: Path = LOG_FILE) -> None:
    """Create the CSV log with a header if it does not already exist."""
    if not path.exists():
        path.parent.mkdir(parents=True, exist_ok=True)
        with path.open("w", newline="", encoding="utf-8") as handle:
            csv.DictWriter(handle, fieldnames=FIELDS).writeheader()


def record_activity(
    project: str,
    task: str,
    outcome: str = "",
    *,
    path: Path = LOG_FILE,
    now: datetime | None = None,
) -> dict[str, str]:
    """Append one activity entry using the current local date and time."""
    project = project.strip()
    task = task.strip()
    outcome = outcome.strip()
    if not project:
        raise ValueError("Project cannot be blank.")
    if not task:
        raise ValueError("Task cannot be blank.")

    timestamp = now or datetime.now().astimezone()
    entry = {
        "date": timestamp.date().isoformat(),
        "time": timestamp.strftime("%H:%M:%S %Z").strip(),
        "project": project,
        "task": task,
        "outcome": outcome,
    }
    ensure_log(path)
    with path.open("a", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=FIELDS)
        writer.writerow(entry)
    return entry


def read_activities(path: Path = LOG_FILE) -> list[dict[str, str]]:
    """Return all activity entries from the CSV log."""
    ensure_log(path)
    with path.open("r", newline="", encoding="utf-8") as handle:
        return list(csv.DictReader(handle))


def active_week_summary(rows: Iterable[dict[str, str]]) -> tuple[int, int]:
    """Return (number of active ISO weeks, longest consecutive-week run)."""
    weeks = set()
    for row in rows:
        try:
            logged_date = date.fromisoformat(row["date"])
        except (KeyError, TypeError, ValueError):
            continue
        iso = logged_date.isocalendar()
        weeks.add((iso.year, iso.week))

    if not weeks:
        return 0, 0

    ordered = sorted(weeks)
    longest = current = 1
    first_year, first_week = ordered[0]
    previous_monday = date.fromisocalendar(first_year, first_week, 1)
    for year, week in ordered[1:]:
        monday = date.fromisocalendar(year, week, 1)
        if monday - previous_monday == timedelta(days=7):
            current += 1
        else:
            current = 1
        longest = max(longest, current)
        previous_monday = monday
    return len(weeks), longest


def print_activities(rows: Iterable[dict[str, str]]) -> None:
    rows = list(rows)
    if not rows:
        print("No activity recorded yet.")
        return
    for row in rows:
        print(
            f'{row["date"]} {row["time"]} | {row["project"]} | {row["task"]}'
        )
        if row.get("outcome"):
            print(f'  Outcome: {row["outcome"]}')


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Track real project work in a dated CSV activity log."
    )
    commands = parser.add_subparsers(dest="command", required=True)

    add = commands.add_parser("add", help="Record work you actually completed.")
    add.add_argument("--project", required=True, help="Project or repository name.")
    add.add_argument("--task", required=True, help="Specific work completed.")
    add.add_argument("--outcome", default="", help="Result or evidence (optional).")

    commands.add_parser("list", help="List recorded activity.")
    commands.add_parser("stats", help="Show activity-log statistics.")
    return parser


def main(argv: list[str] | None = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)

    try:
        if args.command == "add":
            entry = record_activity(args.project, args.task, args.outcome)
            print(f'Logged work for {entry["date"]}.')
            print(f"Saved to {LOG_FILE.name}.")
        elif args.command == "list":
            print_activities(read_activities())
        elif args.command == "stats":
            rows = read_activities()
            days = sorted({row["date"] for row in rows})
            active_weeks, longest_streak = active_week_summary(rows)
            print(f"Entries: {len(rows)}")
            print(f"Distinct work days: {len(days)}")
            print(f"Active ISO weeks: {active_weeks}")
            print(f"Longest consecutive active-week streak: {longest_streak}")
            if days:
                print(f"First logged day: {days[0]}")
                print(f"Latest logged day: {days[-1]}")
        return 0
    except (OSError, ValueError, csv.Error) as error:
        parser.error(str(error))
    return 2


if __name__ == "__main__":
    raise SystemExit(main())
