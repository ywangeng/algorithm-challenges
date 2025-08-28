"""
Question:

Write a function to flatten a nested dictionary. Namespace the keys with a period.

For example, given the following dictionary:

{
    "key": 3,
    "foo": {
        "a": 5,
        "bar": {
            "baz": 8
        }
    }
}
it should become:

{
    "key": 3,
    "foo.a": 5,
    "foo.bar.baz": 8
}
You can assume keys do not contain dots in them, i.e. no clobbering will occur.

"""
from typing import Dict


def solution(d: Dict, parent_key=''):
    sep = '.'
    item = {}

    for k, v in d.items():
        new_key = f'{parent_key}{sep}{k}' if parent_key else k
        if isinstance(v, dict):
            item.update(solution(v, new_key))
        else:
            item[new_key] = v

    return item


nested = {
    "key": 3,
    "foo": {
        "a": 5,
        "bar": {
            "baz": 8
        }
    }
}

print(solution(nested))
