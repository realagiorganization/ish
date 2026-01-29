#!/usr/bin/env python3
import argparse
import json
import os
import sys
import urllib.request
import urllib.error
from pathlib import Path


def read_prompt(args: argparse.Namespace) -> str:
    if args.prompt:
        return args.prompt
    if args.prompt_file:
        return Path(args.prompt_file).read_text(encoding="utf-8")
    env_prompt = os.environ.get("CODEX_PROMPT")
    if env_prompt:
        return env_prompt
    raise ValueError("No prompt provided")


def extract_text(data: dict) -> str:
    for item in data.get("output", []):
        if item.get("type") == "message":
            for content in item.get("content", []):
                if content.get("type") in ("output_text", "text"):
                    return content.get("text", "")
    # Fallback for legacy formats
    choices = data.get("choices", [])
    if choices:
        return choices[0].get("message", {}).get("content", "")
    return ""


def main() -> int:
    parser = argparse.ArgumentParser(description="Minimal Codex CLI helper")
    parser.add_argument("--prompt", help="Prompt text")
    parser.add_argument("--prompt-file", help="Path to prompt file")
    parser.add_argument("--out-json", required=True, help="Output JSON path")
    parser.add_argument("--out-text", required=True, help="Output text path")
    args = parser.parse_args()

    api_key = os.environ.get("CODEX_API_KEY") or os.environ.get("OPENAI_API_KEY")
    if not api_key:
        raise ValueError("Missing CODEX_API_KEY or OPENAI_API_KEY")

    prompt = read_prompt(args).strip()
    if not prompt:
        raise ValueError("Prompt was empty")

    model = os.environ.get("CODEX_MODEL", "gpt-4.1-mini")
    payload = {
        "model": model,
        "input": [
            {
                "role": "user",
                "content": [
                    {"type": "input_text", "text": prompt}
                ],
            }
        ],
    }

    req = urllib.request.Request(
        "https://api.openai.com/v1/responses",
        data=json.dumps(payload).encode("utf-8"),
        headers={
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json",
        },
        method="POST",
    )

    try:
        with urllib.request.urlopen(req) as resp:
            data = json.loads(resp.read().decode("utf-8"))
    except urllib.error.HTTPError as exc:
        error_body = exc.read().decode("utf-8")
        data = {"error": error_body, "status": exc.code}

    out_json = Path(args.out_json)
    out_text = Path(args.out_text)
    out_json.parent.mkdir(parents=True, exist_ok=True)
    out_text.parent.mkdir(parents=True, exist_ok=True)

    out_json.write_text(json.dumps(data, indent=2), encoding="utf-8")
    text = extract_text(data).strip()
    out_text.write_text(text, encoding="utf-8")

    if text:
        print(text)
    else:
        print("No output text returned.")

    return 0


if __name__ == "__main__":
    sys.exit(main())
