def solve():
    n = int(input())
    
    a = []
    b = []
    
    has_odd_even_pair = False
    
    for _ in range(n):
        x, y = map(int, input().split())
        a.append(x)
        b.append(y)
        
        if n == 1 and (x % 2 != y % 2):
            print(-1)
            return

        if (x % 2 != y % 2):
            has_odd_even_pair = True

    sum_a = sum(a)
    sum_b = sum(b)

    # Both sums are even
    if sum_a % 2 == 0 and sum_b % 2 == 0:
        print(0)
    # Both sums are odd and there's at least one odd-even pair
    elif sum_a % 2 == 1 and sum_b % 2 == 1 and has_odd_even_pair:
        print(1)
    # Impossible to make both sums even
    else:
        print(-1)

if __name__ == "__main__":
    solve()
