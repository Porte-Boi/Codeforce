n = int(input())
a = list(map(int, input().split()))

total_sum = sum(a)

max_equal_elements = n if total_sum % n == 0 else n - 1

print(max_equal_elements)