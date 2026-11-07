import respx
import httpx
import pytest
from repoclue.github.client import GitHubClient
from repoclue.display import format_results

@respx.mock
def test_search_basic():
    respx.get("https://api.github.com/search/repositories").mock(
        return_value=httpx.Response(
            200,
            json={"total_count": 1, "items": [{"full_name": "a/b"}]},
        )
    )

    with GitHubClient() as client:
        result = client.search_repositories("web scraper")

    assert result["total_count"] == 1
    assert len(result["items"]) == 1


@respx.mock
def test_search_qualifiers():
    respx.get("https://api.github.com/search/repositories").mock(
        return_value=httpx.Response(
            200,
            json={"total_count": 0, "items": []},
        )
    )

    with GitHubClient() as client:
        client.search_repositories("web scraper", language="python", min_stars=100)

        sent_url = str(respx.calls.last.request.url)
        assert "language%3Apython" in sent_url
        assert "stars%3A%3E%3D100" in sent_url

def test_search_empty_query():
    with GitHubClient() as client:
        with pytest.raises(ValueError):
            client.search_repositories("")


@respx.mock
def test_rate_limit():
    # Fake a 429 response — same pattern as before, just a different status code.
    # Your code calls response.raise_for_status(), which turns any 4xx/5xx into
    # an httpx.HTTPStatusError. We assert that exact exception is raised.
    respx.get("https://api.github.com/search/repositories").mock(
        return_value=httpx.Response(429)
    )

    with GitHubClient() as client:
        with pytest.raises(httpx.HTTPStatusError):
            client.search_repositories("anything")


def test_format_results(capsys):
    # capsys is a pytest fixture — pytest passes it in automatically when you
    # name it as a parameter. It captures everything printed during the test.
    # After calling format_results, capsys.readouterr() gives you a snapshot
    # of stdout and stderr as plain strings you can assert against.
    fake_result = {
        "total_count": 1,
        "items": [
            {
                "full_name": "alice/awesome-repo",
                "stargazers_count": 42,
                "description": "A test repository.",
                "html_url": "https://github.com/alice/awesome-repo",
            }
        ],
    }

    format_results(fake_result)

    captured = capsys.readouterr()
    assert "alice/awesome-repo" in captured.out
    assert "https://github.com/alice/awesome-repo" in captured.out