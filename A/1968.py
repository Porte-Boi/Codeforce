import math

def main():
    t = int(input())
    results = []
    
    for _ in range(t):
        n = int(input())
    
        mx = -1e9
        ans = 1
        for i in range(1, n):
            k = math.gcd(n, i) + i
            if k >= mx:
                mx = k
                ans = i
            
        print(ans)

if __name__ == '__main__':
    main()
