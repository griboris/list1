a = [1, 7, -3, 9, 0, -67, 34, 12, 45, 1000, 6,  8, -2, 99]
n = len(a)


for i in range(1, n):
    j = i
    while(j >= 1 and a[j] < a[j-1]):
        a[j], a[j-1] = a[j-1], a[j]
        j -= 1

print('Отсортированный список:', a)
