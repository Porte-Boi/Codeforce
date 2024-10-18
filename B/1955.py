def solve():
    n, c, d = map(int, input().split())
    
    b = list(map(int, input().split()))[:n*n]
    b = sorted(b)

    x = []
    y = []

    for i in range(n):
        x.append(b[0] + (i*d))
    
    for i in range(n):
        for j in range(n):
            y.append(x[i] + (j*c))
    
    y = sorted(y)

    if (b == y):
        print("Yes")
    else:
        print("No"
        
    )

def main():
    t = int(input())
    for _ in range(t):
        solve()

if __name__ == "__main__":
    main()