Changelog
=========
All notable changes to this project will be documented in this file.

The format is based on `Keep a Changelog`_ and this project adheres to `Semantic Versioning`_.

.. _Keep a Changelog: http://keepachangelog.com/
.. _Semantic Versioning: http://semver.org/spec/v2.0.0-rc.2.html


Unreleased_
-----------
Added
^^^^^
- An actually useful README file

Changed
^^^^^^^
- README and CHANGELOG files now use reStructuredText format instead of Markdown
- Package's long description now includes the contents of CHANGELOG at the end
- All argument descriptions now start with small letters to match ``argparse``'s built-in descriptions for ``--help`` and ``--version``


0.2.2_ - 2017-10-23
--------------------
Fixed
^^^^^
- Crash on startup if not run from an intact git repository (i.e. if run using a sdist build, a github archive, a pypi archive, or literally anything but a dev evironment)


0.2.1_ - 2017-10-22
--------------------
Fixed
^^^^^
- Navigating to / bringing a container to a new workspace promotes that workspace (the new workspace used to stay at the back where it was created - with a numberless name - until it was navigated to again)


0.2.0_ - 2017-10-22
--------------------
Added
^^^^^
- ``-V``/``--version`` flag prints program version and exits


Changed
^^^^^^^
- Now using ``setuptools_scm`` to get the package version from git tags instead of keeping a ``VERSION`` file


0.1.0_ - 2017-10-22
--------------------
Added
^^^^^
- This CHANGELOG file, to keep track of changes in this project over time.
- Project URL now included in setup.py information.
- MIT license (from `Choose a License`_) now included in ``LICENSE`` and in setup.py information.
- ``-t``/``--toggle`` instead of prompting the user for which workspace to use as the target for going/sending/bringing actions, use the first workspace whose title contains ``2:`` as the target.  Can be used to implement quick toggling between the top two workspaces.

.. _Choose a License: https://choosealicense.com/licenses/mit/

0.0.1 - 2017-10-21
--------------------
Added
^^^^^
- ``fluidspaces`` script navigates to the workspace chosen by the user from a list of the current i3 workspaces.
- ``-s``/``--send-to`` send the currently focused i3 container to the chosen workspace.
- ``-b``/``--bring-to`` navigate to the chosen workspace and bring the currently focused i3 container to it at the same time.
- Every execution of ``fluidspaces`` (i.e., with/without flags, user selects workspace / user exits early, etc.) re-numbers all existing i3 workspaces such that the top one is 1, the next is 2, and so on with no gaps.  Existing workspace ordering is maintained.
- Navigating to a workspace with any form of ``fluidspaces`` "promotes" the chosen workspace to position 1 and renumbers the rest of the workspaces to remove the just-created gap.


.. _0.1.0: https://github.com/mosbasik/fluidspaces/compare/0.0.1...0.1.0
.. _0.2.0: https://github.com/mosbasik/fluidspaces/compare/0.1.0...0.2.0
.. _0.2.1: https://github.com/mosbasik/fluidspaces/compare/0.2.0...0.2.1
.. _0.2.2: https://github.com/mosbasik/fluidspaces/compare/0.2.1...0.2.2
.. _Unreleased: https://github.com/mosbasik/fluidspaces/compare/0.2.2...HEAD
