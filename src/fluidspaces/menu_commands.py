import subprocess


class MenuCommands(object):

    @staticmethod
    def menu(command, choices_str):
        '''Display menu of choices and return the one the user picks (or None)'''
        proc = subprocess.Popen(command, stdin=subprocess.PIPE, stdout=subprocess.PIPE)
        stdout, stderr = proc.communicate(choices_str)
        chosen_str = stdout.decode('utf-8').strip()
        return chosen_str if chosen_str else None
