def yogurt_sale(test_cases):
    results = []
    for case in test_cases:
        n, a, b = case
        
        if b >= 2 * a:
            
            price = n * a
        else:
          
            price = (n // 2) * b + (n % 2) * a
            
        results.append(price)
    
    return results


t = int(input())
test_cases = [tuple(map(int, input().split())) for _ in range(t)]

results = yogurt_sale(test_cases)


for result in results:
    print(result)
