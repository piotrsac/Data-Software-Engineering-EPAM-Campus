from typing import Dict

def combine_dicts(*args:Dict[str, int]) -> Dict[str, int]:
    result = {}
    for arg in args:
        for key, value in arg.items():
            if key not in result.keys():
                result[key] = value
            else:
                result[key] += value
    return result


if __name__ == '__main__':
    dict_1 = {'a': 100, 'b': 200}
    dict_2 = {'a': 200, 'c': 300}
    dict_3 = {'a': 300, 'd': 100}
    assert combine_dicts(dict_1,dict_2) == {'a': 300, 'b': 200, 'c': 300}
    assert combine_dicts(dict_1,dict_2,dict_3) == {'a': 600, 'b': 200, 'c': 300, 'd': 100}

