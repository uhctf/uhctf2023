from flask import Flask, render_template, request, send_file, abort
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address

from subprocess import Popen, PIPE
import io

import hashlib
# install Crypto with: `pip install PyCryptoDome`
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad

app = Flask(__name__, static_folder='static')
limiter = Limiter(app, key_func=get_remote_address)


def get_aes_key(password, encrypted_file_name):
    # `shell=False` prevents command injection
    process = Popen(['../keygen/keygen', password,
                    encrypted_file_name], stdout=PIPE, shell=False)
    stdout, _ = process.communicate()

    if process.returncode == 0:
        return stdout
    else:
        raise RuntimeError(stdout)


def decrypt_file(password, encrypted_file_name):
    decryption_key_bytes = bytes(get_aes_key(password, encrypted_file_name))
    decryption_key = hashlib.sha256(
        decryption_key_bytes).digest()

    # flask routing should prevent any path traversal
    with open(f"./uploads/{encrypted_file_name}", "rb") as encrypted_file:
        iv_and_cipher_text = encrypted_file.read()
        iv = iv_and_cipher_text[:AES.block_size]
        cipher_text = iv_and_cipher_text[AES.block_size:]

        cipher = AES.new(decryption_key, AES.MODE_CBC, iv)

        return unpad(cipher.decrypt(cipher_text), AES.block_size)


@app.route('/', methods=['GET'])
def index():
    return render_template('index.html', replace_rule='', input_text='', output_text='')


@app.route('/uploads/<file_name>', methods=['GET'])
# Prevent password brute-forcing by rate limiting the amount of requests per time unit.
@limiter.limit("10/minute")
def download_file(file_name):
    # GET parameters
    decrypt = request.values.get('decrypt') in ['True', 'true']
    password = request.values.get('password') or ''

    try:
        if decrypt:
            decrypted_file = decrypt_file(password, file_name)
            file_name = file_name.replace('.encrypted', '')  # remove extension
            return send_file(io.BytesIO(decrypted_file), as_attachment=True, download_name=file_name)
        else:
            return send_file(f"./uploads/{file_name}", as_attachment=True)

    except FileNotFoundError:
        return abort(404)
    except RuntimeError as e:
        print(f"> ERROR: {e.args[0].decode()}")
        return abort(403)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80)
