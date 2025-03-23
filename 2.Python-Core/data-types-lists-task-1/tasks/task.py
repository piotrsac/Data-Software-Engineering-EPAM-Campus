from typing import List, Tuple

def sort_unique_elements(str_list: Tuple[str, ...]) -> List[str]:
    # TODO: Add your code here
    t=[]
    for element in str_list:
        if element not in t:
            t.append(element)
    t.sort()
    print(t)
    return t

if __name__ == '__main__':
    assert(sort_unique_elements(('red', 'white', 'black', 'red', 'green', 'black')))==['black', 'green', 'red', 'white']

