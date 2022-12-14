# Solution
<!-- optionally include any relevant solution files in this folder -->
This challenge is a sequal to the challenge `De Slimste Hacker` and is a combination of a learning experience (e.g. learning interesting facts), programming with sockets, and learning about cryptography.

The setup of the challenge is fairly simple: there are 10 questions (which do never change) with fairly easy answers: they can usually be found with just one single search in your favorite search engine. So, after running once, the contestants can gather the answers to the questions. However, everything is encrypted. So first, the encryption needs to be broken.

The description of the challenge is the following:
```
Wait, what? Another round?! Wow, that's so not cool. I would've imagined that the final round would be the final round. But, as I said before: your opponent has taken this personal. Some say that he’s a CTR experiment that went wrong, and that he only speaks exclusive, or plain-text. And that he likes to be answered in the same language. And that he uses 16 bytes to shift. All we know is he’s not the Stig, but he is the Stig’s Cryptographic Cousin.
```
In here, there are a few hints, like `CTR`, `exclusive, or` (exclusive or/XOR), hinting to AES encryption with CTR mode. Additionally, similar to the previous `De Slimste Hacker` challenge, the challenge description is first being sent hinting to a known-plaintext attack.

Using these keywords, it is possible to find the next CTF Writeup:
https://ctftime.org/writeup/26871
The same principle can be used to solve this challenge. 

Additionally, the description hints to using 16 bytes to shift. This is similar to the previously mentioned writeup. The used keystream always gets shifted 16 bytes to create the next key. As the known-plaintext is large enough, the keystream is enough to encrypt (and decrypt) all questions and answers. Also mentioned in the description, `he likes to be answered in the same language`, hints to encrypting the answer. The keystream used to decrypt the question can be reused to encrypt the answer.

A solution can be found in `solution.py`. The contestants need to compile a dictionary with the question and answer. Send back the answer (the expected length of the answer is provided in the question) and after 10 questions, you'll get the flag.