import lib

def vigenere_standard_encrypt(plaintext: str, key: str):
    """ Standard Vigenere Encrypt """
    
    plaintext = vigenere_preprocess(plaintext)
    key = generate_vigenere_standard_key(plaintext, key)

    chiper = []
    for i in range(len(plaintext)):
        c = (lib.alphabet_to_number(plaintext[i]) + lib.alphabet_to_number(key[i])) % 26
        c = chr(c + 97)
        chiper.append(c)
    
    return "".join(chiper).upper()

def vigenere_standard_decrypt(chiper: str, key: str):
    """ Standard Vigenere Decrypt """
    
    chiper = vigenere_preprocess(chiper)
    key = generate_vigenere_standard_key(chiper, key)
    
    plaintext = []
    for i in range(len(chiper)):
        p = (lib.alphabet_to_number(chiper[i]) - lib.alphabet_to_number(key[i])) % 26
        p = chr(p + 97)
        plaintext.append(p)
        
    return "".join(plaintext)

def generate_vigenere_standard_key(plaintext: str, key: str):
    """ Generate key with length of plaintext for Standard Vigenere Chiper"""
    
    while len(key) < len(plaintext):
        key += key

    return key[:len(plaintext)]

def vigenere_autokey_encrypt(plaintext: str, key: str):
    """ Auto-key Vigenere Encrypt """
    
    plaintext = vigenere_preprocess(plaintext)
    key = generate_vigenere_autokey(plaintext, key)
    
    chiper = []
    for i in range(len(plaintext)):
        c = (lib.alphabet_to_number(plaintext[i]) + lib.alphabet_to_number(key[i])) % 26
        c = chr(c + 97)
        chiper.append(c)
    
    return "".join(chiper).upper()

def vigenere_autokey_decrypt(chiper: str, key: str):
    """ Auto-key Vigenere Decrypt """
    
    chiper = vigenere_preprocess(chiper)
    key = generate_vigenere_autokey(chiper, key)
    
    plaintext = []
    for i in range(len(chiper)):
        p = (lib.alphabet_to_number(chiper[i]) - lib.alphabet_to_number(key[i])) % 26
        p = chr(p + 97)
        plaintext.append(p)
        
    return "".join(plaintext)

def generate_vigenere_autokey(plaintext: str, key: str):
    """ Generate key with length of plaintext for Auto-key Vigenere Chiper """
    
    while len(key) < len(plaintext):
        key += plaintext

    return key[:len(plaintext)]

def vigenere_preprocess(text: str):
    """ Clean text from number, punctuation, and space """ 
    
    text = lib.remove_punctuation(text)
    text = lib.remove_number(text)
    text = lib.remove_space(text)

    return text

def vigenere_extended_encrypt(plaintext: bytes, key: bytes):
    """ Extended Vigenere Encrypt """
    
    plaintext = vigenere_preprocess(plaintext)
    key = generate_vigenere_extended_key(plaintext, key)

    chiper = []
    for i in range(len(plaintext)):
        c = (plaintext[i] + key[i]) % 256
        chiper.append(c)
    
    return bytes(chiper)

def vigenere_extended_decrypt(chiper: bytes, key: bytes):
    """ Extended Vigenere Decrypt """
    
    chiper = vigenere_preprocess(chiper)
    key = generate_vigenere_extended_key(chiper, key)
    
    plaintext = []
    for i in range(len(chiper)):
        p = (chiper[i] - key[i]) % 256
        plaintext.append(p)
        
    return bytes(plaintext)

def generate_vigenere_extended_key(plaintext: bytes, key: bytes):
    """ Generate key with length of plaintext for Extended Vigenere Chiper """
    
    while len(key) < len(plaintext):
        key += key

    return key[:len(plaintext)]
