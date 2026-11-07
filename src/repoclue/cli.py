"""Command-line entry point for RepoClue."""

import httpx
import argparse
import sys

from repoclue.github.client import GitHubClient
from repoclue.display import format_results

def parse_args(argv: list[str] | None = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        prog="repoclue",
        description="Search for public GitHub repositories from the command line.",
    )
    parser.add_argument("query", help="Search query (e.g., 'python web framework')")
    parser.add_argument("--language", help="Filter by programming language (e.g., 'Python')")
    parser.add_argument("--min-stars", type=int, help="Filter by minimum number of stars (e.g., 100)")
    parser.add_argument("--sort", choices=["stars", "forks", "updated"], default="stars", help="Sort results by (default: stars)")
    parser.add_argument("-l", "--limit", type=int, default=5, help="Max results to return (default: 5)")

    return parser.parse_args(argv)


def main() -> None:
    args = parse_args()

    try:
        with GitHubClient() as client:
            result = client.search_repositories(args.query, language=args.language, min_stars=args.min_stars, sort=args.sort, limit=args.limit)
        
        format_results(result)

    except ValueError as error:
        print(f"Error: {error}")
        sys.exit(1)

    except httpx.HTTPStatusError as error:
        if error.response.status_code in (403, 429):
            print("GitHub API rate limit exceeded. Please try again later.")
            sys.exit(1)
        else:
            print(f"GitHub API returned an error: {error.response.status_code} {error.response.reason_phrase}")
            sys.exit(1)
    except httpx.RequestError as error:
        print(f"Could not reach GitHub. Check your internet connection: {error}")
        sys.exit(1)

if __name__ == "__main__":
    main()
