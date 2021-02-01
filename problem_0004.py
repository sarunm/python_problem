import re

input_data = input()

upper = re.findall("[A-Z]",input_data)
lower = re.findall("[a-z]",input_data)
mix = re.findall("[A-Z][a-z]",input_data)

if not upper and lower:
    print("All Small Letter")
elif not lower and upper:
    print("All Capital Letter")
else:
    print("Mix")
