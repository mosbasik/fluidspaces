#!/usr/bin/env python3

import json
import subprocess
import argparse


class Workspace(object):

    def __init__(self, workspace_dict):
        self.i3_num = workspace_dict['num']
        self.i3_name = workspace_dict['name']

    def __repr__(self):
        return 'Workspace({})'.format({
            'num': self.i3_num,
            'name': self.i3_name,
        })

    @property
    def plain_name(self):
        try:
            return self.i3_name.split(':', 1)[1].strip()
        except IndexError:
            return self.i3_name.strip()

    def set_number(self, number):
        subprocess.run(
            [
                'i3-msg',
                'rename workspace',
                '"{}"'.format(self.i3_name),
                'to',
                '"{}: {}"'.format(number, self.plain_name)
            ],
            stdout=subprocess.PIPE
        )


class Workspaces(object):

    def __init__(self):
        # ask i3 for information about the current workspaces
        self.workspaces = self._i3_get_workspaces()
        # ensure every workspace is numbered and the numbering has no gaps
        self._fix_up()

    @property
    def plain_names(self):
        '''Return list of workspace names without numbers'''
        return [wp.plain_name for wp in self.workspaces]

    def _fix_up(self):
        for new_num, workspace in enumerate(self.workspaces, 1):
            if new_num != workspace.i3_num:
                workspace.set_number(new_num)
        self.workspaces = self._i3_get_workspaces()

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

    def print(self, msg=None):
        if msg is not None:
            print(msg)
        for wp in self.workspaces:
            print(wp)

    def promote_workspace(self, workspace):
        '''Move specified workspace to the front of the list'''
        self.workspaces.remove(workspace)
        self.workspaces.insert(0, workspace)
        self._fix_up()


def choose_workspace(workspaces):
    '''Prompt user to choose a workspace name via a Rofi menu'''
    proc = subprocess.Popen(
        ['rofi', '-dmenu', '-p', 'Select workspace: '],
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE,
    )
    choices_str = '\n'.join(workspaces.plain_names).encode('utf-8')
    chosen_str = proc.communicate(choices_str)[0].decode('utf-8').strip()
    if chosen_str != '':
        match = next((wp for wp in workspaces.workspaces if wp.plain_name == chosen_str), None)
        return match if match is not None else chosen_str
    else:
        return None


def go_to(workspace):
    '''Go to a specifed workspace'''
    try:
        # Workspace object was passed (ie this workspace already exists)
        subprocess.Popen(['i3-msg', 'workspace', workspace.i3_name],
                         stdout=subprocess.PIPE)
    except AttributeError:
        # string was passed (ie this workspace didn't exist and will be createe)
        subprocess.Popen(['i3-msg', 'workspace', workspace],
                         stdout=subprocess.PIPE)


def send_to(workspace):
    '''Send the currently focused window/container to a specified workspace'''
    try:
        # Workspace object was passed (ie this workspace already exists)
        subprocess.Popen(['i3-msg', 'move container to workspace', workspace.i3_name],
                         stdout=subprocess.PIPE)
    except AttributeError:
        # string was passed (ie this workspace didn't exist and will be createe)
        subprocess.Popen(['i3-msg', 'move container to workspace', workspace],
                         stdout=subprocess.PIPE)


def combine_name(number, name):
    '''Return string combining an ordering number and a plain workspace name'''
    return '{}:{}'.format(number, name)


def main():
    # set up command line argument parsing
    parser = argparse.ArgumentParser()
    parser.add_argument('--go-to', action='store_true')
    parser.add_argument('--send-to', action='store_true')
    parser.add_argument('--most-recent', action='store_true')

    # parse the passed command line arguments
    args = parser.parse_args()

    # define behavior based on command line arguments
    if args.go_to or args.send_to:
        workspaces = Workspaces()
        chosen_workspace = choose_workspace(workspaces)
        if chosen_workspace is None:
            return
        if args.send_to:
            send_to(chosen_workspace)
        if args.go_to:
            go_to(chosen_workspace)
            workspaces.promote_workspace(chosen_workspace)


if __name__ == '__main__':
    main()
