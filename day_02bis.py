import re

max_red = 12
max_green = 13
max_blue = 14

with open("data/day_02.txt") as data_file:
    data = data_file.read().split("\n")

# data = data[98:100] # for testing purporses

data_dict = {}
powers = []

for line in data:
    red_draws = [int(re.sub(r'[^\d]+', '', str)) for str in re.findall(r"\d{1,2} red", line)]
    blue_draws = [int(re.sub(r'[^\d]+', '', str)) for str in re.findall(r"\d{1,2} blue", line)]
    green_draws = [int(re.sub(r'[^\d]+', '', str)) for str in re.findall(r"\d{1,2} green", line)]

    powers.append(max(red_draws) * max(blue_draws) * max(green_draws))

print(powers)
print(sum(powers))