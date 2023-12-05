import re

with open("data/day_03.txt") as data_file:
    data = data_file.read().split("\n")

engine_pieces = []

for id, line in enumerate(data):
    if id == 0:
        previous_line = ""
    else:
        previous_line = data[id-1]

    if id == len(data)-1:
        next_line = ""
    else:
        next_line = data[id+1]
    
    symbols_previous = list(re.finditer(r'[+=\-&!\/\*\$\#@%]+', previous_line))
    symbols_current = list(re.finditer(r'[+=\-&!\/\*\$\#@%]+', line))
    symbols_next = list(re.finditer(r'[+=\-&!\/\*\$\#@%]+', next_line))

    numbers = re.finditer(r'\d+', line)
    for num in numbers:
        num_valid = False
        num_start = num.start()
        num_end = num.end()
        for above in symbols_previous: #hyp: the symbols are always lonely, start = end
            if num_start-1 <= above.start() <= num_end:
                num_valid = True
                break
        for below in symbols_next:
            if num_valid == True:
                break
            if num_start-1 <= below.start() <= num_end:
                num_valid = True
                break
        for curr in symbols_current:
            if num_valid:
                break
            if (num_start == curr.end()) or (num_end == curr.start()):
                num_valid = True
        if num_valid:
            engine_pieces.append(int(num.group()))

print(engine_pieces)
print(sum(engine_pieces))