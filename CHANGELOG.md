# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to
[Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

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

[Unreleased]: https://github.com/pabooth/inbrief/compare/v1.0.0...HEAD
[1.0.0]: https://github.com/pabooth/inbrief/releases/tag/v1.0.0
