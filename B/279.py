n, t = map(int, input().split())
a = list(map(int, input().split()))

sort_a = sorted(a)
ans = 0
for i in range(n):
    if t - sort_a[i] >= 0:
        ans += 1
        t -= sort_a[i]
    else:
        break
print(ans)