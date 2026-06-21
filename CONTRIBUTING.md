# Contributing

Bug reports and focused pull requests are welcome.

Participation in this project is governed by the
[Code of Conduct](./CODE_OF_CONDUCT.md).
Maintainer releases follow [RELEASING.md](./RELEASING.md).

1. Fork and clone the repository.
2. Create a virtual environment.
3. Run `python -m pip install -e ".[dev]"`.
4. Run `ruff check .` and `pytest` before opening a pull request.

Never commit Gmail OAuth files, API keys, SMTP passwords, or private email content.
