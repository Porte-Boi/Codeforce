def solve():
    n, a, b = map(int, input().split())

    if a > b:
        print(a * n)
        return
    
    k = min(b - a, n)
    r = b - k
    ans = (b * b +  b) // 2 - (r * r + r) // 2

    if k < n:
        ans += (n - k) * a
    
    print(ans)

def main():
    t = int(input().strip())
    for _ in range(t):
        solve()
if __name__ == "__main__":
    main()
    



