t = int(input())
res =  []

for _ in range(t):
    n, k = map(int, input().split())
    s = input().strip()

    count = 0
    i = 0
    while i < n:
        if s[i] == "B":
            count += 1
            i += k
        else:
            i +=1

    res.append(count)

for i in res:
    print(i)


