def get_fractions(a_b: str, c_b: str) -> str:
    """
    Add your code here
    """
    """
    >> > a_b = '1/3'
    >> > c_b = '5/3'
    >> > get_fractions(a_b, c_b)
    '1/3 + 5/3 = 6/3'
    """
    x=[]
    y=[]
    for a in a_b.split('/'):
        x.append(int(a))
    for a in c_b.split('/'):
        y.append(int(a))

    return f'{a_b} + {c_b} = {x[0]+y[0]}/{x[1]}'

#print(get_fractions('1/3','5/3'))

if __name__ == '__main__':
    assert get_fractions('1/3','5/3') == '1/3 + 5/3 = 6/3'
    assert get_fractions('7/3','-1/3') == '7/3 + -1/3 = 6/3'
    assert get_fractions('1/3','1/3') == '1/3 + 1/3 = 2/3'
    assert get_fractions('15/5','99/5') == '15/5 + 99/5 = 114/5'
    assert get_fractions('1/99','1/99') == '1/99 + 1/99 = 2/99'
