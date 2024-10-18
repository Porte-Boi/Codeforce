n = int(input())
k = list(map(int, input().split()))

best_rating = k[0]
worst_rating = k[0]
amazing_performances = 0

for i in range(1, n):
    if k[i] > best_rating:
        amazing_performances += 1
        best_rating = k[i]
    elif k[i] < worst_rating:
        amazing_performances += 1
        worst_rating = k[i]

print(amazing_performances)

