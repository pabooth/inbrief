# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to
[Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]
## [1.3.0] - 2026-06-24
Change the email template and footer


### Added

- Included the configured AI model's readable name in the email footer.

## [1.2.0] - 2026-06-24



## [1.2.0] - 2026-06-24

### Added

- Provider-neutral AI configuration supporting all Claude model IDs, OpenAI
  models including GPT-5.5, and DeepSeek models.
- Automatic installation of the bundled example configuration on first use.

### Changed

- Renamed the default configuration file to `~/.config/inbrief/config`, while
  retaining support for previous locations.
- Removed the fixed Anthropic temperature parameter for compatibility with
  Claude reasoning and Opus models.
- Documented isolated `pipx` installation for end users and a separate
  project-local editable environment for development.
- Restyled HTML digests with an editorial daily-newsletter template, including
  an at-a-glance section, numbered stories, and responsive email presentation.

### Fixed

- Ensured `provider = deepseek` dispatches to DeepSeek and reads
  `INBRIEF_DEEPSEEK_API_KEY` or `[deepseek] api_key`, rather than requesting
  Anthropic credentials.

## [1.1.0] - 2026-06-21

### Added

- `inbrief --version` using installed package metadata.
- `inbrief-oauth --version` using installed package metadata.
- Tag-driven GitHub release automation for wheel and source distributions.
- Bug report, feature request, and pull request templates.
- Code of conduct, support policy, and maintainer release documentation.
- Clean-environment wheel installation smoke tests in CI.

### Changed

- Removed lifecycle-status package metadata.
- Security and contribution documentation now use consistent project
  policies.

## [1.0.0] - 2026-06-21

### Added

- Gmail label ingestion using read-only OAuth access.
- Anthropic-generated email digests with SMTP delivery.
- Configuration, dry-run, label filtering, and OAuth setup commands.
- Security controls for credentials, generated HTML, and email headers.
- Automated tests, linting, packaging, and dependency updates.

[Unreleased]: https://github.com/pabooth/inbrief/compare/v1.2.0...HEAD
[1.2.0]: https://github.com/pabooth/inbrief/compare/v1.1.0...v1.2.0
[1.1.0]: https://github.com/pabooth/inbrief/compare/v1.0.0...v1.1.0
[1.0.0]: https://github.com/pabooth/inbrief/releases/tag/v1.0.0
