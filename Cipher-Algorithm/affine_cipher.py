import lib

def affine_enc(p: str, b: int):
    # Pre Porcessing

    # Plain teks hanya alfabet tanpa angka, spasi, dan tanda baca
    p = lib.removePunctuation(p)
    p = lib.removeNumber(p)
    p = lib.removeSpace(p)