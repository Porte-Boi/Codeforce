def favorite_cube_removed(n, f, k, a):

    favorite_value = a[f-1] # Get the value of the favorite cube
    sorted_a = sorted(a, reverse=True) # Sort the cubes in non_increasing order

   # first_k_values = sorted_a[:k]

    count_fav_value = sorted_a.count(favorite_value)

    min_index = sorted_a.index(favorite_value)
    max_index = min_index + count_fav_value - 1

    if max_index < k:
        return "YES"
    elif min_index >= k:
        return "NO"
    else:
        return "MAYBE"



if __name__ == "__main__":
    t = int(input())
    results = []

    for _ in range(t):
        n, f, k = map(int,input().split())
        a = list(map(int, input().split()))
        result = favorite_cube_removed(n, f, k, a)
        results.append(result)

    for result in results:
        print(result)
