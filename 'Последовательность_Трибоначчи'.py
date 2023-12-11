n = int(input())
a, b, c = 1, 1, 1

for i in range(n):
    if i >= 3:
        a, b, c = b, c, a + b + c
    print(c, end=' ')
