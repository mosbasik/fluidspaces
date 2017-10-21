#!/usr/bin/env python3

import argparse

from workspaces import Workspaces


def main():
    # set up command line argument parsing
    parser = argparse.ArgumentParser()
    parser.add_argument('--go-to', action='store_true')
    parser.add_argument('--send-to', action='store_true')
    parser.add_argument('--test', action='store_true')

    # parse the passed flags
    args = parser.parse_args()

    if args.test:
        unittest.main()
        # print('tests passed')
        return

    # exit program if both "go_to" and "send_to" flags are absent
    if not args.go_to and not args.send_to:
        return

    # get current state of workspaces
    wps = Workspaces()

    # use flags to determine the workspace-choosing menu prompt
    if args.go_to and args.send_to:
        prompt = 'Bring container to workspace: '
    elif args.go_to:
        prompt = 'Go to workspace: '
    elif args.send_to:
        prompt = 'Send container to workspace: '
    else:
        prompt = 'Choose workspace: '

    # prompt user to to choose a workspace name
    chosen_name = wps.rofi_choose_wp_name(prompt=prompt)

    # exit program if the user didn't choose a workspace
    if chosen_name is None:
        return

    # define behavior
    if args.send_to:
        wps.i3_send_to(chosen_name)

    if args.go_to:
        wps.i3_go_to(chosen_name)

    wps.sync_and_renumber()

    if args.go_to:
        wps.i3_promote(chosen_name)

if __name__ == '__main__':
    main()
