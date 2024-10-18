def main():
    t = int(input())
    for _ in range(t):
        n, k = map(int, input().split())
        a = list(map(int, input().split()))

        a.sort()
        ans = 0
        b = a[:k-1]
        for i in b:
            ans += i
            ans += i - 1
        print(ans)

if __name__ == '__main__':
    main()
