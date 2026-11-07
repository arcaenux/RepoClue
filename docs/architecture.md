# Architecture

## File responsibilities

```
src/repoclue/
├── __init__.py         # Package marker; holds the version number
├── cli.py              # Entry point: parses arguments, calls the client,
│                       # calls the display function, handles errors
├── display.py          # Formats search results and prints them
└── github/
    ├── __init__.py     # Package marker
    └── client.py       # Sends HTTP requests to the GitHub search API
                        # and returns the raw JSON response
```

**`cli.py`** owns the user interface. It knows what arguments the user typed and what to print when something goes wrong. It does not know how HTTP works or how to format a result.

**`github/client.py`** owns the network layer. It knows how to talk to GitHub — the URL, the headers, the query format. It does not know what the user typed or how results are displayed.

**`display.py`** owns the presentation layer. It knows how to turn a GitHub JSON response into readable terminal output. It does not know how the data was fetched.

This separation means you can change how results are displayed without touching the HTTP code, and you can swap the data source without touching the display code.

## How a search flows through the program

```
User types:  repoclue "web scraper" --language python

cli.py        parse_args()          reads sys.argv, returns args.query,
                                    args.language, args.min_stars, etc.

cli.py        main()                calls GitHubClient.search_repositories()

github/       search_repositories() builds the query string:
client.py                           "web scraper language:python"
                                    sends GET /search/repositories?q=...
                                    to api.github.com
                                    returns the JSON dict

cli.py        main()                passes the dict to format_results()

display.py    format_results()      prints name, stars, description, URL
                                    for each repository in the response
```

## Dependencies

- **httpx** — the HTTP client library used to make requests to GitHub.
- **pytest + respx** — test runner and HTTP mocking library (dev only).
