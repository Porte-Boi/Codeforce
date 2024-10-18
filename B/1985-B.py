def maximum_multiple_sum(n):
    if n == 3:
        return 3
    else:
        return 2

if __name__ == "__main__":
    t = int(input())
    results = []
    for _ in range(t):
        n = int(input())
        results.append(maximum_multiple_sum(n))

    for result in results:
            print(result)
