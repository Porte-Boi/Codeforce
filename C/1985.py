def solve():
    n = int(input().strip())
    m =list(map(int, input().strip().split()))
    mx = 0
    ct = 0 
    sum = 0

    for i in range(n):
        x = m[i]
        sum += x
        mx = max(x, mx)
        if sum - mx == mx:
            ct += 1
    print(ct)

def main():
    t = int(input().strip())
    for _ in range(t):       
        solve()
    
if __name__ == "__main__":
    main()