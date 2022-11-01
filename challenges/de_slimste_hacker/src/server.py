import socket
import os
import sys
from _thread import *
from threading import *
import time
import json
import random

FLAG = os.environ['FLAG']

ServerSideSocket = socket.socket()
host = '0.0.0.0'
port = int(sys.argv[1])
# port = 2000

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
    # Randomize questions, keep original intact
    connection_questions = random.sample(questions, len(questions))
    t = time.time_ns()
    all_correct = True

    # Send intro
    connection.sendall(str.encode("""Wow, you made it to the final round!
Think about all the fame you'd get if you win this one.
However, your opponent has taken this personal.
Some say he never blinks, and that he roams around the woods at night foraging for wolves.
And that he's scared of Belgians. Or was it bells?
Anyway, all we know is he’s called the Stig.
Press <Enter> to continue\n"""))

    # Wait for some input, we don't really care what it is
    data = connection.recv(2048)

    for question in connection_questions:
        possible_answers = random.sample(question_dict[question]["possible_answers"], len(question_dict[question]["possible_answers"]))
        # Ask the multiple choice question
        connection.sendall(str.encode(question + "\na) " + possible_answers[0] + "\nb) " + possible_answers[1] + "\nc) " + possible_answers[2] + "\n"))
        # Get a response
        data = connection.recv(2048)
        response = data.decode('utf-8').strip("\n")
        # Process response
        if (possible_answers[0] == question_dict[question]["answer"]) and (response != "a"):
            all_correct = False
        elif (possible_answers[1] == question_dict[question]["answer"]) and (response != "b"):
            all_correct = False
        elif (possible_answers[2] == question_dict[question]["answer"]) and (response != "c"):
            all_correct = False

    if all_correct and time.time_ns()-t < threshold:
        connection.sendall(str.encode("Wow, you are amazing! Here is the flag:\n" + FLAG + "\n"))
    elif all_correct:
        connection.sendall(str.encode("You are really good at this... but some say your opponent is faster\n"))
    else:
        connection.sendall(str.encode("Mistakes were made...\n"))
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