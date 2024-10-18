def convert_to_12_hour_format(twenty_four_hour_time):
    
    hh, mm = map(int, twenty_four_hour_time.split(':'))
    
    
    if hh == 0:
        return f"12:{mm:02d} AM"  
    elif hh < 12:
        return f"{hh:02d}:{mm:02d} AM"  
    elif hh == 12:
        return f"12:{mm:02d} PM"  
    else:
        return f"{hh - 12:02d}:{mm:02d} PM" 

def main():
    t = int(input())
    results = []

    for _ in range(t):
        time_24h = input()
        result = convert_to_12_hour_format(time_24h)
        results.append(result)

    
    for result in results:
        print(result)

if __name__ == "__main__":
    main()
