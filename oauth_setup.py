#!/usr/bin/env python3
"""Create the Gmail OAuth token used by InBrief."""

from __future__ import annotations

import argparse
import sys
from collections.abc import Sequence
from pathlib import Path

from inbrief import (
    GMAIL_READONLY_SCOPE,
    default_config_path,
    install_example_config,
    load_config,
    read_version,
    resolve_config_path,
)


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(prog="inbrief-oauth", description=__doc__)
    parser.add_argument(
        "--version",
        action="version",
        version=f"%(prog)s {read_version()}",
    )
    parser.add_argument("--config", type=Path, default=default_config_path())
    parser.add_argument(
        "--client-secrets",
        type=Path,
        help="Google OAuth desktop client JSON; overrides [gmail] client_secrets_file",
    )
    return parser


def main(argv: Sequence[str] | None = None) -> int:
    args = build_parser().parse_args(argv)

    try:
        from google_auth_oauthlib.flow import InstalledAppFlow
    except ImportError:
        print(
            "Google OAuth dependencies are missing. Install the project first.",
            file=sys.stderr,
        )
        return 2

    try:
        install_example_config(args.config)
        cfg = load_config(args.config)
        client_secrets = args.client_secrets or resolve_config_path(
            cfg,
            cfg.get("gmail", "client_secrets_file", fallback="credentials.json"),
        )
        token_file = resolve_config_path(
            cfg, cfg.get("gmail", "token_file", fallback="token.json")
        )
        if not client_secrets.is_file():
            raise FileNotFoundError(f"OAuth client file not found: {client_secrets}")

        flow = InstalledAppFlow.from_client_secrets_file(
            str(client_secrets), [GMAIL_READONLY_SCOPE]
        )
        credentials = flow.run_local_server(port=0)
        token_file.parent.mkdir(parents=True, exist_ok=True)
        token_file.write_text(credentials.to_json(), encoding="utf-8")
        token_file.chmod(0o600)
        print(f"Wrote Gmail token to {token_file}")
        return 0
    except (FileNotFoundError, ValueError) as exc:
        print(exc, file=sys.stderr)
        return 2


if __name__ == "__main__":
    sys.exit(main())
