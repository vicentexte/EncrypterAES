import binascii

from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad

from hashmdfive import hash_string


def desencriptar(texto_encriptado: str, llave: str, iv: str) -> str:
    """
    Decrypt the content of texto_encriptado

    Parameters
    ---
    texto_encriptado: str
        encrypt message
    llave: str
        key
    iv: str
        initalizer vector

    Returns
    ---
    str
        decrypted message
    """

    if len(llave) not in [16, 24, 32]:
        llave = hash_string(llave)
    else:
        llave = llave.encode("utf-8")

    iv = iv.encode("utf-8")
    texto_encriptado_bytes = binascii.unhexlify(texto_encriptado)
    cipher = AES.new(llave, AES.MODE_CBC, iv)
    texto_desencriptado_padded = cipher.decrypt(texto_encriptado_bytes)
    texto_desencriptado = unpad(texto_desencriptado_padded, AES.block_size)

    return texto_desencriptado.decode("utf-8")


if __name__ == "__main__":
    iv = "1234567890abcdef"  # 16 bytes

    print("Ingresa un mensaje para desencriptar: ")
    texto = input()
    print("Ingresa la clave: ")
    llave = input()
    print("Mensaje desencriptado: " + desencriptar(texto, llave, iv))
