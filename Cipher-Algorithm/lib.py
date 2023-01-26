import re

def alphabet_to_number(c: str):
    return ord(c.lower()) - 97

def remove_number(s: str):
    return ''.join([i for i in s if not i.isdigit()])

def remove_punctuation(s: str):
    return re.sub(r'[^\w\s]','',s)

def remove_space(s: str):
    return s.replace(" ", "")

def mod_inverse(A: int, M: int):
    for X in range(1, M):
        if (((A % M) * (X % M)) % M == 1):
            return X
    return -1

if __name__=='__main__':
    s = '1 2ab cd4.,"*05  '
    s = remove_punctuation(s)
    s = remove_number(s)
    s = remove_space(s)
    print(s)

