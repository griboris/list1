def quick_merge(mylist):
    result = mylist[0]
    
    for f in range(len(mylist)-1):
        p1 = 0
        p2 = 0
        list1 = result.copy()
        list2 = mylist[f+1].copy()
        result = []
        
        while p1 < len(list1) and p2 < len(list2):  # пока не закончился хотя бы один список
            if list1[p1] <= list2[p2]:
                result.append(list1[p1])
                p1 += 1
            else:
                result.append(list2[p2])
                p2 += 1

        if p1 < len(list1):   # прицепление остатка
            result += list1[p1:]
        else:                 # иначе прицепляем остаток другого списка
            result += list2[p2:]
    
    return result

mylist = []
for i in range(int(input())):
    mylist.append([int(i) for i in input().split()])

print(*quick_merge(mylist))
