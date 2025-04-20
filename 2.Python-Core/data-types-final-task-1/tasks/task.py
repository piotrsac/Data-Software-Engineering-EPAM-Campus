from typing import Any, Dict, List, Set

def check(lst: List[Dict[Any, Any]]) -> Set[Any]:

    result = set()
    for i in lst:
        for j in i.values():
            if j not in result:
                result.add(j)
    return result

"""Input: [{"V":"S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII":"S005"}, {"V":"S009"},{"VIII":"S007"}]
Output: {'S005', 'S002', 'S007', 'S001', 'S009'}"""
if __name__ == '__main__':
    assert((check([{"V":"S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"},
                   {"VII":"S005"}, {"V":"S009"},{"VIII":"S007"}]))
           == {'S005', 'S002', 'S007', 'S001', 'S009'})