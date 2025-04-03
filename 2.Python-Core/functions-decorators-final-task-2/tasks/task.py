from typing import List

def split_by_index(s: str, indexes: List[int]) -> List[str]:
    """
    Function splitting string by index into list of strings (no elements are lost)
    if 0>int>len(indexes) it ignores them
    """
    indexes.sort()
    result = []
    last_split=-10**9
    for element in indexes:
        if element >= len(s):
            break
        result.append(s[last_split:element])
        last_split=element
    result.append(s[last_split:])
    return result
if __name__ == '__main__':
    assert split_by_index("pythoniscool,isn'tit?", [6, 8, 12, 13, 18]) == ["python", "is", "cool", ",", "isn't", "it?"]
    assert split_by_index("no luck", [42]) == ["no luck"]