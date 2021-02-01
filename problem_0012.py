#okivi

input_data = input()
divide_by_three = int(len(input_data) / 3)
result = ""
for i in range(5):
    for j in range(int(len(input_data)) * 4 + 1):
        if i % 2 == 0 and j % 2 == 0 and (j + 1) / 3 == 1:
            if (j + 1) / 3 == 1 and (i + 1) / 3 == 1:
                result += input_data[:1]
                # input_data = input_data[1:]
            else:
                result += "#"
        elif j % 2 == 0 and i % 2 == 0 and i == 2:
            result += "#"
        elif i % 2 != 0  and j % 2 != 0:
            result += "#"
        else:
            result += "."
    print(result)
    result = ""
