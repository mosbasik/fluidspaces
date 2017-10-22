import json

from fluidspaces import i3Commands, Workspace


class Workspaces(object):

    def __init__(self):
        self.workspaces = []  # list of Workspace objects (main state)

    @property
    def choices_str(self):
        '''Return single string representing current list of workspaces'''
        return '\n'.join(self.plain_names).encode('utf-8')

    def export_wps(self):
        old_i3_names, new_i3_names = self.gapless_rename_lists
        i3Commands.rename_wps(old_i3_names, new_i3_names)

    @property
    def gapless_rename_lists(self):
        old_i3_names = []
        new_i3_names = []
        for gapless_num, wp in enumerate(self.workspaces, 1):
            gapless_i3_name = Workspace.join_i3_name(gapless_num, wp.plain_name)
            if gapless_i3_name != wp.i3_name:
                old_i3_names.append(wp.i3_name)
                new_i3_names.append(gapless_i3_name)
        return old_i3_names, new_i3_names

    def get_wp(self, name):
        '''Return first Workspace object in list whose i3_name contains name, or
        None if none of the Workspace objects in the list contain name'''
        return next((wp for wp in self.workspaces if name in wp.i3_name), None)

    def import_wps(self, i3_workspace_str):
        '''Overwrite self's current wps state with i3's current wps state'''
        workspace_dicts = json.loads(i3_workspace_str)
        self.workspaces = [Workspace(wp) for wp in workspace_dicts]

    @property
    def plain_names(self):
        '''Return list of workspace names without numbers'''
        return [wp.plain_name for wp in self.workspaces]

    def promote_wp(self, name):
        '''Move specified workspace to the front of the list'''
        wp = self.get_wp(name)
        self.workspaces.remove(wp)  # remove wp from current position
        self.workspaces.insert(0, wp)  # insert wp at front of list
