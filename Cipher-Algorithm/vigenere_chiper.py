import lib

def vigenere_standard_encrypt(plaintext: str, key: str):
    """ Vigenere Standard Encrypt """
    
    plaintext = vigenere_preprocess(plaintext)
    key = generate_vigenere_key(plaintext, key)

    chiper = []
    for i in range(len(plaintext)):
        c = (lib.alphabet_to_number(plaintext[i]) + lib.alphabet_to_number(key[i])) % 26
        c = chr(c + 97)
        chiper.append(c)
    
    return "".join(chiper).upper()

def vigenere_standard_decrypt(chiper: str, key: str):
    """ Vigenere Standard Decrypt """
    
    chiper = vigenere_preprocess(chiper)
    key = generate_vigenere_key(chiper, key)
    
    plaintext = []
    for i in range(len(chiper)):
        p = (lib.alphabet_to_number(chiper[i]) - lib.alphabet_to_number(key[i])) % 26
        p = chr(p + 97)
        plaintext.append(p)
        
    return "".join(plaintext)

def generate_vigenere_key(plaintext: str, key: str):
    """ Generate key with length of plaintext """
    
    while len(key) < len(plaintext):
        key += key

    return key[:len(plaintext)]

def vigenere_preprocess(text: str):
    """ Clean text from number, punctuation, and space """ 
    
    text = lib.remove_punctuation(text)
    text = lib.remove_number(text)
    text = lib.remove_space(text)

    return text
