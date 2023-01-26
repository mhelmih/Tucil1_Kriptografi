import lib

relative_prime_26 = [1, 3, 5, 7, 9, 11, 15, 17, 19, 21, 23, 25]

def affine_encrypt(plaintext: str, pergeseran: int, relatifprima: int):
    """ Enkripsi menggunakan affine cipher"""
    # Pre Porcessing

    # Plain teks hanya alfabet tanpa angka, spasi, dan tanda baca
    plaintext = lib.remove_punctuation(plaintext)
    plaintext = lib.remove_number(plaintext)
    plaintext = lib.remove_space(plaintext)

    letters = lib.split_letter(plaintext)

    cipher_text = list(map(encrypt_single_char,letters,[pergeseran for _ in range(len(letters))],[relatifprima for _ in range(len(letters))]))
    return "".join(cipher_text).upper()

def encrypt_single_char(plainchar:str, pergeseran:int, relatifprima:int):
    """ Enkripsi satu karakter dengan rumus"""
    cipher_char = relatifprima * lib.alphabet_to_number(plainchar) + pergeseran
    # print(f"{m} * {lib.alphabetToNumber(p)} + {b} = {c}", end='')
    cipher_char = cipher_char % 26
    # print(f" = {c} (mod 26)")
    return chr(cipher_char + 97)

def affine_decrypt(ciphertext: str, pergeseran: int, relatifprima: int):
    """ Dekripsi string """

    ciphertext = lib.remove_punctuation(ciphertext)
    ciphertext = lib.remove_number(ciphertext)
    ciphertext = lib.remove_space(ciphertext)

    letters : list = list(ciphertext)

    plain_text = list(map(decrypt_char,letters,[pergeseran for _ in range(len(letters))],[relatifprima for _ in range(len(letters))]))
    
    return "".join(plain_text).upper()


def decrypt_char(cipherchar:str, pergeseran:int, relatifprima:int):
    """ dekripsi satu karakter menggunakan rumus """
    m_inverse = lib.mod_inverse(relatifprima,26)

    plain_char = m_inverse * (lib.alphabet_to_number(cipherchar) - pergeseran)
    plain_char = plain_char % 26
    return lib.number_to_alphabet(plain_char)


if __name__ == '__main__':
    p = 'kripto'
    b = 10
    m = 7
    c = affine_encrypt(p,b,m)
    print(c)
    p = affine_decrypt(c,b,m)
    print(p)