# 3rd course of 'Python for Everybody'
# Course title: Using Python to Access Web Data
# Week 02: Regular Expression (Chapter 11)
# assignment

import re

hand = open("regex_sum_111892.txt")

j = 0
z = 0

for line in hand:
    line = line.rstrip()
    #print(line)
    x = re.findall('[0-9]+', line)
    if len(x) > 0:
        for i in range(len(x)):
            #print(x)
            y = int(x[i])
            z = z + y
            j = j + 1

print("The sum of all values in this file is {0:d}.".format(z))
print("There are {0:d} values in this file.".format(j))
