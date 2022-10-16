# From here is adapted from the keygen binary
from Crypto.Util.Padding import pad, unpad
from Crypto.Cipher import AES
import hashlib


def keygenbin_keygen(arg_8h, arg_ch):  # param1, param2
    # convert strings to arrays of bytes. This is how strings in C actually look like and it allows us to do arithmetic.
    arg_8h = [ord(c) for c in arg_8h]
    arg_ch = [ord(c) for c in arg_ch]

    var_2ch = 0  # i
    # we must create the full result array in python, otherwise it'll complain about "array not long enough". In C we can just write to memory at will (more or less)
    var_25h = [0 for _ in range(0x20)]  # result
    while var_2ch != 0x20:  # 0x00001693: cmp dword [var_2ch], 0x21
        # main block of loop at 0x0000169d
        eax = var_2ch
        eax &= 0xf  # i % 16
        var_30h = eax  # j
        eax = arg_8h
        ecx = var_2ch
        # eax + ecx; param1 string's base ptr + i offset; param1[i]
        # movsx eax, byte [eax + ecx] --> byte means to constrain value to 8 bits --> max int value = 255
        eax = eax[ecx] % 255
        ecx = arg_ch
        edx = var_30h
        # ecx + edx; param2 string's base ptr + j offset; param2[j]
        ecx = ecx[edx] % 255
        eax &= ecx
        ecx = 0xff
        ecx -= var_30h  # 255 - j
        eax ^= ecx
        var_31h = eax % 255  # tmp
        ecx = var_31h
        eax = var_2ch
        var_25h[eax] = ecx  # result[i] = tmp
        eax = var_2ch
        eax += 1
        var_2ch = eax

    return var_25h


def keygenbin_main(encrypted_file_name):
    param1 = encrypted_file_name
    # memset the rest of the C buffer of 32bytes
    param1 = param1 + ((0x20 - len(param1)) * 'x')

    param2 = "owo_secwet_kwey?"

    # convert array of ints back to bytes
    return bytes(keygenbin_keygen(param1, param2))

# From here is adapted from the app.py server file


def app_py_get_aes_key(_password, encrypted_file_name):
    return keygenbin_main(encrypted_file_name)


def app_py_decrypt_file(password, encrypted_file_name):
    decryption_key_bytes = app_py_get_aes_key(password, encrypted_file_name)
    decryption_key = hashlib.sha256(
        decryption_key_bytes).digest()

    with open(f"./{encrypted_file_name}", "rb") as encrypted_file:
        iv_and_cipher_text = encrypted_file.read()
        iv = iv_and_cipher_text[:AES.block_size]
        cipher_text = iv_and_cipher_text[AES.block_size:]

        cipher = AES.new(decryption_key, AES.MODE_CBC, iv)

        print(unpad(cipher.decrypt(cipher_text), AES.block_size))


# our script main
def main():
    app_py_decrypt_file(None, 'the_flag.txt.encrypted')


main()
