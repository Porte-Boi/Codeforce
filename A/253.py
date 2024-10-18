b, g = map(int, input().split())

res = []


while b > 0 and g > 0:
    res.append("B")
    b -= 1
    res.append("G")
    g -= 1


while b > 0:
    res.append("B")
    b -= 1


while g > 0:
    res.append("G")
    g -= 1

print("".join(res))
