# Changelog

All notable changes to this project are documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

## [0.1.0] - 2026-11-17

### Added

- Search public GitHub repositories from the command line with `repoclue QUERY`.
- Filter results by programming language with `--language`.
- Filter results by minimum star count with `--min-stars`.
- Sort results by stars, forks, or last update with `--sort`.
- Limit the number of results with `--limit` (1-100).
- Print each repository's full name, star count, description, and URL.
- Show a clear message and exit with code 1 for empty queries, GitHub API errors, rate limits, and network failures.

[Unreleased]: https://github.com/arcaenux/RepoClue/compare/v0.1.0...HEAD
[0.1.0]: https://github.com/arcaenux/RepoClue/releases/tag/v0.1.0
