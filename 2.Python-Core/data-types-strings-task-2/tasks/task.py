def get_longest_word( s: str) -> str:
    """
    >>> get_longest_word('Python is simple and effective!')
    'effective!'
    """
    max_len = -1
    res=''
    for i in s.split():
        if len(i)>max_len:
            max_len = len(i)
            res=i
    return res

if __name__ == '__main__':
    assert(get_longest_word('Python is simple and effective!') == 'effective!')
    assert(get_longest_word('Ala ma kota') == 'kota')
    assert(get_longest_word('Piotrek blablah') == 'Piotrek')
