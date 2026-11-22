# 9-Month GitHub Contribution Roadmap

**Target:** 350+ meaningful GitHub contributions across 9 months, while staying active for at least 35 consecutive weeks.

This is a work plan, not a contribution generator. Only real work should be logged, committed, reviewed, or opened as an issue/PR. GitHub decides which activities appear on the contribution graph.

## Weekly pace

- Aim for 10 meaningful contribution events per week on average.
- Work on 4–5 days each week; do not create empty or duplicate commits to fill squares.
- Keep at least one real contribution in every target week for 35 consecutive weeks.
- Review progress every Sunday and adjust the next week's tasks.

350 contributions over roughly 39 weeks is about 9 contributions per week. The target is a stretch goal, not a guarantee.

## Suggested project rotation

| Day | Focus | Example of real work |
|---|---|---|
| Monday | Student Task Management System | Fix a bug, improve validation, or add a tested feature |
| Tuesday | Health Bot / HMMP | Improve input handling, documentation, or tests |
| Wednesday | 3-D Texture Segmentation | Reproduce an experiment, improve preprocessing, or document results |
| Thursday | Mini Compiler / Quiz App | Add a language feature, edge-case test, or accessibility improvement |
| Friday | Inventory / Omni-Sight / Guidewire | Resolve a real issue or improve an existing workflow |
| Saturday | Review and quality | Run tests, review diffs, improve README/API docs, or review a PR |
| Sunday | Weekly review | Summarize completed work and choose the next tasks |

Choose only repositories you are actively developing. Do not make cosmetic edits just to create commits.

## What counts as useful work

- A tested feature or bug fix.
- A meaningful documentation improvement tied to the actual implementation.
- A pull request with a clear change and review.
- A useful issue describing a reproducible bug or concrete enhancement.
- A code review that identifies actionable improvements.

A commit is not automatically a GitHub contribution. Some activity types have eligibility rules, and commits may need to be on the default branch or associated with a merged pull request.

## Weekly review checklist

- [ ] At least one real piece of work completed this week.
- [ ] Tests or manual verification performed where appropriate.
- [ ] Commit messages describe the actual change.
- [ ] README or issue tracker updated when useful.
- [ ] No empty, duplicate, or backdated commits.
- [ ] Next week's first task selected.

## Track completed work

Use the activity logger to record what was actually done:

```powershell
py activity_gen.py add --project "Student-Task-Management-System" --task "Describe the completed change" --outcome "Describe the test or result"
py activity_gen.py stats
```

The local activity log is a personal work journal; it does not itself create a GitHub contribution.

## Important

Do not expose access tokens, passwords, API keys, or private project data in commits. Keep private repositories private unless you intentionally choose to publish them.
