input_data = sorted([int(i) for i in input().split(' ')])
sort_data = str(input())
result_data = []
for item in sort_data:
    if item == "A":
        result_data.append(input_data[0])
    elif item == "B":
        result_data.append(input_data[1])
    elif item == "C":
        result_data.append(input_data[2])
print(" ".join(map(str,result_data)))