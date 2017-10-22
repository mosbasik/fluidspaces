import pytest
import sys

from fluidspaces import Workspace, Workspaces


@pytest.fixture
def input_wps_string():
    return '[{"num":1,"name":"1:foo"}, {"num":-1,"name":"spam"}, {"num":2,"name":"2:bar"}, {"num":-1,"name":"baz"}]'

@pytest.fixture
def input_wps(input_wps_string):
    wps = Workspaces()
    wps.import_wps(input_wps_string)
    return wps

@pytest.fixture(params=[('1', 0),
                        ('foo', 0),
                        ('a', 1),
                        ('spam', 1),
                        ('2', 2),
                        ('ba', 2),
                        ('bar', 2),
                        ('z', 3),
                        ('baz', 3)])
def name_query(request):
    return request.param

@pytest.fixture(params=[[],
                        [Workspace({'num':1,'name':'1:spam'}),
                         Workspace({'num':2,'name':'2:eggs'})]])
def base_wps_list(request):
    return request.param


def test_init():
    wps = Workspaces()
    assert wps.workspaces == []

def test_choices_str(input_wps):
    assert input_wps.choices_str == 'foo\nspam\nbar\nbaz'.encode('utf-8')

def test_gapless_rename_lists(input_wps):
    assert input_wps.gapless_rename_lists == (
        ['spam', '2:bar', 'baz'],  # old i3_names
        ['2:spam', '3:bar', '4:baz'],  # new i3_names
    )

def test_get_wp(input_wps, name_query):
    query, expected_index = name_query
    query_result = input_wps.get_wp(query)
    expected_result = input_wps.workspaces[expected_index]
    assert query_result == expected_result

def test_import_wps(base_wps_list, input_wps_string):
    wps = Workspaces()
    wps.workspaces = base_wps_list
    wps.import_wps(input_wps_string)
    result_list = [(wp.i3_num, wp.i3_name) for wp in wps.workspaces]
    expected_list = [(1, '1:foo'),
                     (-1, 'spam'),
                     (2, '2:bar'),
                     (-1, 'baz')]
    assert result_list == expected_list

def test_plain_names(input_wps):
    assert input_wps.plain_names == ['foo', 'spam', 'bar', 'baz']

def test_promote_wp(input_wps):
    input_wps.promote_wp('bar')
    assert input_wps.plain_names == ['bar', 'foo', 'spam', 'baz']
