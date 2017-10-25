Fluidspaces
===========

- Create i3_ workspaces with custom names on the fly
- Type a few letters to jump to a target workspace using fuzzy matching
- Quick toggle between the two most recently used workspaces
- Bring/send containers to workspaces while doing any of the above

Dependencies
------------

i3_
^^^

You need this installed for ``fluidspaces`` to be useful, of course. ::

  pacman -S i3  # to install on Arch

Refer to the `i3 repository docs`_ to install on Ubuntu.

rofi_ (optional)
^^^^^^^^^^^^^^^^

Can be used as a replacement for ``dmenu``.  Has a nicer looking menu, displays different prompts for different actions, etc.  Not required for ``fluidspaces`` to function. ::

  sudo pacman -S rofi  # to install on Arch
  sudo apt install rofi  # to install on Ubuntu

Installing Fluidspaces
----------------------

From PyPi::

  pip install fluidspaces

From source::

  git clone https://github.com/mosbasik/fluidspaces.git
  cd fluidspaces
  pip install .

Argument Reference
------------------

-h, --help                  show this help message and exit
-b, --bring-to              bring focused container with you to workspace
-s, --send-to               send focused container away to workspace
-m PROGRAM, --menu=PROGRAM  program to render the menu {dmenu,rofi} (default: dmenu)
-t, --toggle                skip menu & choose workspace 2 (default: False)
-V, --version               show program's version number and exit

Example i3 configurations
-------------------------

Using defaults::

  bindsym $mod+c            exec fluidspaces
  bindsym $mod+Shift+c      exec fluidspaces --send-to
  bindsym $mod+Ctrl+Shift+c exec fluidspaces --bring-to

  bindsym $mod+Tab          exec fluidspaces --toggle
  bindsym $mod+Shift+Tab    exec fluidspaces --toggle --send-to

Using ``rofi`` instead of ``dmenu``::

  bindsym $mod+c            exec fluidspaces --menu=rofi
  bindsym $mod+Shift+c      exec fluidspaces --menu=rofi --send-to
  bindsym $mod+Ctrl+Shift+c exec fluidspaces --menu=rofi --bring-to

  # note that toggling bypasses the menu entirely, so no need to define it
  bindsym $mod+Tab          exec fluidspaces --toggle
  bindsym $mod+Shift+Tab    exec fluidspaces --toggle --send-to

.. _i3: https://i3wm.org/
.. _i3 repository docs: https://i3wm.org/docs/repositories.html
.. _rofi: https://github.com/DaveDavenport/rofi
