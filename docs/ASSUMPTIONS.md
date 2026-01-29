# Assumptions

- GitHub Actions provides an LLM API key via `CODEX_API_KEY` (fallback accepted: `OPENAI_API_KEY`) for the Codex CLI BDD scenario.
- The TestFlight release workflow should reuse the same App Store Connect and signing secrets already used by `Upload Build`.
- "Internal build" maps to the Debug configuration; FiraCode fonts are bundled for Debug builds via `INTERNAL_BUILD=YES` and are not required for release builds.
- GitHub Pages screenshots from the prompt attachments represent the current UI and can be stored under `docs/assets/` for README display.
- VHS-generated GIFs cannot be recorded locally here, so placeholder GIFs are committed and the `bdd` workflow will overwrite them on CI.
- The TestFlight release workflow should only run for the canonical repo `realagiorganization/ish`.
