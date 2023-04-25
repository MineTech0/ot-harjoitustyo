import base64
import bcrypt
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.fernet import Fernet


def generate_key_from_password(password):
    salt_string: str = "defaultSalt"
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
    key = generate_key_from_password(password)
    fer = Fernet(key)
    return fer.encrypt(word.encode()).decode()


def decrypt(secret: str, password):
    key = generate_key_from_password(password)
    fer = Fernet(key)
    return fer.decrypt(secret.encode()).decode()


def hash_password(password):
    salt = bcrypt.gensalt()
    return bcrypt.hashpw(password.encode('utf8'), salt)


def check_password(password, hashed_password):
    return bcrypt.checkpw(password.encode('utf8'), hashed_password)
