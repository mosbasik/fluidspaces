import pkg_resources

from .i3_commands import i3Commands
from .rofi_commands import RofiCommands
from .workspace import Workspace
from .workspaces import Workspaces


try:
    __version__ = pkg_resources.get_distribution(__name__).version
except pkg_resources.DistributionNotFound:
    # package is not installed
    pass
