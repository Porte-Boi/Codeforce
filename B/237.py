def solve():
    n = int(input())  
    if n == 0:
        print(0)
        return
    
    
    prev_h, prev_m = map(int, input().split())
    max_cash_needed = 1  
    current_count = 1  

    
    for _ in range(n - 1):
        h, m = map(int, input().split())
        
        if h == prev_h and m == prev_m:
            
            current_count += 1
        else:
            
            max_cash_needed = max(max_cash_needed, current_count)
            current_count = 1  
        
        
        prev_h, prev_m = h, m
    
    
    max_cash_needed = max(max_cash_needed, current_count)
    
    print(max_cash_needed)

if __name__ == "__main__":
    solve()
