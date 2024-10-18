def solve():
    n, m = map(int, input().split())  
    
    if (n + m) % 2 == 1 or n < m:
        return "NO"
    else:
        return "Yes"

def main():
    t = int(input())
    results = [solve() for _ in range(t)]
    for result in results:
        print(result)
    
if __name__ == "__main__":
    main()
        