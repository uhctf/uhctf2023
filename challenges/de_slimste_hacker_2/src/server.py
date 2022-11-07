import socket
import os
import sys
from _thread import *
from threading import *
import time
import json
import random

import binascii
from Crypto.Cipher import AES
from Crypto.Util import Counter
from Crypto.Util import strxor

FLAG = os.environ['FLAG']

ServerSideSocket = socket.socket()
host = '0.0.0.0'
port = int(sys.argv[1])
# port = 2001

try:
    ServerSideSocket.bind((host, port))
except socket.error as e:
    print(str(e))

print('Socket is listening..')
ServerSideSocket.listen(5)

# 1 second should be enough, but made dynamic with the environment variable just in case
threshold = int(os.environ['THRESHOLD'])

question_dict = {}
# Opening JSON file
with open('questions.json') as json_file:
    question_dict = json.load(json_file)

# Retrieve the questions, so we can hussle this list later on
questions = question_dict.keys()

def multi_threaded_client(connection, addr):
    # Setup
    random.seed()

    key = os.urandom(16)
    iv = int(binascii.hexlify(os.urandom(16)), 16)

    cipher = AES.new(key, AES.MODE_CTR, counter = Counter.new(128, initial_value=iv))

    # Randomize questions, keep original intact
    connection_questions = random.sample(questions, len(questions))
    t = time.time_ns()
    wrong_answers = 0

    intro = "Wait, what? Another round?! Wow, that's so not cool. I would've imagined that the final round would be the final round. But, as I said before: your opponent has taken this personal. Some say that he’s a CTR experiment that went wrong, and that he only speaks exclusive, or plain-text. And that he likes to be answered in the same language. And that he uses 16 bytes to shift. All we know is he’s not the Stig, but he is the Stig’s Cryptographic Cousin."
    # Convert string to bytes
    intro_bytes = str.encode(intro)
    # Encrypt the bytes
    intro_cipher = cipher.encrypt(intro_bytes)

    # Get the original keystream
    keystream = strxor.strxor(intro_cipher, intro_bytes)
    shift_counter = 0

    # Send intro
    connection.sendall(intro_cipher)

    # Wait for some input, we don't really care what it is
    data = connection.recv(2048)

    for question in connection_questions:
        # Prepare cipher
        iv += 1
        cipher = AES.new(key, AES.MODE_CTR, counter = Counter.new(128, initial_value=iv))

        # Update shift_counter to get the keystream to decypher the answer
        shift_counter += 1 

        # Ask the single question encrypted
        # Convert string to bytes
        question_bytes = str.encode(question + " (" + str(len(question_dict[question]["answer"])) + ")")
        encrypted_question = cipher.encrypt(question_bytes)
        connection.sendall(encrypted_question)

        # Get a response
        data = connection.recv(2048)

        # Try to decode the answer
        try:
            # Get the keystream for this question
            question_keystream = keystream[(shift_counter * 16):][:len(data)]

            response = strxor.strxor(data, question_keystream[:len(data)]).decode('utf-8')

            # Process response
            if (response.lower() != question_dict[question]["answer"].lower()):
                wrong_answers += 1
        except:
            # Decoding went wrong, answer must be invalid
            wrong_answers += 1
    
    # Prepare cipher
    iv += 1
    cipher = AES.new(key, AES.MODE_CTR, counter = Counter.new(128, initial_value=iv))

    if (wrong_answers < 1) and time.time_ns()-t < threshold:
        connection.sendall(cipher.encrypt(str.encode("Wow, you are amazing! Here is the flag:\n" + FLAG + "\n")))
    elif wrong_answers < 1:
        connection.sendall(cipher.encrypt(str.encode("You are really good at this... but some say your opponent is faster\n")))
    else:
        connection.sendall(cipher.encrypt(str.encode("Mistakes were made... " + str(wrong_answers) + " actually\n")))
    connection.close()

def main():
    ThreadCount = 0
    while True:
        Client, address = ServerSideSocket.accept()
        print('Connected to: ' + address[0] + ':' + str(address[1]))
        t = Thread(target = multi_threaded_client, args = (Client, address) )
        t.start()
        print(time.thread_time_ns())
        ThreadCount += 1
        print('Thread Number: ' + str(ThreadCount))
    ServerSideSocket.close()

if __name__ == '__main__':
	main()