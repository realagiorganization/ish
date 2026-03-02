from pathlib import Path
from behave import given, then


@given("the terminal web assets are present")
def step_terminal_assets_present(context):
    context.terminal_assets = [
        Path("app/terminal/term.html"),
        Path("app/terminal/term.js"),
        Path("app/terminal/term.css"),
    ]
    missing = [p for p in context.terminal_assets if not p.exists()]
    assert not missing, f"Missing terminal assets: {missing}"


@then("the terminal UI assets should be readable")
def step_terminal_assets_readable(context):
    for asset in context.terminal_assets:
        content = asset.read_text(encoding="utf-8")
        assert content.strip(), f"Empty asset: {asset}"


@given("the FiraCode font files are bundled")
def step_firacode_fonts_present(context):
    context.firacode_fonts = [
        Path("app/Fonts/FiraCode-Regular.ttf"),
        Path("app/Fonts/FiraCode-Medium.ttf"),
        Path("app/Fonts/FiraCode-SemiBold.ttf"),
    ]
    missing = [p for p in context.firacode_fonts if not p.exists()]
    assert not missing, f"Missing FiraCode fonts: {missing}"


@then("the Info.plist lists the FiraCode fonts for internal builds")
def step_info_plist_lists_fonts(context):
    info_plist = Path("app/Info.plist").read_text(encoding="utf-8")
    for font in context.firacode_fonts:
        assert font.name in info_plist, f"{font.name} not referenced in Info.plist"


@given("the build scripts are present")
def step_build_scripts_present(context):
    context.build_files = [
        Path("meson.build"),
        Path("tools/fakefsify.c"),
    ]
    missing = [p for p in context.build_files if not p.exists()]
    assert not missing, f"Missing build files: {missing}"


@then("the command line tool build instructions should be documented")
def step_build_instructions_documented(context):
    readme = Path("README.md").read_text(encoding="utf-8")
    assert "Build command line tool for testing" in readme
