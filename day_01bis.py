import re

with open("data/day_01.txt") as data_file:
    full_input = data_file.read().split("\n")

full_input = [str.replace("one", "o1e") for str in full_input]
full_input = [str.replace("two", "t2o") for str in full_input]
full_input = [str.replace("three", "t3e") for str in full_input]
full_input = [str.replace("four", "f4r") for str in full_input]
full_input = [str.replace("five", "f5e") for str in full_input]
full_input = [str.replace("six", "s6x") for str in full_input]
full_input = [str.replace("seven", "s7n") for str in full_input]
full_input = [str.replace("eight", "e8t") for str in full_input]
full_input = [str.replace("nine", "n9e") for str in full_input]

#print(full_input)

num_inputs = [re.sub(r'[^\d]+', '', str) for str in full_input]
sum_calibration_values = sum([int(str[0]+str[-1]) for str in num_inputs])

print(sum_calibration_values)
