import math
def solve():
    l, r = map(int, input().split())

    if r % 2 != 0:
        r -= 1
    ans = int(math.log2(r))
    print(ans)

def main():
    t = int(input())
    for _ in range(t):  
           solve()

if __name__ == "__main__":
    main()