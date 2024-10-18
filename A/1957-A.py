def maximum_polygons(stick_counts):
    max_polygons = 0
    for count in stick_counts.values():
        max_polygons += count // 3  # Only triangles considered as minimum polygon
    return max_polygons

if __name__ == "__main__":
    t = int(input().strip())
    results = []
    
    for _ in range(t):
        n = int(input().strip())
        sticks = list(map(int, input().strip().split()))
        
        from collections import Counter
        stick_counts = Counter(sticks)
        
        result = maximum_polygons(stick_counts)
        results.append(result)
    
    for result in results:
        print(result)
