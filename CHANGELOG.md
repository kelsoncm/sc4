# Changelog

All notable changes to this project are documented in this file.

## Unreleased

## [0.2.0] - 2026-04-08 (sc4net)

### Added

* sc4net tests for `post` and `post_json` using local HTTP mock endpoints.
* CI test matrix expanded to Python `3.10`, `3.11`, `3.12`, `3.13`, and `3.14`.
* Pre-commit workflow to run the same checks used in CI quality/test jobs.

### Changed

* sc4net networking layer migrated to Python stdlib:
  * FTP via `ftplib`
  * HTTP(S) via `urllib.request`
* sc4net no longer requires `requests` or `requests_ftp` as runtime dependencies.
* CI installation steps now rely on stdlib-only sc4net requirements.

### Notes

* This update improves compatibility with modern Python versions (including Python 3.13+ where `cgi` removal affected `requests_ftp`).

## [0.1.5] - 2026-04-08 (sc4py)

### Added

* New tests for `sc4py.choice`.
* Additional test coverage for `daterange` and ZIP helper branches.

### Changed

* Coverage and test quality improvements to support stricter CI gates.
