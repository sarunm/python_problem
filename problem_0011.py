#modulo

tmp_data = []

for i in range(10):
    input_data = int(input())
    result = input_data % 42 
    if result not in tmp_data:
        tmp_data.append(result)

print(len(tmp_data))