n, m = map(int, input().split())
a = list(map(int, input().split()))

a.sort()


neg = []
for i in range(len(a)):
    if a[i] < 0:
        neg.append(a[i])
    if len(neg) == m:
        break

neg = abs(sum(neg))
print(neg)


