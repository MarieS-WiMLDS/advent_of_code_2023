import re

with open("data/day_01.txt") as data_file:
    full_input = data_file.read().split("\n")

num_inputs = [re.sub(r'[^\d]+', '', str) for str in full_input]
sum_calibration_values = sum([int(str[0]+str[-1]) for str in num_inputs])

print(sum_calibration_values)
