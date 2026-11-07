# Usage

## Running a search

```
repoclue QUERY [--language LANGUAGE] [--min-stars N] [--sort {stars,forks,updated}] [-l LIMIT]
```

`QUERY` is the only required argument. Put it in quotes if it contains spaces.

### Options

| Option | Description | Default |
|--------|-------------|---------|
| `QUERY` | Search keywords | required |
| `--language` | Filter by programming language (e.g. `python`, `go`) | any |
| `--min-stars` | Only show repositories with at least this many stars | none |
| `--sort` | Sort by `stars`, `forks`, or `updated` | `stars` |
| `-l`, `--limit` | Maximum number of results to show (1–100) | 5 |

### Examples

```bash
# Simple search
repoclue "markdown parser"

# Filter by language and minimum stars
repoclue "web scraper" --language python --min-stars 100

# Show 10 results, sorted by most recently updated
repoclue "data pipeline" --sort updated --limit 10
```

### Example output

```
Found 1284 matching repositories.

scrapy/scrapy  ★ 51200
Scrapy, a fast high-level web crawling & scraping framework for Python.
https://github.com/scrapy/scrapy

...
```

Each result shows the repository's full name, star count, description, and link.

## Error messages

### Empty search query

```
Error: Search query cannot be empty
```

Cause: you passed an empty string as the query. Provide at least one keyword.

### No internet / cannot reach GitHub

```
Could not reach GitHub. Check your internet connection: ...
```

Cause: the request never reached GitHub. Check that you are online.

### GitHub rate limit exceeded

```
GitHub API rate limit exceeded. Please try again later.
```

Cause: GitHub limits unauthenticated API requests to 10 per minute. Wait a minute and try again.

### Other GitHub API error

```
GitHub API returned an error: 422 Unprocessable Entity
```

Cause: GitHub rejected the request (for example, an unsupported query format). The status code and reason are shown.

## Exit codes

| Code | Meaning |
|------|---------|
| `0` | Search completed successfully |
| `1` | Any error (bad input, network failure, API error) |
