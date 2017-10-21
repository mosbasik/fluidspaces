#!/usr/bin/env python3

import json
import subprocess
import argparse

# version 1: functional

def get_workspace_names_f():
    '''Get sorted list of current i3 workspace names'''
    return sorted([workspace['name'] for workspace in json.loads(
        subprocess.run(['i3-msg', '-t', 'get_workspaces'],
                       stdout=subprocess.PIPE).stdout.decode('utf-8'))])

def choose_workspace_f(workspace_choices):
    '''Prompt user to choose a workspace name via a Rofi menu'''
    return subprocess.Popen(
        ['rofi', '-dmenu', '-p', 'Select workspace: '],
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE,
    ).communicate(
        '\n'.join(workspace_choices).encode('utf-8')
    )[0].decode('utf-8')


# version 2: imperative

def get_workspace_names_i():
    '''Get sorted list of current i3 workspace names'''
    completed_proc = subprocess.run(
        ['i3-msg', '-t', 'get_workspaces'],
        stdout=subprocess.PIPE,
    )
    stdout = completed_proc.stdout.decode('utf-8')
    workspaces = json.loads(stdout)
    workspace_names = [w['name'] for w in workspaces]
    return sorted(workspace_names)

def choose_workspace_i(workspace_choices):
    '''Prompt user to choose a workspace name via a Rofi menu'''
    proc = subprocess.Popen(
        ['rofi', '-dmenu', '-p', 'Select workspace: '],
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE,
    )
    workspace_choices_str = '\n'.join(workspace_choices).encode('utf-8')
    chosen_workspace = proc.communicate(workspace_choices_str)[0].decode('utf-8')
    return chosen_workspace


def go_to(workspace_name):
    '''Go to a specifed workspace'''
    subprocess.Popen(['i3-msg', 'workspace', workspace_name],
                     stdout=subprocess.PIPE)


def send_to(workspace_name):
    '''Send the currently focused window/container to a specified workspace'''
    subprocess.Popen(['i3-msg', 'move container to workspace', workspace_name],
                     stdout=subprocess.PIPE)


if __name__ == '__main__':

    # set up command line argument parsing
    parser = argparse.ArgumentParser()
    parser.add_argument('--go-to', action='store_true')
    parser.add_argument('--send-to', action='store_true')

    # parse the passed command line arguments
    args = parser.parse_args()

    # define behavior based on command line arguments
    if args.go_to or args.send_to:
        # chosen_workspace = choose_workspace_i(get_workspace_names_i())
        chosen_workspace = choose_workspace_f(get_workspace_names_f())
        if args.send_to:
            send_to(chosen_workspace)
        if args.go_to:
            go_to(chosen_workspace)
