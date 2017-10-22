import subprocess


class i3Commands(object):

    @staticmethod
    def send_to_wp(i3_name):
        '''Send the currently focused window/container to the named workspace'''
        subprocess.Popen(['i3-msg', 'move container to workspace', i3_name], stdout=subprocess.PIPE)

    @staticmethod
    def go_to_wp(i3_name):
        '''Go to the named workspace'''
        subprocess.Popen(['i3-msg', 'workspace', i3_name], stdout=subprocess.PIPE)

    @staticmethod
    def get_wps_str():
        '''Query i3 for current workspaces and return stdout as a string'''
        completed_proc = subprocess.run(['i3-msg', '-t', 'get_workspaces'], stdout=subprocess.PIPE)
        stdout = completed_proc.stdout.decode('utf-8')
        return stdout

    @staticmethod
    def rename_wp(old_i3_name, new_i3_name):
        subprocess.run([
            'i3-msg',
            'rename workspace',
            '"{}"'.format(old_i3_name),
            'to',
            '"{}"'.format(new_i3_name),
        ], stdout=subprocess.PIPE)

    @staticmethod
    def rename_wps(old_i3_names, new_i3_names):
        for old_i3_name, new_i3_name in zip(old_i3_names, new_i3_names):
            i3Commands.rename_wp(old_i3_name, new_i3_name)
