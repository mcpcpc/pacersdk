"""
Handles one-time password (OTP) generation.
"""

from base64 import b32decode
from hmac import new
from struct import pack, unpack
from time import time


def hotp(key: str, counter: int, digits: int = 6):
    """
    Generate a HMAC-based one-time password (HOTP) token.

    :param key: Base32 encoded secret.
    :param counter: Number of 30s intervals since epoch.
    :param digits: Number of digits in the OTP.
    :return: Generated HOTP token.
    """
    key = b32decode(key.upper() + "=" * ((8 - len(key)) % 8))
    counter = pack(">Q", counter)
    mac = new(key, counter, "sha1").digest()
    offset = mac[-1] & 0x0F
    binary = unpack(">L", mac[offset : offset + 4])[0] & 0x7FFFFFFF
    return str(binary)[-digits:].zfill(digits)


def totp(key: str, time_step: int = 30, digits: int = 6):
    """
    Generate a time-based one-time password (TOTP) token.

    :param key: Base32 encoded secret.
    :param time_step: Time step in seconds.
    :param digits: Number of digits in the OTP.
    :return: Generated TOTP token.
    """
    counter = int(time() / time_step)
    return hotp(key, counter, digits)
