import subprocess


class RofiCommands(object):

    @staticmethod
    def menu(choices_str, prompt='Select workspace: '):
        '''Display Rofi menu of choices and return the one the user picks (or None)'''
        proc = subprocess.Popen(
            ['rofi', '-dmenu', '-p', prompt],
            stdin=subprocess.PIPE,
            stdout=subprocess.PIPE,
        )
        chosen_str = proc.communicate(choices_str)[0].decode('utf-8').strip()
        return chosen_str if chosen_str else None
