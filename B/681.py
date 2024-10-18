n = int(input())

house = 1234567
car = 123456
computer = 1234

for a in range(n // house + 1):
    left_coins = n - a * house

    for b in range(left_coins // car + 1):
        c = left_coins - b * car

        if c % computer == 0:
            print("YES")
            exit()

print("NO")


