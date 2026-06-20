![InBrief](https://raw.githubusercontent.com/pabooth/inbrief/main/header.png)

# InBrief

[![CI](https://github.com/pabooth/inbrief/actions/workflows/ci.yml/badge.svg)](https://github.com/pabooth/inbrief/actions/workflows/ci.yml)
[![License: MIT](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)

InBrief reads messages received during the previous 24 hours from selected Gmail
labels, asks Claude to produce a concise digest, and sends one digest per label by
email.

> [!IMPORTANT]
> InBrief sends the contents of matching emails to Anthropic. Do not use it with
> sensitive mail unless that data transfer is acceptable under your security,
> privacy, and compliance requirements.

## Requirements

- Python 3.10 or newer
- A Google Cloud OAuth desktop client with the Gmail API enabled
- An Anthropic API key
- An SMTP account

## Install

Clone the repository and install it in a virtual environment:

```console
git clone https://github.com/pabooth/inbrief.git
cd inbrief
python3 -m venv .venv
source .venv/bin/activate
python -m pip install .
```

For development, use `python -m pip install -e ".[dev]"`.

## Configure

Create the configuration directory and copy the example:

```console
mkdir -p ~/.config/inbrief
cp config.example ~/.config/inbrief/inbrief.conf
chmod 600 ~/.config/inbrief/inbrief.conf
```

Edit the file with your Gmail label IDs, sender, recipient, SMTP host, timezone,
and digest preferences.

Keep secrets out of the file where practical:

```console
export INBRIEF_ANTHROPIC_API_KEY='...'
export INBRIEF_SMTP_USER='...'
export INBRIEF_SMTP_PASSWORD='...'
```

`INBRIEF_CONFIG` can specify a different configuration file. The original
`~/.local/etc/inbrief.conf` location remains supported for compatibility.

### Google OAuth

1. In Google Cloud, enable the Gmail API and create an OAuth client with application
   type **Desktop app**.
2. Download its JSON file to `~/.config/inbrief/credentials.json`.
3. Complete the browser authorization flow:

```console
inbrief-oauth
```

The resulting token is restricted to read-only Gmail access and is written with
owner-only permissions.

### Gmail label IDs

The values in `[labels]` are Gmail label IDs, not necessarily their visible names.
You can retrieve them with the Gmail API
[`users.labels.list`](https://developers.google.com/gmail/api/reference/rest/v1/users.labels/list)
or an API client. Each key is the display name used in the generated email:

```ini
[labels]
Technology = Label_123456789
Security = Label_987654321
```

## Run

```console
inbrief
```

Useful options:

```console
inbrief --dry-run
inbrief --label Technology
inbrief --config /path/to/inbrief.conf
inbrief --help
```

`--dry-run` still reads Gmail and calls Anthropic, but prints the digest instead of
sending it through SMTP. A failed label does not prevent later labels from being
processed; the command exits non-zero if any label fails.

For unattended operation, invoke `inbrief` from cron, systemd, launchd, or another
scheduler. Ensure the scheduler receives the required environment variables.

## Security notes

- Never commit `inbrief.conf`, OAuth client files, OAuth tokens, API keys, or SMTP
  credentials. The included `.gitignore` excludes the common local filenames.
- Email bodies are untrusted input. InBrief separates them in the model prompt and
  escapes generated HTML, but prompt-injection risk cannot be eliminated entirely.
- SMTP uses verified TLS by default. Set `security = ssl` for implicit TLS or
  `security = none` only for a trusted local relay.
- The Gmail token grants read-only mailbox access. Revoke it from your Google account
  if the machine or token file is compromised.

See [SECURITY.md](SECURITY.md) for vulnerability reporting.

## Development

```console
ruff check .
pytest
python -m build
```

Contributions are covered by the [MIT License](LICENSE). See
[CONTRIBUTING.md](CONTRIBUTING.md).
