![InBrief](header.png)

![CI](https://img.shields.io/github/actions/workflow/status/pabooth/inbrief/ci.yml?branch=main)
![License: MIT](https://img.shields.io/badge/license-MIT-green)
![Version](https://img.shields.io/github/v/release/pabooth/inbrief)

InBrief reads messages received during the previous 24 hours from selected Gmail
labels, asks a configured Claude, OpenAI, or DeepSeek model to produce a concise
digest, and sends one digest per label by email.

> [!WARNING]
> InBrief sends the contents of matching emails to the configured AI provider.
> Do not use it with sensitive mail unless that data transfer is acceptable
> under your security, privacy, and compliance requirements.

## Requirements

- Python 3.10 or newer
- [pipx](https://pipx.pypa.io/) for an isolated command-line installation
- A Google Cloud OAuth desktop client with the Gmail API enabled
- An Anthropic, OpenAI, or DeepSeek API key
- An SMTP account

## Installation

Install the latest released version in its own managed environment:

```console
pipx install "git+https://github.com/pabooth/inbrief.git@v1.3.3"
```

If `pipx` is not already installed on macOS:

```console
brew install pipx
pipx ensurepath
```

On other platforms, follow the
[pipx installation instructions](https://pipx.pypa.io/stable/installation/).
You may need to open a new terminal after running `pipx ensurepath`.

`pipx` keeps InBrief and its Python dependencies out of the system Python
environment. It normally stores the environment under
`~/.local/share/pipx/venvs/inbrief/` and exposes `inbrief` and
`inbrief-oauth` through `~/.local/bin/`.

To install a newer release, replace `X.Y.Z` below with the released version:

```console
pipx install --force "git+https://github.com/pabooth/inbrief.git@vX.Y.Z"
```

To remove InBrief:

```console
pipx uninstall inbrief
```

## Quick start

On first use, `inbrief` or `inbrief-oauth` creates
`~/.config/inbrief/config` from the bundled example if no existing
configuration is present. Edit that file with your Gmail label IDs, sender,
recipient, SMTP host, timezone, and digest preferences.

Keep secrets out of the file where practical:

```console
export INBRIEF_ANTHROPIC_API_KEY='...'
export INBRIEF_OPENAI_API_KEY='...'
export INBRIEF_DEEPSEEK_API_KEY='...'
export INBRIEF_SMTP_USER='...'
export INBRIEF_SMTP_PASSWORD='...'
```

Only the API key for the configured provider is required. Select the provider
and model in `[ai]`:

```ini
[ai]
provider = anthropic
model = claude-opus-4-8
max_tokens = 4096
timeout_seconds = 120
```

`provider` may be `anthropic`, `openai`, or `deepseek`. Model IDs are passed
through without an allow-list. This supports every Claude model available
through Anthropic's Messages API, including Opus, as well as OpenAI Responses
models such as `gpt-5.5` and DeepSeek models such as `deepseek-v4-flash` and
`deepseek-v4-pro`.

`INBRIEF_CONFIG` can specify a different configuration file. The previous
`~/.config/inbrief/inbrief.conf` and original `~/.local/etc/inbrief.conf`
locations remain supported for compatibility.

### Google OAuth

1. In Google Cloud, enable the Gmail API and create an OAuth client with
   application type **Desktop app**.
2. Download its JSON file to `~/.config/inbrief/credentials.json`.
3. Complete the browser authorisation flow:

```console
inbrief-oauth
inbrief-oauth --version
```

The resulting token is restricted to read-only Gmail access and is written with
owner-only permissions.

### Gmail label IDs

The values in `[labels]` are Gmail label IDs, not necessarily their visible
names. You can retrieve them with the Gmail API
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
inbrief --config /path/to/config
inbrief --version
inbrief --help
```

`--dry-run` still reads Gmail and calls the configured AI provider, but prints
the digest instead of sending it through SMTP. A failed label does not prevent
later labels from being processed; the command exits non-zero if any label
fails.

For unattended operation, invoke `inbrief` from cron, systemd, launchd, or
another scheduler. Use `command -v inbrief` to find its absolute path for the
scheduler, and ensure the scheduler receives the required environment
variables.

## Security notes

- Never commit `config`, `inbrief.conf`, OAuth client files, OAuth tokens, API
  keys, or SMTP credentials. The included `.gitignore` excludes the common
  local filenames.
- Email bodies are untrusted input. InBrief separates them in the model prompt
  and escapes generated HTML, but prompt-injection risk cannot be eliminated
  entirely.
- SMTP uses verified TLS by default. Set `security = ssl` for implicit TLS or
  `security = none` only for a trusted local relay.
- The Gmail token grants read-only mailbox access. Revoke it from your Google
  account if the machine or token file is compromised.

## Development

```console
git clone https://github.com/pabooth/inbrief.git
cd inbrief
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -e ".[dev]"
ruff check .
pytest
python -m build
```

The editable installation keeps the `inbrief` and `inbrief-oauth` commands
linked to the checked-out source. Reactivate `.venv` in each new terminal
before running development commands.

See [CONTRIBUTING.md](CONTRIBUTING.md), [SECURITY.md](SECURITY.md), and
[SUPPORT.md](SUPPORT.md).

## License

MIT © 2026 Paul Booth. See [LICENSE](LICENSE).
