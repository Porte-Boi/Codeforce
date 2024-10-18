t = int(input())

for _ in range(t):
    s = input()
    
    if len(set(s)) < 3:
        print(0)
        continue
    
    left = 0
    min_length = float('inf')
    count = {'1': 0, '2': 0, '3': 0}
    
    for right in range(len(s)):
        count[s[right]] += 1
        
        while all(count[char] > 0 for char in '123'):
            min_length = min(min_length, right - left + 1)
            count[s[left]] -= 1
            left += 1
    
    if min_length == float('inf'):
        print(0)
    else:
        print(min_length)



    
