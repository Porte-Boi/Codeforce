def test_cases():
    s = list(input().strip())
    t = input().strip()

    n = len(s)
    m = len(t)

    j = 0

    for i in range(n):
        if j < m and (s[i] == '?' or s[i] == t[j]):
            s[i] = t[j]
            j += 1

    if j != m:
        return "NO"
    
    s = ['a' if char == '?' else char for char in s]

    return "YES\n" + ''.join(s)
    

def main():
    t = int(input())
    for _ in range(t):
        res = test_cases()
        print(res)


if __name__ == "__main__":
    main()
