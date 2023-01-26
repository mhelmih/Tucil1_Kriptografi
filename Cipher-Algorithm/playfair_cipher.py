import lib

ALFABET = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'k', 'l', 'm',
         'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

################# ENCRYPTION #################
def playfair_encrypt(key: str, plaintext: str):
    """ Fungsi enkripsi menggunakan playfair algorithm"""

    key = lib.remove_punctuation(key)
    key = lib.remove_number(key)
    key = lib.remove_space(key)
    key = lib.to_lower_case(key)

    plaintext = lib.remove_punctuation(plaintext)
    plaintext = lib.remove_number(plaintext)
    plaintext = lib.remove_space(plaintext)
    plaintext = lib.to_lower_case(plaintext)

    key_square = create_key_square(key)
    digraphs = create_digraphs(plaintext)

    alphabet_square_dict = {}
    for letter in ALFABET:
        x,y = search(key_square, letter)
        alphabet_square_dict[letter] = (x,y)
    
    cipher_text = []
    for digraph in digraphs:
        c1 = 0
        c2 = 0
        e1x, e1y = alphabet_square_dict[digraph[0]]
        e2x, e2y = alphabet_square_dict[digraph[1]]
 
        if e1x == e2x:
            c1, c2 = encrypt_row(key_square, e1x, e1y, e2x, e2y)
        elif e1y == e2y:
            c1, c2 = encrypt_column(key_square, e1x, e1y, e2x, e2y)
        else:
            c1, c2 = encrypt_rectangular(key_square, e1x, e1y, e2x, e2y)
 
        cipher = c1 + c2
        cipher_text.append(cipher)
    return "".join(cipher_text).upper()


def search(key_square : list, letter: str):
    """ Mencari posisi huruf di matrix key """
    for i in range(5):
        for j in range(5):
            if(key_square[i][j] == letter):
                return i, j
 
 
def encrypt_row(key_square : list, e1x: int, e1y: int, e2x: int, e2y: int):
    """ Mengaplikasikan rule enkripsi untuk karakter digraph sebaris"""
    char1 = ''
    if e1y == 4:
        char1 = key_square[e1x][0]
    else:
        char1 = key_square[e1x][e1y+1]
 
    char2 = ''
    if e2y == 4:
        char2 = key_square[e2x][0]
    else:
        char2 = key_square[e2x][e2y+1]
 
    return char1, char2
 
 
def encrypt_column(key_square :list, e1x, e1y, e2x, e2y):
    """ Mengaplikasikan rule enkripsi untuk karakter digraph sekolom"""
    char1 = ''
    if e1x == 4:
        char1 = key_square[0][e1y]
    else:
        char1 = key_square[e1x+1][e1y]
 
    char2 = ''
    if e2x == 4:
        char2 = key_square[0][e2y]
    else:
        char2 = key_square[e2x+1][e2y]
 
    return char1, char2
 
 
def encrypt_rectangular(key_square :list, e1x, e1y, e2x, e2y):
    """ Mengaplikasikan rule enkripsi untuk karakter digraph tidak sebaris dan tidak sekolom"""
    char1 = ''
    char1 = key_square[e1x][e2y]
 
    char2 = ''
    char2 = key_square[e2x][e1y]
 
    return char1, char2

def create_digraphs(plaintext:str):
    " Fungsi mengubah plain text menjadi digraph + menggenapkan plaintext"
    text = digest_double_letter(plaintext)
    if not len(text) % 2 == 0:
        text = text + 'x'
    return convert_to_digraph(text)

def convert_to_digraph(text: str):
    """ Membagi text menjadi array of digraph """
    digraph = []
    group = 0
    for i in range(2, len(text), 2):
        digraph.append(text[group:i])
 
        group = i
    digraph.append(text[group:])
    return digraph

