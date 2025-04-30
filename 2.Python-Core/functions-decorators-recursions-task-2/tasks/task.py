from typing import Any, List

def linear_seq(sequence: List[Any]) -> List[Any]:
    result=[]
    for item in sequence:
        if type(item) == int:
            result.append(item)
        else:
            result += (linear_seq(item))
    return result

if __name__ == '__main__':
    assert linear_seq([1,2,3,[4,5,(6,7)]]) == [1,2,3,4,5,6,7]