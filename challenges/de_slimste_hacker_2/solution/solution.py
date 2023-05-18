import socket
import json

import binascii
from Crypto.Cipher import AES
from Crypto.Util import Counter
from Crypto.Util import strxor

question_dict = {}
# Opening JSON file
# The idea is that contestants compile a dictionary themselves
# As an example, the original file with questions was used
with open('questions.json') as json_file:
    question_dict = json.load(json_file)

HOST = "35.210.207.112"
PORT = 8001
BUFFER_S = 8192

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect((HOST, PORT))

# The plain text can be found from the challenge description
# This is similar to the first challenge
intro_plain = "Wait, what? Another round?! Wow, that's so not cool. I would've imagined that the final round would be the final round. But, as I said before: your opponent has taken this personal. Some say that he’s a CTR experiment that went wrong, and that he only speaks exclusive, or plain-text. And that he likes to be answered in the same language. And that he uses 16 bytes to shift. All we know is he’s not the Stig, but he is the Stig’s Cryptographic Cousin."
intro_bytes = str.encode(intro_plain)

# Receive encrypted intro
intro_encrypted = sock.recv(BUFFER_S)

# Find keystream
keystream = strxor.strxor(intro_encrypted, intro_bytes)

# Send <Enter>
# Doesn´t need to be encrypted, the server will answer no matter what input was given
sock.sendall("\n".encode("utf-8"))

# Receive questions, 10 times
for i in range(10):
    # Receive data, but don't decode it this time as we need the bytes
    data = sock.recv(BUFFER_S)
    # This is the encrypted data we can decrypt using our bytes
    bytes_counter = (i + 1) * 16
    question_keystream = keystream[bytes_counter:][:len(data)]
    question_plain = strxor.strxor(data, question_keystream)
    question_decoded = question_plain.decode("utf-8")

    # print(question_decoded)

    # Prepare answer
    answer_bytes = str.encode(question_dict[question_decoded]["answer"])
    answer_keystream = keystream[bytes_counter:][:len(answer_bytes)]
    answer_encrypted = strxor.strxor(answer_bytes, answer_keystream)

    sock.sendall(answer_encrypted)

# Receive the outcome of the game... flag or a disappointing message
# Receive data, but don't decode it this time as we need the bytes
data = sock.recv(BUFFER_S)
# This is the encrypted data we can decrypt using our bytes
bytes_counter = 11 * 16 # 11 as we got 10 questions + 1, 16 bytes as we always shift 16 bytes
message_keystream = keystream[bytes_counter:][:len(data)]
message_plain = strxor.strxor(data, message_keystream)

print(message_plain.decode("utf-8"))