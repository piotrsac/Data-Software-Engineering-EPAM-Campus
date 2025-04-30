def check_str(s: str):
    s=s.lower()
    left=0
    right=len(s)-1
    res=True
    while left!=right:
        while not s[left].isalnum():
            left+=1
        while not s[right].isalnum():
            right-=1
        if left==right:
            if s[left]!=s[right]:
                res=False
            break
        if s[left]!=s[right]:
            res=False
            break
        else:
            left+=1
            right-=1

    return res

if __name__ == '__main__':
    assert(check_str('A dog! A panic in a pagoda!')) is True
    assert(check_str('pajak')) is False
    assert(check_str('a dog!')) is False
    assert(check_str('kajak')) is True
    assert(check_str('Do nine men Interpret? Nine men I nod')) is True
