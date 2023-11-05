n = int(input())
k = int(input())-1

ones = [i+1 for i in range(n)]

i = k
while len(ones) > 1:

    while i < len(ones) and len(ones) > 1:       
        del ones[i]
        i += k
        
    i = i-len(ones)
    
print(*ones)
