# Onboarding Task Schedule

Expand a small onboarding template into dated employee task assignments.

Uses Python 3.10+ and its standard library only. No package installation, virtual
environment, external service, or network access is required.

## Run

```console
python -m onboarding_tool --help
python -m onboarding_tool examples/sample.json
python -m onboarding_tool --check-fixtures fixtures/cases.jsonl
python generate_fixtures.py --count 20
python -m unittest discover -s tests -v
```

Run from this directory. The optional path defaults to `-`, which reads JSON from
stdin. Output is JSON or a fixture-check summary. Exit codes are 0 success,
1 file failure, and 2 invalid input. Examples and fixtures contain generated data.

Requires employee_id, hire_date, and template [{id,offset_days,title}] (up to 100). Offsets range -30 to 365 calendar days. IDs are unique and assignments sort by due date then ID. Weekends are not shifted. No tasks, messages, or external accounts are created.

## Learning focus

Independent concept exercise for modeled blueprint section B03. This is an independent concept exercise based on the modeled
roadmap. It makes no claim to be employer-owned or period-authentic production code.

## Structure

- `onboarding_tool/core.py`: validated parsing, storage, or state transitions.
- `onboarding_tool/cli.py`: JSON command interface.
- `onboarding_tool/generate_fixtures.py`: original deterministic validation cases.
- `onboarding_tool/fixture_check.py`: expected-output/error checks.
- `fixtures/cases.jsonl`: 492 generated cases, with explicit descriptions.
- `tests/`: independently selected boundaries and the complete corpus check.

Branches `feature/core`, `feature/cli`, `data/fixtures`, and `docs/usage` retain
snapshots; `main` contains the complete tool. Dates and provenance are also recorded
in TIMELINE.json. Many data cases share a scenario; they are not separate features.

Keep changes focused, use actual dates for new work, and add a regression test
for changed behavior. Licensed under [MIT](LICENSE).

[History and provenance](HISTORY.md).
