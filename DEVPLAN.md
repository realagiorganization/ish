# Development Plan

## Goals
- Build the iOS app locally with Xcode.
- Build and test the CLI emulator tooling on macOS/Linux.
- Automate CI checks, BDD verification, and TestFlight releases.

## Steps
1. Clone the repository with submodules (`git clone --recurse-submodules`).
2. Install macOS build prerequisites (Xcode, command line tools, Homebrew, Ruby/Bundler).
3. Install cross-platform build prerequisites (Python 3, Meson, Ninja, Clang/LLD, sqlite3, libarchive).
4. Open `iSH.xcodeproj` in Xcode and update signing as noted in `README.md`.
5. For internal Debug builds, validate FiraCode fonts appear in Settings → Font picker.
6. Build and run the app on simulator or device.
7. For CLI testing, run `meson build` and `ninja` to build the command line emulator.
8. Run end-to-end tests in `tests/e2e` as needed.
9. Run BDD tests via `tests/bdd/run_bdd.sh`.
10. Use GitHub Actions to run CI, BDD, and TestFlight release workflows.

## External Dependencies
- Apple Xcode + command line tools (build, run, and test the iOS app).
- Apple Developer account + App Store Connect (signing and TestFlight upload).
- Fastlane (build automation and TestFlight uploads).
- Homebrew (macOS package manager for build deps).
- Meson + Ninja (CLI build tooling).
- Clang + LLD (compiler and linker for emulator components).
- sqlite3 (runtime dependency for iSH data storage).
- libarchive (filesystem tooling for Alpine rootfs generation).
- GitHub Actions (CI automation for build, BDD, and release pipelines).
- Netlify deploy hook (GitHub Pages/website deploy pipeline).
- VHS + tmux (recording CLI interactions for README artifacts).
- OpenAI-compatible API key (Codex CLI BDD scenario).

## Artifacts
- GitHub Pages UI screenshots and GIFs live in `docs/assets/`.
- VHS captures are generated in CI and published to `docs/assets/`.
