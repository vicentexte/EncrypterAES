import binascii

from Crypto.Cipher import AES
from Crypto.Util.Padding import pad

from hashmdfive import hash_string


def encriptar(texto: str, llave: str, iv: str) -> str:
    """
    Encrypt the content of texto

    Parameters
    ---
    texto: str
        message
    llave: str
        key
    iv: str
        initalizer vector

    Returns
    ---
    str
        encrypted message
    """

    if len(llave) not in [16, 24, 32]:
        llave = hash_string(llave)
    else:
        llave = llave.encode("utf-8")

    iv = iv.encode("utf-8")
    texto_bytes = texto.encode("utf-8")
    cipher = AES.new(llave, AES.MODE_CBC, iv)
    texto_padded = pad(texto_bytes, AES.block_size)
    texto_encriptado = cipher.encrypt(texto_padded)

    return binascii.hexlify(texto_encriptado).decode("utf-8")


if __name__ == "__main__":
    iv = "1234567890abcdef"  # 16 bytes

    print("Ingresa un mensaje para encriptar: ")
    texto = input()
    print("Ingresa una llave: ")
    llave = input()
    print("Mensaje encriptado: " + encriptar(texto, llave, iv))
