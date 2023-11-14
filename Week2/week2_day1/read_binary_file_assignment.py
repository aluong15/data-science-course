# Read Binary File: Write a Python program that reads a binary file and prints its content.

with open('pengu.jpg','rb') as rf:
    with open('pengu_copy.jpg','wb') as wf:
        for line in rf:
            wf.write(line)
