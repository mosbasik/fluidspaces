import pytest

from fluidspaces import Workspace


@pytest.fixture(
    scope='module',
    params=[
        {'num': 1, 'name': '1:config'},
        {'num': 1, 'name': '1 : config'},
        {'num': 1, 'name': '1: config'},
        {'num': 1, 'name': '1 :config'},
    ],
)
def input_wp(request):
    return Workspace(request.param)


def test_join_i3_name():
    assert Workspace.join_i3_name(1, 'config') == '1:config'

def test_split_i3_name(input_wp):
    assert Workspace.split_i3_name(input_wp.i3_name) == (1, 'config')

def test_plain_name(input_wp):
    assert input_wp.plain_name == 'config'
