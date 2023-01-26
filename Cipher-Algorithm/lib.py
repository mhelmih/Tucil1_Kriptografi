import re
import numpy as np

import math

def modMatInv(A,p):       # Finds the inverse of matrix A mod p
  n=len(A)
  A=np.matrix(A)
  adj=np.zeros(shape=(n,n))
  for i in range(0,n):
    for j in range(0,n):
      adj[i][j]=((-1)**(i+j)*int(round(np.linalg.det(minor(A,j,i)))))%p

  return (np.rint((modInv(int(round(np.linalg.det(A))),p)*adj)%p)).astype(int)
   

def modInv(a,p):          # Finds the inverse of a mod p, if it exists
  for i in range(1,p):
    if (i*a)%p==1:
      return i
  raise ValueError(str(a)+" has no inverse mod "+str(p))

def minor(A,i,j):    # Return matrix A with the ith row and jth column deleted
  A=np.array(A)
  minor=np.zeros(shape=(len(A)-1,len(A)-1))
  p=0
  for s in range(0,len(minor)):
    if p==i:
      p=p+1
    q=0
    for t in range(0,len(minor)):
      if q==j:
        q=q+1
      minor[s][t]=A[p][q]
      q=q+1
    p=p+1
  return minor

def convert_to_ngraph(text: str,n:int):
    """ Membagi text menjadi array of digraph """
    ngraph = []
    group = 0
    for i in range(n, len(text), n):
        ngraph.append(text[group:i])
 
        group = i
    ngraph.append(text[group:])
    return ngraph

def alphabet_to_number(c: str):
    return ord(c.lower()) - 97

def number_to_alphabet(n:int):
    return chr(n + 97)

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

def to_lower_case(text: str):
    return text.lower()

def split_letter(text: str):
    return list(text)

if __name__=='__main__':
    s = '1 2ab cd4.,"*05  '
    s = remove_punctuation(s)
    s = remove_number(s)
    s = remove_space(s)
    print(s)

