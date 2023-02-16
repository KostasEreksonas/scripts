#!/usr/bin/env python3

addition = 0
count = 0
values = open("input.txt")
value_array = []

for val in values:
    value_array.append(val)

addition_array = []
for i in range(len(value_array)):
    addition = int(value_array[i]) + int(value_array[i-1]) + int(value_array[i-2])
    addition_array.append(addition)

for i in range(len(addition_array)):
    if addition_array[i] > addition_array[i-1]:
        count += 1
print(f"The result is: {count}")
values.close()
