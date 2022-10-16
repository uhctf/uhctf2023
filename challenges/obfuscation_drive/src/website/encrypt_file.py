import sys
import os

from subprocess import Popen, PIPE
import io

import hashlib
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from Crypto import Random


def get_aes_key(password, encrypted_file_name):
    # `shell=False` prevents command injection
    process = Popen(['../keygen/keygen', password,
                    encrypted_file_name], stdout=PIPE, shell=False)
    stdout, _ = process.communicate()

    if process.returncode == 0:
        return stdout
    else:
        raise Exception(stdout)


def encrypt_file(password, file_name):
    key_bytes = get_aes_key(password, f"{file_name}.encrypted")
    key = hashlib.sha256(key_bytes).digest()

    plain_text = b''
    file_path = f"./uploads/{file_name}"
    with open(file_path, "rb") as file:
        plain_text = file.read()
    os.remove(file_path)

    with open(f"./uploads/{file_name}.encrypted", "wb") as file:
        padded_plain_text = pad(plain_text, AES.block_size)
        iv = Random.new().read(AES.block_size)

        cipher = AES.new(key, AES.MODE_CBC, iv)

        file.seek(0)
        file.write(iv + cipher.encrypt(padded_plain_text))


if len(sys.argv) != 3:
    print(f"Usage: {sys.argv[0]} password file_name")
    exit(1)
encrypt_file(sys.argv[1], sys.argv[2])
