'''Navigator for i3wm "named containers".

Create i3 workspaces with custom names on the fly, navigate between them based
on their their name or position, and move containers between them.
'''

import argparse
import sys

from fluidspaces import i3Commands, MenuCommands, Workspaces, __version__


def main(args=None):

    # set up command line argument parsing
    parser = argparse.ArgumentParser(description=__doc__)

    # define what "action" to perform (bring to, send to, or go to)
    parser.set_defaults(action='go_to')
    send_actions = parser.add_mutually_exclusive_group(required=False)
    send_actions.add_argument('-b', '--bring-to',
                              dest='action',
                              action='store_const',
                              const='bring_to',
                              help='bring focused container with you to workspace')
    send_actions.add_argument('-s', '--send-to',
                              dest='action',
                              action='store_const',
                              const='send_to',
                              help='send focused container away to workspace')

    # define what "menu" to render (dmenu, rofi)
    parser.add_argument('-m', '--menu',
                        choices=['dmenu', 'rofi'],
                        default='dmenu',
                        help='program used to render the menu (default: %(default)s)')

    # define whether to simply target the second window or not
    parser.add_argument('-t', '--toggle',
                        action='store_true',
                        help='skip menu & choose workspace 2 (default: %(default)s)')

    # define how to show the program version
    parser.add_argument('-V', '--version',
                        action='version',
                        version=__version__)

    # parse the passed flags
    args = parser.parse_args()

    # get current state of workspaces
    wps = Workspaces()  # create workspaces object
    wps.import_wps(i3Commands.get_wps_str())  # import current wps
    wps.export_wps()  # normalize wps numbers and export
    wps.import_wps(i3Commands.get_wps_str())  # import normalized wps

    # if the toggle flag was passed, the target is the second workspace
    if args.toggle:
        chosen_plain_name = '2:'

    # otherwise we need to get the target from the user via a menu
    else:

        # define menu prompts used for various actions
        prompts = {
            'go_to': 'Go to workspace: ',
            'send_to': 'Send container to workspace: ',
            'bring_to': 'Bring container to workspace: ',
        }

        # define various menu generating commands (lists for subprocess.Popen)
        menus = {
            'dmenu': ['dmenu'],
            'rofi': ['rofi', '-dmenu', '-p', prompts[args.action]],
        }

        # prompt user to to choose a workspace
        chosen_plain_name = MenuCommands.menu(menus[args.menu], wps.choices_str)

        # exit program without error if the user didn't choose a workspace
        if chosen_plain_name is None:
            sys.exit(0)

    # find out if a workspace containing chosen_plain_name already existed
    chosen_wp = wps.get_wp(chosen_plain_name)
    if chosen_wp is None:
        chosen_wp_is_new = True
        chosen_i3_name = chosen_plain_name
    else:
        chosen_wp_is_new = False
        chosen_i3_name = chosen_wp.i3_name

    # SEND TO CASE
    if args.action == 'send_to':
        i3Commands.send_to_wp(chosen_i3_name)

    # BRING TO CASE
    elif args.action == 'bring_to':
        i3Commands.send_to_wp(chosen_i3_name)
        i3Commands.go_to_wp(chosen_i3_name)
        if chosen_wp_is_new:
            wps.import_wps(i3Commands.get_wps_str())
        wps.promote_wp(chosen_i3_name)
        wps.export_wps()

    # GO TO CASE
    elif args.action == 'go_to':
        i3Commands.go_to_wp(chosen_i3_name)
        if chosen_wp_is_new:
            wps.import_wps(i3Commands.get_wps_str())
        wps.promote_wp(chosen_i3_name)
        wps.export_wps()


if __name__ == '__main__':
    main()
