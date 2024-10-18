
n = int(input().strip())

results = []

for _ in range(n):
    
    word1, word2 = input().strip().split()

    if word1[0] == word2[0]:
        results.append(f"{word1} {word2}")
        
    else:
        # Swap the first characters of word1 and word2
        modified_word1 = word2[0] + word1[1:]
        modified_word2 = word1[0] + word2[1:]
        results.append(f"{modified_word1} {modified_word2}")

for result in results:
    print(result)