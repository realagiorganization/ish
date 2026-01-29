Feature: Core iSH workflows
  As a developer or tester
  I want core assets and configuration in place
  So the iSH app can be built and exercised

  Scenario: Terminal assets are bundled
    Given the terminal web assets are present
    Then the terminal UI assets should be readable

  Scenario: Internal builds expose FiraCode fonts
    Given the FiraCode font files are bundled
    Then the Info.plist lists the FiraCode fonts for internal builds

  Scenario: CLI build scaffolding exists
    Given the build scripts are present
    Then the command line tool build instructions should be documented
