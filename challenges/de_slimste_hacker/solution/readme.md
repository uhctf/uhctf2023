# Solution
<!-- optionally include any relevant solution files in this folder -->
This challenge is a combination of a learning experience (e.g. learning interesting facts), and programming with sockets.

The setup of the challenge is fairly simple: there are 10 questions (which do never change) with for every question 3 multiple choice answers (which do also never change). So, after running once, the contestants can gather the answers to the questions. However, there's a catch. The order of the questions varies on every connection. Additionally, the answers also get shuffled. Oh, and in order to beat *The Stig*, the entire quiz should be performed within a second.

A solution can be found in `solution.py`. The contestants need to compile a dictionary with the question and answer. In this example, the original question file was reused. Send back the correct letter (`a`, `b` or `c`) and after 10 questions, you'll get the flag.