#!/bin/python
# a Wordle helper!

class random:
	def __init__(self, seed):
		self.seed = int(seed)

	def float(self):
		self.seed += 1
		x = self.seed * 15485863
		return (x * x * x % 2038074743) / 2038074743

	def int(self, min, max):
		x = self.float()
		return int(min + (x * (max-min+1)))

def get_seed():
	# return list with correctness of guess
	# 0 = bad
	# 1 = wrong place
	# 2 = correct
	return int(http.get("https://wordle.example.org/seed"))

def get_correctness(guess):
	# return list with correctness of guess
	# 0 = bad
	# 1 = wrong place
	# 2 = correct
	# e.g. [0,1,2,0,0]
	return http.post("https://wordle.example.org/?guess={}".format(guess))

seed = get_seed()
if seed < 1624140000 or seed > 2556054000:
	raise Exception("unsupported seed")
r = random(seed)

guesses = []
words = []
correct = []
perfect = [None, None, None, None, None]

with open("words", 'r') as f:
	words = f.readlines()
	
found = False
while not found:
	gi = r.int(0, len(words)-1)
	guess = words[gi][:-1]
	del words[gi]
	can_guess = True
	for c in correct:
		if not c in guess:
			can_guess = False
			break
	if can_guess:
		for i in range(len(perfect)):
			if not perfect[i] == None and not perfect[i] == guess[i]:
				can_guess = False
	
	if not can_guess:
		continue

	guesses.append(guess)
	cv = get_correctness(guess)

	cvs = "".join(map(str, cv))
	cvs = cvs.replace('0', '⬛')
	cvs = cvs.replace('1', '🟨')
	cvs = cvs.replace('2', '🟩')
	print(cvs)

	for i in range(len(guess)):
		if cv[i] > 0 and not guess[i] in correct:
			correct.append(guess[i])

		if cv[i] == 2:
			perfect[i] = guess[i]

	if not None in perfect:
		break

flag = "We guessed {} after {} guesses: {}".format(guesses[-1], len(guesses), ','.join(guesses))
print("uhctf{" + flag + "}")