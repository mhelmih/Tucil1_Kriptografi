import lib

relative_prime_26 = [1, 3, 5, 7, 9, 11, 15, 17, 19, 21, 23, 25]

def affine_enc(p: str, b: int, m: int):
    # Pre Porcessing

    # Plain teks hanya alfabet tanpa angka, spasi, dan tanda baca
    p = lib.removePunctuation(p)
    p = lib.removeNumber(p)
    p = lib.removeSpace(p)

    letters : list = list(p)

    c = list(map(enc_char,letters,[b for _ in range(len(letters))],[m for _ in range(len(letters))]))
    return "".join(c)

def enc_char(p:str, b:int, m:int):
    c = m * lib.alphabetToNumber(p) + b
    # print(f"{m} * {lib.alphabetToNumber(p)} + {b} = {c}", end='')
    c = c % 26
    # print(f" = {c} (mod 26)")
    return chr(c + 97)

def affine_dec(c: str, b: int, m: int):

    c = lib.removePunctuation(c)
    c = lib.removeNumber(c)
    c = lib.removeSpace(c)

    letters : list = list(c)

    p = list(map(dec_char,letters,[b for _ in range(len(letters))],[m for _ in range(len(letters))]))
    
    return "".join(p)


def dec_char(c:str, b:int, m:int):
    m_inverse = lib.modInverse(m,26)

    p = m_inverse * (lib.alphabetToNumber(c) - b)
    p = p % 26
    return chr(p + 97)


if __name__ == '__main__':
    p = 'kripto'
    b = 10
    m = 7
    c = affine_enc(p,b,m)
    print(c)
    p = affine_dec(c,b,m)
    print(p)