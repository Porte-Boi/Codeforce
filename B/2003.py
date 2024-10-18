def solve():
    n = int(input())
    a = list(map(int, input().split()))

    a.sort(reverse=True)

    print(a[(n + 1) // 2 - 1 ] )

if __name__ == "__main__":
    T = int(input())
    for _ in range(T):
        solve()
