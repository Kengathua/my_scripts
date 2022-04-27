import time
from .dict_within_list_vs_ordered_dict import dict_within_list, ordered_dict
from collections import OrderedDict

def test_dict_within_list():
    start_time = time.time()
    keys = ['A', 'B', 'C', 'D']
    values = {'A':10, 'B':20, 'C':30, 'D':40}
    error = {'Error': 'Found an error'}
    data = dict_within_list(keys, values, err=error)
    time_spent = time.time()- start_time
    assert data == [{'A':10, 'B':20, 'C':30, 'D':40, 'Error': 'Found an error'}]
    # import pdb
    # pdb.set_trace()

def test_ordered_dict():
    start_time = time.time()
    keys = ['A', 'B', 'C', 'D']
    values = {'A':10, 'B':20, 'C':30, 'D':40}
    error = {'Error': 'Found an error'}
    data = dict_within_list(keys, values, err=error)
    data = ordered_dict(keys, values, err=error)
    time_spent = time.time()- start_time
    assert data == OrderedDict([('A', 10), ('B', 20), ('C', 30), ('Error', 'Found an error')])
    # import pdb
    # pdb.set_trace()
