import base64
import bcrypt
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.fernet import Fernet


def generate_key_from_password(password):
    """
    Generates a key from a password to use for encryption/decryption.


    Args:
        password (_type_): _description_

    Returns:
        _type_: _description_
    """
    salt_string: str = "secret salt"
    salt = bytes(salt_string, "utf-8")
    password = bytes(password, "utf-8")
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=salt,
        iterations=480000,
    )

    return base64.urlsafe_b64encode(kdf.derive(password))


def encrypt(word, password) -> str:
    """
    Encrypt a word with a password. 
    The password is used to generate a key. 
    The key is used to encrypt the word.

    Args:
        word (str): A word to encrypt
        password (str): A password to generate a key from

    Returns:
        str: The encrypted word
    """
    key = generate_key_from_password(password)
    fer = Fernet(key)
    return fer.encrypt(word.encode()).decode()


def decrypt(secret: str, password):
    """
    Decrypt a secret with a password. 
    The password is used to generate a key. 
    The key is used to decrypt the secret.

    Args:
        secret (str): A secret to decrypt
        password (str): A password to generate a key from

    Returns:
        str: decrypted secret
    """
    key = generate_key_from_password(password)
    fer = Fernet(key)
    return fer.decrypt(secret.encode()).decode()


def hash_password(password: str):
    """
    Generates a salt and hashes the password with the salt.

    Args:
        password (str): A password to hash

    Returns:
        str: The hashed password
    """
    salt = bcrypt.gensalt()
    return bcrypt.hashpw(password.encode('utf8'), salt)


def check_password(password: str, hashed_password: bytes) -> bool:
    """
    Checks if the password matches the hashed password.

    Args:
        password (str): A password to check
        hashed_password (str): A hashed password to check against

    Returns:
        bool: True if the password matches the hashed password, False otherwise
    """
    return bcrypt.checkpw(password.encode('utf8'), hashed_password)
