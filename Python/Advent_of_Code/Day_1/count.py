#!/usr/bin/env python3

count = 0
values = open("input.txt")
value_array = []

for val in values:
    value_array.append(val)

for i in range(len(value_array)):
    if value_array[i] > value_array[i-1]:
        count += 1

print(f"The result is: {count}")
values.close()
