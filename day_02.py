import re

max_red = 12
max_green = 13
max_blue = 14

with open("data/day_02.txt") as data_file:
    data = data_file.read().split("\n")

# data = data[98:100] # for testing purporses

data_dict = {}
allowed = []

for line in data:
    game_number = int(line[5:8].replace(':', ''))
    red_draws = [int(re.sub(r'[^\d]+', '', str)) for str in re.findall(r"\d{1,2} red", line)]
    blue_draws = [int(re.sub(r'[^\d]+', '', str)) for str in re.findall(r"\d{1,2} blue", line)]
    green_draws = [int(re.sub(r'[^\d]+', '', str)) for str in re.findall(r"\d{1,2} green", line)]

    data_dict[game_number] = {
        "red": red_draws,
        "blue": blue_draws,
        "green": green_draws
    }
    if (max(red_draws) <= max_red) and (max(blue_draws) <= max_blue) and (max(green_draws) <= max_green):
        allowed.append(game_number)

# print(data_dict)
print(allowed)
print(sum(allowed))