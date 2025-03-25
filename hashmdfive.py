import hashlib


def hash_string(input_string: str) -> bytes:
    """
    hash input_string with md5

    Parameters
    ---
    input_string: str
        string to hash

    Returns
    ---
    bytes
        hashed string as bytes
    """
    hash_md5 = hashlib.md5(input_string.encode('utf-8')).digest()
    return hash_md5
