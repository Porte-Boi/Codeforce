def solve():
    a, b, c, d = map(int, input().split())

    ct = 0

    for i in range(min(a, b), max(a, b)):
        if i == c or i == d:
            ct += 1
        
    if ct % 2 == 1:
        return("YES")
    else:
        return("NO")

def main():
    results = []
    t = int(input())
    for _ in range(t):
        results.append(solve())
        
    for result in results:
        print(result)

if __name__ == "__main__":
    main()

    