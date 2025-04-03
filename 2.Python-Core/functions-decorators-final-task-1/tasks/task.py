from typing import List

def split(data: str, sep=' ', maxsplit=-1):
    """
    Add your code here or call it from here   
    """
    num_of_splits = maxsplit
    data=data.strip()
    data_work=data
    if len(data) == 0:
        return []
    if maxsplit == 0:
        return [data.strip()]
    result=[]
    last_split=-10**9
    for i in range(len(data)):
        if data[i] == sep[0]:
            if sep==' ' and last_split == i:
                last_split = i + len(sep)
                i += len(sep) - 1
                continue
            for j in range(len(sep)):
                if data[i + j] != sep[j]:
                    break
            else:
                result.append(data_work[last_split:i])
                last_split = i + len(sep)
                i += len(sep) - 1
                continue

    result.append(data_work[last_split:])
    return result

if __name__ == '__main__':
    assert split('') == [],print(split(''))
    assert split('123  123   123 123') == '123  123   123 123'.split(),print(split('123  123   123 123'))
    assert split(',123,', sep=',') == ['', '123', ''],print(split(',123,', sep=','))
    assert split('test') == ['test'],print(split('test'))
    #assert split('Python    2     3', maxsplit=1) == ['Python', '2     3']
    #assert split('    test     6    7', maxsplit=1) == ['test', '6    7'],print(split('    test     6    7', maxsplit=1))
    assert split('    Hi     8    9', maxsplit=0) == ['Hi     8    9'],print(split('Hi     8    9',maxsplit=0))
    assert split('    set   3     4') == ['set', '3', '4'],print(split('    set   3     4'))
    assert split('set;:23', sep=';:') == ['set','23'], print(split('set;:23', sep=';:'))
    assert split('set;:;;:;23', sep=';:;') == 'set;:;;:;23'.split(sep=';:;'), print(split('set;:;;:;23', sep=';:;'))
    assert split('set;:;23', sep=';:;') == ['set', '23'], print(split('set;:;;:;23', sep=';:;'))
    #assert split('set;:23', sep=';:', maxsplit=0) == ['set;:23'],print(split('set;:23', sep=';:', maxsplit=0))
    #assert split('set;:;:23', sep=';:', maxsplit=2) == ['set', '', '23']
