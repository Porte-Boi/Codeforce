def is_magic_num(n):
    num = str(n)
    i = 0
    while i < len(num):
        if num[i:i+3] == "144":
            i += 3
        elif num[i:i+2] == "14":
            i += 2
        elif num[i:i+1] == "1":
            i += 1
        else:
            return "NO"
    return "YES"

if __name__ == "__main__":
    n = input().strip()
    print(is_magic_num(n))