def solve ():
    s = input()
    t = input()

    m = 0
    len_s = len(s)
    len_t = len(t)

    for i in range(1, min(len_s, len_t) + 1):
        if s[:i] == t[:i]:
            m = i
        
    print(len_s + len_t - max(m, 1) + 1)
    return
    
def main():
    n = int(input())
    for _ in range(n):
        solve()

if __name__ == "__main__":
    main()