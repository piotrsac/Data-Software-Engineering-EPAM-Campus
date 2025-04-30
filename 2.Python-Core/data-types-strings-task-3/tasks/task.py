def replacer(s: str) -> str:
    t=''
    for i in range(len(s)):
        if s[i]=='\'':
            t+='\"'
        elif s[i]=='\"':
            t+='\''
        else:
            t+=s[i]
    return t

if __name__ == '__main__':
    assert(replacer('This is my \'Sentence\' where i use \"quotes\"')) == 'This is my \"Sentence\" where i use \'quotes\''
