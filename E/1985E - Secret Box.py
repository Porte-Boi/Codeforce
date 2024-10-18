def solve(x, y, z, k):
    
    mx = 0

    for a in range(1, x + 1):
        for b in range(1, y + 1):
            if k % (a * b) != 0:
                continue
            c = k // (a * b)
            if c <= z and a * b * c == k:
                ct = (x - a + 1) * (y - b + 1) * (z - c + 1)
                mx = max(ct, mx)
    print(mx)



if __name__ == "__main__":
    TCS = int(input())  
    for _ in range(TCS):       
        x, y, z, k = map(int, input().split())
        solve(x, y, z, k)
    
