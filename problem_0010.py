input_data = input()
ball = [1,0,0]

for i in input_data:
    if i == "A":
        tmp = ball[0]
        ball[0] = ball[1]
        ball[1] = tmp
    elif i == "B":
        tmp = ball[1]
        ball[1] = ball[2]
        ball[2] = tmp
    elif i == "C":
        tmp = ball[2]
        ball[2] = ball[0]
        ball[0] = tmp
print(int(ball.index(1)) + 1)