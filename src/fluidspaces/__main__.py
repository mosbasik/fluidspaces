'''Navigator for i3wm "named containers".

Create i3 workspaces with custom names on the fly, navigate between them based
on their their name or position, and move containers between them.
'''

import argparse

from fluidspaces import i3Commands, RofiCommands, Workspaces, __version__


def main(args=None):

    # set up command line argument parsing
    parser = argparse.ArgumentParser(description=__doc__)
    send_actions = parser.add_mutually_exclusive_group(required=False)
    send_actions.add_argument('-b', '--bring-to',
                              action='store_true',
                              help='bring focused container with you to workspace')
    send_actions.add_argument('-s', '--send-to',
                              action='store_true',
                              help='send focused container away to workspace')
    parser.add_argument('-t', '--toggle',
                        action='store_true',
                        help='skip menu prompt & choose workspace 2 (useful for "Alt-Tab" behavior)')
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

    # if the toggle flag was passed, just get the second workspace
    if args.toggle:
        chosen_plain_name = '2:'

    # but if the toggle flag wasn't passed, start setting up the menu
    else:

        # choose menu prompt to show user
        if args.bring_to:
            prompt = 'Bring container to workspace: '
        elif args.send_to:
            prompt = 'Send container to workspace: '
        else:
            prompt = 'Go to workspace: '

        # prompt user to to choose a workspace
        chosen_plain_name = RofiCommands.menu(wps.choices_str, prompt=prompt)

        # exit program if the user didn't choose a workspace
        if chosen_plain_name is None:
            return

    # find out if a workspace containing chosen_plain_name already existed
    chosen_wp = wps.get_wp(chosen_plain_name)
    if chosen_wp is None:
        chosen_wp_is_new = True
        chosen_i3_name = chosen_plain_name
    else:
        chosen_wp_is_new = False
        chosen_i3_name = chosen_wp.i3_name

    # SEND TO CASE
    if args.send_to:
        i3Commands.send_to_wp(chosen_i3_name)

    # BRING TO CASE
    elif args.bring_to:
        i3Commands.send_to_wp(chosen_i3_name)
        i3Commands.go_to_wp(chosen_i3_name)
        if chosen_wp_is_new:
            wps.import_wps(i3Commands.get_wps_str())
        wps.promote_wp(chosen_i3_name)
        wps.export_wps()

    # GO TO CASE
    else:
        i3Commands.go_to_wp(chosen_i3_name)
        if chosen_wp_is_new:
            wps.import_wps(i3Commands.get_wps_str())
        wps.promote_wp(chosen_i3_name)
        wps.export_wps()


if __name__ == '__main__':
    main()
