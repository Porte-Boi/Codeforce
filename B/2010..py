a, b = map(int, input().split())

if (a == 1 or a == 2) and (b == 1 or b == 2):
    print(3)
elif (a == 1 or a == 3) and (b == 1 or b == 3):
    print(2)
elif (a == 2 or a == 3) and (b == 2 or b == 3):
    print(1)
