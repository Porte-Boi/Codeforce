def main():
    n, k = map(int, input().split())
    s = list(map(int, input().split()))
    res = float('-inf')

    for i in range(n):
        res = max(res, s[i])

    for i in range(n - k):
        res = max(res, s[i] + s[2 * (n - k) - 1 - i])
    
    print(res)

if __name__ == '__main__':
    main()