from decrypter import desencriptar
from encrypter import encriptar

llave = "llave_aleatoria_"
texto = "Mensaje de prueba para encriptar y desencriptar"
iv = "anlsdfkjasnlfkjs"


def test_encryption_decryption():
    texto_encriptado = encriptar(texto, llave, iv)
    texto_desencriptado = desencriptar(texto_encriptado, llave, iv)

    assert texto_desencriptado == texto


def test_estatic_encryption():
    assert (
        encriptar("Este es un mensaje secreto", "mi_llave_de_16_b", "1234567890abcdef")
        == "a3bbb70fd91074223627d8b16bac98877183a2f35c5a5c7b080d1714fdbd3f20"
    )


def test_estatic_decryption():
    assert (
        desencriptar(
            "a3bbb70fd91074223627d8b16bac98877183a2f35c5a5c7b080d1714fdbd3f20",
            "mi_llave_de_16_b",
            "1234567890abcdef",
        )
        == "Este es un mensaje secreto"
    )


def test_not_16bytes_key_encryption():
    assert (
        encriptar("Este es un mensaje secreto", "no16", "1234567890abcdef")
        == "417395beaac3c63d3f740ef3cdeea8c559bd73acf0290b206f00443eac58afe1"
    )
