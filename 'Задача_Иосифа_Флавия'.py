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

n = int(input())
k = int(input())
 
res = 0
for i in range(1, n+1):
    res = (res + k) % i
print(res + 1)

n = int(input())
k = int(input())
list = [i for i in range(1, n + 1)]

while len(list) != 1:
    for i in range(0, k-1):
        list.append(list[i])
    del list[0:k]

print(*list)
