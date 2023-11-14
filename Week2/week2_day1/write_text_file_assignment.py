# **Write Text File**: Write a Python program that writes a list of strings to a text file.

# using original test.txt, open a txt file and write a copy of the test.txt file
with open('test.txt','r') as rf:
    with open('test_copy.txt','w') as wf:
        for line in rf:
            wf.write(line)