from cipher_algo import lib

def vigenere_standard_encrypt(plaintext: str, key: str):
    """ Standard Vigenere Encrypt """
    
    plaintext = vigenere_preprocess(plaintext)
    key = generate_vigenere_standard_key(plaintext, key)

    cipher = []
    for i in range(len(plaintext)):
        c = (lib.alphabet_to_number(plaintext[i]) + lib.alphabet_to_number(key[i])) % 26
        c = chr(c + 97)
        cipher.append(c)
    
    return "".join(cipher).upper()

def vigenere_standard_decrypt(cipher: str, key: str):
    """ Standard Vigenere Decrypt """
    
    cipher = vigenere_preprocess(cipher)
    key = generate_vigenere_standard_key(cipher, key)
    
    plaintext = []
    for i in range(len(cipher)):
        p = (lib.alphabet_to_number(cipher[i]) - lib.alphabet_to_number(key[i])) % 26
        p = chr(p + 97)
        plaintext.append(p)
        
    return "".join(plaintext)

def generate_vigenere_standard_key(plaintext: str, key: str):
    """ Generate key with length of plaintext for Standard Vigenere cipher"""
    
    while len(key) < len(plaintext):
        key += key

    return key[:len(plaintext)]

def vigenere_autokey_encrypt(plaintext: str, key: str):
    """ Auto-key Vigenere Encrypt """
    
    plaintext = vigenere_preprocess(plaintext)
    key = generate_vigenere_autokey(plaintext, key)
    
    cipher = []
    for i in range(len(plaintext)):
        c = (lib.alphabet_to_number(plaintext[i]) + lib.alphabet_to_number(key[i])) % 26
        c = chr(c + 97)
        cipher.append(c)
    
    return "".join(cipher).upper()

def vigenere_autokey_decrypt(cipher: str, key: str):
    """ Auto-key Vigenere Decrypt """
    
    cipher = vigenere_preprocess(cipher)
    current_key = key
    
    plaintext = []
    for i in range(len(cipher)):
        p = (lib.alphabet_to_number(cipher[i]) - lib.alphabet_to_number(current_key[i])) % 26
        p = chr(p + 97)
        plaintext.append(p)
        current_key += p
        
    return "".join(plaintext)

def generate_vigenere_autokey(plaintext: str, key: str):
    """ Generate key with length of plaintext for Auto-key Vigenere cipher """
    
    while len(key) < len(plaintext):
        key += plaintext

    return key[:len(plaintext)]

def vigenere_preprocess(text: str):
    """ Clean text from number, punctuation, and space """ 
    
    text = lib.remove_punctuation(text)
    text = lib.remove_number(text)
    text = lib.remove_space(text)
    text = lib.remove_newline(text)

    return text

def vigenere_extended_encrypt(plaintext: int, key: int):
    """ Extended Vigenere Encrypt """
    
    key = generate_vigenere_extended_key(plaintext, key)
    if type(plaintext) != str:
        key = bytes(key, encoding='utf-8')
    
    cipher = []
    for i in range(len(plaintext)):
        c = ''
        if type(plaintext[i]) == str:
            # convert to ascii
            c = int(ord(plaintext[i]) + ord(key[i])) % 256
        else:
            c = int(plaintext[i] + key[i]) % 256
        cipher.append(c)
    
    return bytes(cipher)

def vigenere_extended_decrypt(cipher: bytes, key: bytes):
    """ Extended Vigenere Decrypt """
    
    key = generate_vigenere_extended_key(cipher, key)
    key = bytes(key, encoding='utf-8')
    
    plaintext = []
    for i in range(len(cipher)):
        p = (cipher[i] - key[i]) % 256
        plaintext.append(p)
        
    return bytes(plaintext)

def generate_vigenere_extended_key(plaintext: bytes, key: bytes):
    """ Generate key with length of plaintext for Extended Vigenere cipher """
    
    while len(key) < len(plaintext):
        key += key

    return key[:len(plaintext)]
