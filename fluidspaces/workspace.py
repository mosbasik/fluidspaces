
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
        number, plain_name = self.split_i3_name(self.i3_name)
        return plain_name

    @staticmethod
    def join_i3_name(number, plain_name):
        '''Return an i3_name given a number and a plain_name'''
        return '{}:{}'.format(number, plain_name)

    @staticmethod
    def split_i3_name(i3_name):
        '''Return a (number, plain_name) tuple given an i3_name'''
        try:
            number, plain_name = i3_name.split(':', 1)
        except ValueError:
            number, plain_name = None, i3_name

        number = int(number) if number is not None else None
        plain_name = plain_name.strip()

        return number, plain_name

    def i3_set_number(self, number):
        subprocess.run(
            [
                'i3-msg',
                'rename workspace',
                "{}".format(self.i3_name),
                'to',
                # "'{}: {}'".format(number, self.plain_name),
                self.join_i3_name(number, self.plain_name)
            ],
            stdout=subprocess.PIPE
        )

    def i3_set_i3_name(self, new_i3_name):
        subprocess.run(
            [
                'i3-msg',
                'rename workspace',
                '"{}"'.format(self.i3_name),
                'to',
                '"{}"'.format(new_i3_name),
            ],
            stdout=subprocess.PIPE
        )
