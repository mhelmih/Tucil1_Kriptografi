import re

def alphabetToNumber(c: str):
    return ord(c.lower()) - 97

def removeNumber(s: str):
    return ''.join([i for i in s if not i.isdigit()])

def removePunctuation(s: str):
    return re.sub(r'[^\w\s]','',s)

def removeSpace(s: str):
    return s.replace(" ", "")

def modInverse(A: int, M: int):

    for X in range(1, M):
        if (((A % M) * (X % M)) % M == 1):
            return X
    return -1

if __name__=='__main__':
    s = '1 2ab cd4.,"*05  '
    s = removePunctuation(s)
    s = removeNumber(s)
    s = removeSpace(s)
    print(s)

