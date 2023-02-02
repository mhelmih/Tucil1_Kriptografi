import numpy as np
from cipher_algo import lib

def hill_encrypt(plaintext: str, n: int, matrix:list):
    """ Enkripsi teks menggunakan hill cipher """
    # key_matrix = create_key_matrix(n, keyfiller)

    text = fill_plain_text(plaintext, n) if not len(plaintext) % n == 0 else plaintext
    ngraphs = lib.convert_to_ngraph(text, n)

    return encrypt_ngraphs(ngraphs, matrix)

def encrypt_ngraphs(plainngraphs: list, keymatrix: list):
    plainngraphs = list(map(lib.split_letter, plainngraphs))
    np_key = np.array(keymatrix)
    cipher_text = []
    for i in range(len(plainngraphs)):
        el = plainngraphs[i]
        el = list(map(lib.alphabet_to_number, el))
        np_el = np.array(el)
        
        res = np.matmul(np_key,np_el)
        res = np.mod(res, 26)
        res = res.tolist()
        res = list(map(lib.number_to_alphabet,res))

        cipher_text += res
    return "".join(cipher_text).upper()


def fill_plain_text(plaintext:str, n:int):
    """ Menggenapkan panjang plain text dengan menambah beberapa karakter x di belakang"""
    return plaintext + ('x' * (n - (len(plaintext) % n)) )

def create_key_matrix(n: int, keyfiller:list):
    """ Mengubah list of int menjadi key matrix """
    matrix = [[0 for i in range(n)] for i in range(n)]
    
    x = 0
    y = 0
    for char in keyfiller:
        if y == n:
            x += 1
            y = 0
        matrix[x][y] = char
        y += 1
    return matrix

def hill_decrypt(ciphertext:str,n: int, matrix:list):
    # key_matrix = create_key_matrix(n, keyfiller)
    text = fill_plain_text(ciphertext, n) if not len(ciphertext) % n == 0 else ciphertext
    ngraphs = lib.convert_to_ngraph(text, n)
    return decrypt_ngraphs(ngraphs,matrix)

def decrypt_ngraphs(cipher: list, keymatrix: list):
    cipher = list(map(lib.split_letter, cipher))
    inverse_key_matrix = lib.modMatInv(keymatrix,26)
    plain_text = []
    for i in range(len(cipher)):
        el = cipher[i]
        el = list(map(lib.alphabet_to_number, el))
        np_el = np.array(el)
        
        res = np.matmul(inverse_key_matrix,np_el)
        res = np.mod(res, 26)
        res = res.tolist()
        res = list(map(lib.number_to_alphabet,res))

        plain_text += res
    return "".join(plain_text).upper()


if __name__ == '__main__':
    key = create_key_matrix(3,[17,17,5,21,18,21,2,2,19])
    # text = [15,0,24]

    # np_key = np.array(key)
    # np_text = np.array(text)

    # mat = np.matmul(np_key,np_text)
    # print(np.mod(mat,26))

    # print(fill_plain_text("dimasfaidh",3))

    res = hill_encrypt("paymoremoney",3,[17,17,5,21,18,21,2,2,19])
    print(res)

    p = hill_decrypt(res,3,[17,17,5,21,18,21,2,2,19])
    print(p)
    # np_key = np.array(key)
    # print(lib.modMatInv(key,26))

    
    
    
        

        