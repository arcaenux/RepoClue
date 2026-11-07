# Development

## Setup

**Requirements:** Python 3.11 or newer, Git.

```bash
git clone https://github.com/arcaenux/RepoClue.git
cd RepoClue
python -m venv .venv
source .venv/Scripts/activate   # Windows Git Bash
# source .venv/bin/activate     # macOS / Linux
pip install -e ".[dev]"
```

The `.[dev]` part installs the project itself plus the development tools
(pytest and respx).

## Running tests

```bash
pytest
```

Tests live in `tests/test_search.py`. They use `respx` to fake HTTP
responses, so no internet connection is required and no real GitHub
requests are made.

## Making changes

1. Make your edits in `src/repoclue/`.
2. Run `pytest` to check nothing broke.
3. Stage and commit your changes:

```bash
git add <file>
git commit -m "short description of what changed and why"
```

4. Push to your branch:

```bash
git push
```

## Checking what changed before committing

```bash
git diff          # shows uncommitted changes line by line
git status        # shows which files are modified or untracked
git log --oneline # shows recent commit history
```

## Project structure

See [architecture.md](architecture.md) for a full breakdown of which
file is responsible for what.
