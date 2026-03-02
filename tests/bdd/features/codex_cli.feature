@codex
Feature: Codex CLI in tmux
  As a CI pipeline
  I want to validate a Codex CLI request in tmux
  So the encrypted LLM key is exercised during BDD runs

  Scenario: Run Codex CLI request via tmux
    Given a Codex API key is available
    When I run a Codex prompt in tmux
    Then the Codex response log should include output text
