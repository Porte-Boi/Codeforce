t= int(input())

for _ in range(t):
    
    n=int(input())
    s=input()
    i=0
    while i<n and s[i]=='1':
        i+=1
    if i==n:
        if n==4:
            print("Yes")
        else:
            print("No")
        continue
    i-=1
    if i*i==n:
        print("Yes")
    else:
        print("No")