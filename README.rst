Fluidspaces
===========

- Create i3_ workspaces with custom names on the fly
- Type a few letters to jump to a target workspace using fuzzy matching
- Quick toggle between the two most recently used workspaces
- Bring/send containers to workspaces while doing any of the above


Installation
------------

Requirements
^^^^^^^^^^^^

:i3_:
  Required for fluidspaces to be useful

  - Arch: ``sudo pacman -S i3``
  - Ubuntu: refer to the `i3 repository docs`_


:rofi_:
  Used to get user input via pop-up menu

  - Arch: ``sudo pacman -S rofi``
  - Ubuntu: ``sudo apt install rofi``


Installing Fluidspaces
^^^^^^^^^^^^^^^^^^^^^^

From PyPi
"""""""""

::

  pip install fluidspaces

From Source
"""""""""""

::

  git clone https://github.com/mosbasik/fluidspaces.git
  cd fluidspaces
  pip install .


Argument Reference
------------------

-h, --help      show this help message and exit
-b, --bring-to  bring focused container with you to workspace
-s, --send-to   send focused container away to workspace
-t, --toggle    skip menu prompt & choose workspace 2 (useful for "Alt-Tab" behavior)
-V, --version   show program's version number and exit


Example i3 configuration
------------------------

::

  bindsym $mod+c            exec fluidspaces
  bindsym $mod+Shift+c      exec fluidspaces --send-to
  bindsym $mod+Ctrl+Shift+c exec fluidspaces --bring-to

  bindsym $mod+Tab          exec fluidspaces --toggle
  bindsym $mod+Shift+Tab    exec fluidspaces --toggle --send-to


.. _i3: https://i3wm.org/
.. _i3 repository docs: https://i3wm.org/docs/repositories.html
.. _rofi: https://github.com/DaveDavenport/rofi