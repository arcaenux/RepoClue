"""Format and display repository search results."""

def format_results(result: dict) -> None:
    """Print repository search results to the terminal."""
    print(f"\nFound {result['total_count']} matching repositories.\n")
    for repo in result["items"]:
        print(f"{repo['full_name']}  ★ {repo['stargazers_count']}")
        print(repo["description"] or "No description provided.")
        print(repo["html_url"])
        print()