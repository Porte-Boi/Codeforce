def solve():
    x, y = list(map(int, input().split()))
    if x > y:
        print(y, x)
    else:
        print(x, y)

def main():
    t = int(input())
    for _ in range(t):
        solve()
if __name__ == "__main__":
    main()
