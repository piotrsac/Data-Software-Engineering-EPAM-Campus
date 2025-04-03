from typing import List

def split(data: str, sep=' ', maxsplit=-1) -> List[str]:
    '''
    My custom str.split() function
    :param data: string
    :param sep: separator
    :param maxsplit: maximum number of elements in str.split, if -1 then no limit
    :return: list of strings splitted by separator
    '''
    if sep==' ':
        data=data.strip()
    working_data=data
    if len(data) == 0 and sep == ' ': #weird edge cases, that's how str.split() works
        return []
    if len(data) == 0:
        return ['']
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
                if maxsplit == 0:
                    break
                result.append(working_data[last_split:i])
                last_split = i + len(sep)
                i += len(sep) - 1
                maxsplit-=1
                continue

    result.append(working_data[last_split:])
    return result

if __name__ == '__main__':
    assert split('') == [],print(split(''))
    assert split('') == ''.split()
    assert split('',sep=',') == ''.split(',')
    assert split(' ', sep=',') == ' '.split(','),print(' '.split(','))
    assert split('',sep=',') == ''.split(sep=','),print(''.split(sep=','))
    assert split('123  123   123 123') == '123  123   123 123'.split(),print(split('123  123   123 123'))
    assert split(',123,', sep=',') == ['', '123', ''],print(split(',123,', sep=','))
    assert split('test') == ['test'],print(split('test'))
    assert split('Python    2     3', maxsplit=1) == ['Python', '2     3'],print(split('Python    2     3',maxsplit=1))
    assert split('    test     6    7', maxsplit=1) == ['test', '6    7'],print(split('    test     6    7', maxsplit=1))
    assert split('    Hi     8    9', maxsplit=0) == ['Hi     8    9'],print(split('Hi     8    9',maxsplit=0))
    assert split(';;;;sp;;;;t;;;;;;;;;;',sep=';') == ';;;;sp;;;;t;;;;;;;;;;'.split(sep=';')
    assert split('    set   3     4') == ['set', '3', '4'],print(split('    set   3     4'))
    assert split('set;:23', sep=';:') == ['set','23'], print(split('set;:23', sep=';:'))
    assert split('set;:;;:;23', sep=';:;') == 'set;:;;:;23'.split(sep=';:;'), print(split('set;:;;:;23', sep=';:;'))
    assert split('set;:;23', sep=';:;') == ['set', '23'], print(split('set;:;;:;23', sep=';:;'))
    assert split(';;;;;;;;;;set;;;;;;;23;;;;;;;;;;;',sep=';') == ';;;;;;;;;;set;;;;;;;23;;;;;;;;;;;'.split(sep=';'),print(';;;;;;;;;;set;;;;;;;23;;;;;;;;;;;'.split(sep=';'))
    assert split('set;:23', sep=';:', maxsplit=0) == ['set;:23'],print(split('set;:23', sep=';:', maxsplit=0))
    assert split('set;:;:23', sep=';:', maxsplit=2) == ['set', '', '23']
