#!/usr/bin/env python3

import unittest

import dynamic_workspaces as dw

class TestWorkspace(unittest.TestCase):

    def setUp(self):
        self.wp_space_around_colon_no = dw.Workspace({'num': 1, 'name': '1:config'})
        self.wp_space_around_colon_yes = dw.Workspace({'num': 1, 'name': '1 : config'})
        self.wp_space_after_colon = dw.Workspace({'num': 1, 'name': '1: config'})
        self.wp_space_before_colon = dw.Workspace({'num': 1, 'name': '1 :config'})


    def test_join_i3_name(self):
        self.assertEqual(dw.Workspace.join_i3_name(1, 'config'), '1:config')


    def test_split_i3_name_space_around_colon_no(self):
        self.assertEqual(self.wp_space_around_colon_no.plain_name, 'config')

    def test_split_i3_name_space_around_colon_yes(self):
        self.assertEqual(self.wp_space_around_colon_yes.plain_name, 'config')

    def test_split_i3_name_space_after_colon(self):
        self.assertEqual(self.wp_space_after_colon.plain_name, 'config')

    def test_split_i3_name_space_before_colon(self):
        self.assertEqual(self.wp_space_before_colon.plain_name, 'config')

# class TestWorkspaces(unittest.TestCase):

#     w1 = dw.Workspace({
#         'num': 1,
#         'name': '1:config',
#     })

#     def test_plain_name(self):
#         self.assertEqual(self.w1.plain_name, 'config')

if __name__ == '__main__':
    unittest.main()
