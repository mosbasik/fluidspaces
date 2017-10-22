# Changelog
All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](http://keepachangelog.com/) and this project adheres to [Semantic Versioning](http://semver.org/spec/v2.0.0-rc.2.html).

## [Unreleased]


## [0.1.0] - 2017-10-22
### Added
- This CHANGELOG file, to keep track of changes in this project over time.
- Project URL now included in setup.py information.
- MIT license (from [Choose A License](https://choosealicense.com/licenses/mit/)) now included in `LICENSE` and in setup.py information.
- `-t`/`--toggle` instead of prompting the user for which workspace to use as the target for going/sending/bringing actions, use the first workspace whose title contains `2:` as the target.  Can be used to implement quick toggling between the top two workspaces.


## 0.0.1 - 2017-10-21
### Added
- `fluidspaces` script navigates to the workspace chosen by the user from a list of the current i3 workspaces.
- `-s`/`--send-to` send the currently focused i3 container to the chosen workspace.
- `-b`/`--bring-to` navigate to the chosen workspace and bring the currently focused i3 container to it at the same time.
- Every execution of `fluidspaces` (i.e., with/without flags, user selects workspace / user exits early, etc.) re-numbers all existing i3 workspaces such that the top one is 1, the next is 2, and so on with no gaps.  Existing workspace ordering is maintained.
- Navigating to a workspace with any form of `fluidspaces` "promotes" the chosen workspace to position 1 and renumbers the rest of the workspaces to remove the just-created gap.


[Unreleased]: https://github.com/mosbasik/fluidspaces/compare/0.1.0...HEAD
[0.1.0]: https://github.com/mosbasik/fluidspaces/compare/0.0.1...0.1.0
