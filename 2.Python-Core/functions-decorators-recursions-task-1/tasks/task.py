from typing import List, Tuple, Union
from functools import reduce


def seq_sum(sequence: Union[List, Tuple]) -> int:
    """
    Add your code here or call it from here   
    """
    result = 0
    if type(sequence) == int:
        return sequence
    for element in sequence:
        if type(element) == int:
            result += element
        else:
            result += seq_sum(element)
    return result

if __name__ == "__main__":

    assert seq_sum([1,2,3,[4,5, (6,7)]]) == 28
