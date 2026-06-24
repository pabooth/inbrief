# Contributing

Bug reports and focused pull requests are welcome.

Participation in this project is governed by the
[Code of Conduct](./CODE_OF_CONDUCT.md).
Maintainer releases follow [RELEASING.md](./RELEASING.md).

1. Fork and clone the repository.
2. Create and activate a project-local virtual environment:

   ```console
   python3 -m venv .venv
   source .venv/bin/activate
   ```

3. Install the project and development dependencies in editable mode:

   ```console
   python -m pip install -e ".[dev]"
   ```

4. Run `ruff check .`, `pytest`, and `python -m build` before opening a pull
   request.

The `.venv` directory is for development only and is excluded from version
control. End-user installations should use the `pipx` process documented in
the README.

Never commit Gmail OAuth files, API keys, SMTP passwords, or private email content.
