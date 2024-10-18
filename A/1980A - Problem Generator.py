def solve():
    # Read input values
    n, m = map(int, input().split())  # Number of problems and rounds
    s = input().strip()  # String containing difficulty levels
    
    # Initialize a list to count occurrences of each difficulty level
    v = [0] * 7  # There are 7 difficulty levels 'A' to 'G'
    
    # Count occurrences of each difficulty level in s
    for i, char in enumerate('ABCDEFG'):
        v[i] = s.count(char)

    # Calculate the minimum number of additional problems needed
    ans = 0
    for count in v:
        if count < m:
            ans += (m - count)
    
    # Output the result for the current test case
    print(ans)

if __name__ == "__main__":
    TCS = int(input().strip())  # Number of test cases
    for _ in range(TCS):
        solve()
