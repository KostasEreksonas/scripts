#!/usr/bin/env python3

f = open("input.txt")
distance = 0
depth = 0
aim = 0

for val in f:
    val_split = val.split()
    if val_split[0] == 'forward':
        distance += int(val_split[1])
        depth += aim*int(val_split[1])
    if val_split[0] == 'down':
        aim += int(val_split[1])
    if val_split[0] == 'up':
        aim -= int(val_split[1])
    #print(val_split[0])
    #print(val_split[1])


result = distance*depth
print("The result is:",result)
#print(directions)
#print(values)

f.close()
