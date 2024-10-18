t = int(input())

for _ in range(t):
    x = list(map(int,input().strip().split()))
    a = sorted(x)
    if len(a) == 3:
        ans = (a[-1] - a[0])
        print(ans)


