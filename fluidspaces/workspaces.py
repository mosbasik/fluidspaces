import subprocess
import json

from workspace import Workspace

class Workspaces(object):

    def __init__(self):
        self.workspaces = []  # list of Workspace objects (main state)
        self.sync_wps()  # import i3 wps as they are
        self.i3_renumber_wps()  # renumber imported wps if any require it
        self.sync_wps()  # import i3 wps again after renumbering

    @property
    def plain_names(self):
        '''Return list of workspace names without numbers'''
        return [wp.plain_name for wp in self.workspaces]

    def sync_and_renumber(self):
        # get current state of i3 workspaces
        self.workspaces = self._i3_get_workspaces()
        # renumber all i3 workspaces (gapless and monotonically increasing)
        for new_num, workspace in enumerate(self.workspaces, 1):
            if new_num != workspace.i3_num:
                workspace.set_number(new_num)
        # get new state of i3 workspaces
        self.workspaces = self._i3_get_workspaces()

    def sync_wps(self):
        '''Overwrite self's current wps state with i3's current wps state'''
        self.workspaces = self._i3_get_workspaces()

    def get_wp_with_name(self, name):
        '''Return first Workspace object in list whose i3_name contains name, or
        None if none of the Workspace objects in the list contain name'''
        return next((wp for wp in self.workspaces if name in wp.i3_name), None)

    def rofi_choose_wp_name(self, prompt='Select workspace: '):
        '''Prompt user to choose a workspace via a Rofi menu

        Arguments:
            workspaces {Workspaces} -- which workspaces to show in Rofi menu

        Keyword Arguments:
            prompt {str} -- Rofi menu user prompt (default: {'Select workspace: '})

        Returns:
            str -- chosen workspace name (i3_name if the wp exists; otherwise user's typed string)
        '''
        proc = subprocess.Popen(
            ['rofi', '-dmenu', '-p', prompt],
            stdin=subprocess.PIPE,
            stdout=subprocess.PIPE,
        )
        choices_str = '\n'.join(self.plain_names).encode('utf-8')
        chosen_name = proc.communicate(choices_str)[0].decode('utf-8').strip()
        if chosen_name == '':
            return None
        try:
            return self.get_wp_with_name(chosen_name).i3_name
        except AttributeError:
            return chosen_name

    def _i3_get_workspaces(self):
        '''Return list of current Workspace objects'''
        completed_proc = subprocess.run(
            ['i3-msg', '-t', 'get_workspaces'],
            stdout=subprocess.PIPE,
        )
        stdout = completed_proc.stdout.decode('utf-8')
        workspace_dicts = json.loads(stdout)
        workspace_objs = [Workspace(wp) for wp in workspace_dicts]
        return workspace_objs

    def i3_go_to_wp(self, name):
        '''Go to the named workspace'''
        subprocess.Popen(['i3-msg', 'workspace', self.get_wp_with_name(name).i3_name],
                         stdout=subprocess.PIPE)
        self.i3_promote_wp(work)

    def i3_promote_wp(self, name):
        '''Move specified workspace to the front of the list'''
        wp = self.get_wp_with_name(name)
        print('promoting workspace', wp)
        self.workspaces.remove(wp)  # remove wp from current position
        self.workspaces.insert(0, wp)  # insert wp at front of list
        self.sync_and_renumber()  # renumber all wp in list

    def i3_renumber_wps(self):
        '''Renumber all wps in self's state to be gapless & increasing'''
        for gapless_num, wp in enumerate(self.workspaces, 1):
            gapless_i3_name = Workspace.join_i3_name(gapless_num, wp.plain_name)
            if gapless_i3_name != wp.i3_name:
                wp.i3_set_i3_name(gapless_i3_name)

    def i3_send_to_wp(self, name):
        '''Send the currently focused window/container to the named workspace'''
        subprocess.Popen(['i3-msg', 'move container to workspace', self.get_wp_with_name(name).i3_name],
                         stdout=subprocess.PIPE)
