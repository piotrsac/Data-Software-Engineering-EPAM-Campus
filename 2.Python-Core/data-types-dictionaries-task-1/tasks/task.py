from typing import Dict


def get_dict(s: str) -> Dict[str, int]:
    dictionary = {}
    s=s.lower()
    for i in s:
        if i not in dictionary.keys():
            dictionary[i] = 1
        else:
            dictionary[i] += 1

    return dictionary


if __name__ == '__main__':
    # print(get_dict('Oh, it is python'))
    assert get_dict('Oh, it is python')=={" ": 3, ",": 1, "h": 2, "i": 2, "n": 1, "o": 2, "p": 1, "s": 1, "t": 2, "y": 1}
