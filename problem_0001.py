keep_point = int(input())
middle_point = int(input())
final_point = int(input())

total_point = keep_point + middle_point + final_point

if total_point >= 80 and total_point <= 100:
    print("A")
elif total_point >= 75:
    print("B+")
elif total_point >= 70:
    print("B")
elif total_point >= 65:
    print("C+")
elif total_point >= 60:
    print("C")
elif total_point >= 55:
    print("D+")
elif total_point >= 50:
    print("D")
else: 
    print("F")

