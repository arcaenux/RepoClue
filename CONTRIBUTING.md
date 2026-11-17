# Contributing to RepoClue

Thanks for your interest in RepoClue. This project is in early development, so small, focused contributions are the easiest to review.

## Report a bug

1. Check the [existing issues](https://github.com/arcaenux/RepoClue/issues) to see whether the bug is already reported.
2. If it is new, open an issue.
3. Include:
   - the exact command you ran,
   - what you expected to happen,
   - what actually happened (copy the full error message),
   - your operating system and Python version.

## Suggest a feature

Open an issue and describe:

- the problem you want RepoClue to solve,
- what you would like it to do,
- any alternatives you considered.

Please open an issue before writing a large change, so we can agree on the approach first.

## Submit a change

1. Fork the repository and clone your fork.
2. Create a branch for your change:

   ```bash
   git checkout -b my-change
   ```

3. Make your change. Add or update tests when behavior changes.
4. Run the tests:

   ```bash
   pytest
   ```

5. Commit with a clear message:

   ```bash
   git add <file>
   git commit -m "short description of what changed and why"
   ```

6. Push your branch and open a pull request against `main`.
7. In the pull request, explain what changed and why. Link the issue it fixes, if there is one.

## Development setup

See [docs/development.md](docs/development.md) for how to create a virtual environment, install the project, and run the tests.

## Questions

If something is unclear, open an issue and ask. There are no silly questions.
