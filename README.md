# RepoClue

Finding a good GitHub repository usually means searching, opening a dozen tabs, and sometimes cloning a project just to discover it's abandoned or not what you needed. RepoClue is a command-line tool that helps you judge public repositories before you clone them. Today, it searches GitHub from your terminal and shows each match's name, star count, description, and link. The goal is to go beyond search results: to help you tell whether a repository is relevant to what you need and whether it is well maintained, and to organize the ones worth coming back to. RepoClue is open source and in early development, so expect things to change.

## Installation

These steps work on Windows (Git Bash), macOS, and Linux.

**1. Clone the repository** — downloads the source code to your machine:
```bash
git clone https://github.com/arcaenux/RepoClue.git
cd RepoClue
```

**2. Create a virtual environment** — keeps RepoClue's dependencies separate from other Python projects:
```bash
python -m venv .venv
```

**3. Activate the virtual environment** — tells your terminal to use it:

*Windows (Git Bash):*
```bash
source .venv/Scripts/activate
```

*macOS / Linux:*
```bash
source .venv/bin/activate
```

**4. Install RepoClue** — `-e` means "editable": changes to the source take effect immediately without reinstalling:
```bash
pip install -e ".[dev]"
```

## Usage

```
repoclue QUERY [--language LANGUAGE] [--min-stars N] [--sort {stars,forks,updated}] [-l LIMIT]
```

`QUERY` is required. All other options are optional.

**Examples:**

```bash
repoclue "web scraper"
repoclue "web scraper" --language python --min-stars 100
repoclue "machine learning" --sort forks --limit 10
```

**Example output:**

```
Found 847 matching repositories.

psf/requests  ★ 52341
A simple, yet elegant, HTTP library.
https://github.com/psf/requests

...
```

For full option descriptions and error message explanations, see [docs/usage.md](docs/usage.md).

## Project layout

```
repoclue/
├── src/repoclue/
│   ├── cli.py          # Argument parsing and main entry point
│   ├── display.py      # Formats and prints search results
│   └── github/
│       └── client.py   # Talks to the GitHub search API
├── tests/
│   └── test_search.py  # Automated tests (no internet required)
├── docs/               # Detailed documentation
├── pyproject.toml      # Project metadata and dependencies
└── LICENSE
```

## Running tests

```bash
pytest
```

## Roadmap

These are planned, not yet built:

- Score repositories by relevance and maintenance signals
- Save interesting repositories to a local list
- Show richer metadata (last commit date, open issues, language breakdown)

## License

MIT — see [LICENSE](LICENSE).
