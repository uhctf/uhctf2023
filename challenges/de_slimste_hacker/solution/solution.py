import socket
import json

question_dict = {}
# Opening JSON file
# The idea is that contestants compile a dictionary themselves
# As an example, the original file with questions was used
with open('questions.json') as json_file:
    question_dict = json.load(json_file)

HOST = "0.0.0.0"
PORT = 8000
BUFFER_S = 8192

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect((HOST, PORT))

# Receive initial intro
data = sock.recv(BUFFER_S).decode("utf-8")
print(data)

# Send <Enter>
sock.sendall("\n".encode("utf-8"))

# Receive questions, 10 times
for i in range(10):
    data = sock.recv(BUFFER_S).decode("utf-8")

    print(data)

    # Process data
    splitted = data.split("\n")
    # Question = splitted[0], a) = splitted[1], b) = splitted[2], c) = splitted[3]

    # Find the correct answer from your dict and send the response
    if question_dict[splitted[0]]["answer"] in splitted[1]:
        # Send answer
        sock.sendall("a\n".encode("utf-8"))
    elif question_dict[splitted[0]]["answer"] in splitted[2]:
        # Send answer
        sock.sendall("b\n".encode("utf-8"))
    elif question_dict[splitted[0]]["answer"] in splitted[3]:
        # Send answer
        sock.sendall("c\n".encode("utf-8"))
    else:
        # Didn´t find it, something must've gone wrong. Send something anyway
        sock.sendall("a\n".encode("utf-8"))   

# Receive the outcome of the game... flag or a disappointing message
data = sock.recv(BUFFER_S).decode("utf-8")
print(data)