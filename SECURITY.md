# Security policy

Please report vulnerabilities privately through
[GitHub security advisories](https://github.com/pabooth/inbrief/security/advisories/new).
Do not include credentials, private email content, or OAuth tokens in a public issue.

Only the latest released version receives security fixes.

InBrief sends selected email content to the configured Anthropic API account and sends
the generated digest through the configured SMTP server. Review those providers'
privacy and retention terms before use. Email content is untrusted input: the prompt
includes injection-resistant instructions, but no model-level defence is absolute.
