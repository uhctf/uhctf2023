#!/bin/env/python

inpt_file = None
with open("input.png", "br") as inpt:
    inpt_file = inpt.read()
cropped_file = None
with open("cropped.png", "br") as cropped:
    cropped_file = cropped.read()

with open("output.png", "bw") as outpt:
    outpt.write(cropped_file)
    outpt.write(inpt_file[len(cropped_file):])