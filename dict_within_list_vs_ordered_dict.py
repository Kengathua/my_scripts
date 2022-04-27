"""Test for space and time complexity"""
from collections import OrderedDict


def dict_within_list(keys, values, err=None):
    data = []
    if err:
        values.update(err)
    data.append(values)
    return data


def ordered_dict(keys, values, err=None):
    od = OrderedDict()
    od['A'] = values['A']
    od['B'] = values['B']
    od['C'] = values['C']
    od['Error'] = values['Error']

    return od