def digest_double_letter(text:str):
    """ Plain text dimodifikasi agar mengikuti aturan digraph """
    k = len(text)
    if k % 2 == 0:
        for i in range(0, k, 2):
            if text[i] == text[i+1]:
                new_word = text[0:i+1] + str('x') + text[i+1:]
                new_word = digest_double_letter(new_word)
                break
            else:
                new_word = text
    else:
        for i in range(0, k-1, 2):
            if text[i] == text[i+1]:
                new_word = text[0:i+1] + str('x') + text[i+1:]
                new_word = digest_double_letter(new_word)
                break
            else:
                new_word = text
    return new_word

def create_key_square(key:str):
    """ Membuat matrix alfabet 5x5 untuk kunci enkripsi berdasarkan string key"""
    alfabet_key = []

    for letter in key:
        letter = 'i' if letter == 'j' else letter
        if not letter in alfabet_key:
            alfabet_key.append(letter)
 
    sisa_alfabet = []
    for i in alfabet_key:
        if i not in sisa_alfabet:
            sisa_alfabet.append(i)
    for i in ALFABET:
        if i not in sisa_alfabet:
            sisa_alfabet.append(i)
 
    square = []
    while sisa_alfabet != []:
        square.append(sisa_alfabet[:5])
        sisa_alfabet = sisa_alfabet[5:]
 
    return square

################# DECRYPTION #################
def playfair_decrypt(key: str, cipher_text: str):
    """ Dekripsi cipher teks """
    key = lib.remove_punctuation(key)
    key = lib.remove_number(key)
    key = lib.remove_space(key)
    key = lib.to_lower_case(key)

    cipher_text = lib.remove_punctuation(cipher_text)
    cipher_text = lib.remove_number(cipher_text)
    cipher_text = lib.remove_space(cipher_text)
    cipher_text = lib.to_lower_case(cipher_text)

    key_square = create_key_square(key)
    digraphs = convert_to_digraph(cipher_text)

    alphabet_square_dict = {}
    for letter in ALFABET:
        x,y = search(key_square, letter)
        alphabet_square_dict[letter] = (x,y)
    
    plain_text = []
    for digraph in digraphs:
        c1 = 0
        c2 = 0
        e1x, e1y = alphabet_square_dict[digraph[0]]
        e2x, e2y = alphabet_square_dict[digraph[1]]
 
        if e1x == e2x:
            c1, c2 = decrypt_row(key_square, e1x, e1y, e2x, e2y)
        elif e1y == e2y:
            c1, c2 = decrypt_column(key_square, e1x, e1y, e2x, e2y)
        else:
            c1, c2 = decrypt_rectangular(key_square, e1x, e1y, e2x, e2y)
 
        plain = c1 + c2
        plain_text.append(plain)
    return "".join(plain_text).upper()

def decrypt_row(key_square : list, e1x: int, e1y: int, e2x: int, e2y: int):
    """ Mengaplikasikan rule dekripsi untuk karakter digraph sebaris"""
    char1 = ''
    if e1y == 0:
        char1 = key_square[e1x][4]
    else:
        char1 = key_square[e1x][e1y-1]
 
    char2 = ''
    if e2y == 0:
        char2 = key_square[e2x][4]
    else:
        char2 = key_square[e2x][e2y-1]
 
    return char1, char2
 
 
def decrypt_column(key_square :list, e1x, e1y, e2x, e2y):
    """ Mengaplikasikan rule dekripsi untuk karakter digraph sekolom"""
    char1 = ''
    if e1x == 0:
        char1 = key_square[4][e1y]
    else:
        char1 = key_square[e1x-1][e1y]
 
    char2 = ''
    if e2x == 0:
        char2 = key_square[4][e2y]
    else:
        char2 = key_square[e2x-1][e2y]
 
    return char1, char2
 
 
def decrypt_rectangular(key_square :list, e1x, e1y, e2x, e2y):
    """ Mengaplikasikan rule dekripsi untuk karakter digraph tidak sebaris dan tidak sekolom"""
    char1 = ''
    char1 = key_square[e2x][e1y]
 
    char2 = ''
    char2 = key_square[e1x][e2y]
 
    return char2, char1

if __name__ == '__main__':
    cipher_text = playfair_encrypt("monarchy", "instruments")
    print(cipher_text)
    print(playfair_decrypt("monarchy", cipher_text))
    
    
    
