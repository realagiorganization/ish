import os
import subprocess
from pathlib import Path
from behave import given, when, then


def _codex_key():
    return os.environ.get("CODEX_API_KEY") or os.environ.get("OPENAI_API_KEY")


@given("a Codex API key is available")
def step_codex_key_available(context):
    key = _codex_key()
    assert key, "Missing CODEX_API_KEY or OPENAI_API_KEY in environment"
    context.codex_key = key


@when("I run a Codex prompt in tmux")
def step_run_codex_prompt(context):
    prompt = "Say hello from the iSH BDD suite."
    env = os.environ.copy()
    env["CODEX_API_KEY"] = context.codex_key
    subprocess.run(["tools/run_codex_tmux.sh", prompt], check=True, env=env)


@then("the Codex response log should include output text")
def step_codex_output_present(context):
    output_file = Path("prompt_artifacts/codex_cli_output.txt")
    assert output_file.exists(), "Codex output file missing"
    content = output_file.read_text(encoding="utf-8").strip()
    assert content, "Codex output was empty"
