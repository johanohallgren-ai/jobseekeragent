# JobSeekerAgent

JobSeekerAgent is a lightweight Python package that helps rank job postings against a candidate profile.

## Features

- Candidate/job datamodels via dataclasses.
- Match scoring based on:
  - required skill overlap
  - target title relevance
  - preferred location
- Ranking API to sort postings by best fit first.
- A small CLI demo output.

## Project structure

- `src/jobseekeragent/agent.py` — core domain model and ranking logic
- `src/jobseekeragent/cli.py` — demo runner
- `tests/test_agent.py` — unit tests for scoring and ranking

## Quickstart

```bash
python -m venv .venv
source .venv/bin/activate
pip install -e .
pytest
python -m jobseekeragent.cli
```

## Example output

```text
Top matches for Alex:
- Senior Data Engineer (Remote) => 0.97
- Backend Engineer (Munich) => 0.53
```
