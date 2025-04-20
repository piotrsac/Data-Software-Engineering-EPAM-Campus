def get_longest_word( s: str) -> str:
    """
     Add your code here 
    """
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
# print(get_longest_word('Python is simple and effective!'))

if __name__ == '__main__':
    assert(get_longest_word('Python is simple and effective!') == 'effective!')
    assert(get_longest_word('Ala ma kota') == 'kota')
    assert(get_longest_word('Piotrek siusiak') == 'Piotrek')
