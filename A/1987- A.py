t = int(input())
results = []
for _ in range(t):
    n, k = map(int, input().strip().split())
    if k == 1:
        results.append(n)
    elif n == 1:
        results.append(1)
    else:
        equation = n * k - (k - 1)
        results.append(equation)

for result in results:
    print(result)