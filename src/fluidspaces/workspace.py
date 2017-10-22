class Workspace(object):

    def __init__(self, workspace_dict):
        self.i3_num = workspace_dict.get('num', None)
        self.i3_name = workspace_dict.get('name', None)

    def __repr__(self):
        return 'Workspace({})'.format({
            'num': self.i3_num,
            'name': self.i3_name,
        })

    @staticmethod
    def join_i3_name(number, plain_name):
        '''Return an i3_name given a number and a plain_name'''
        return '{}:{}'.format(number, plain_name)

    @property
    def plain_name(self):
        number, plain_name = self.split_i3_name(self.i3_name)
        return plain_name

    @staticmethod
    def split_i3_name(i3_name):
        '''Return a (number, plain_name) tuple given an i3_name'''
        try:
            number, plain_name = i3_name.split(':', 1)
        except ValueError:
            number, plain_name = None, i3_name

        number = int(number) if number is not None else None
        plain_name = plain_name.strip()
        # plain_name = plain_name

        return number, plain_name

