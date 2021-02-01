#Seven Dwarves
input_data = []
for i in range(9):
    input_data.append(int(input()))

hundred = 100
result = []

target = sum(input_data) - 100

for i in range(9):
    for j in range(9):
        if target == (input_data[i]+input_data[j]):
            input_data.pop(j)
            input_data.pop(i)
            [print(i) for i in input_data]
            break
    else:
        continue
    break
