mylist = []
for i in '10 9 8 7 6 5 4 3 2 1'.split():
    mylist.append(int(i))
for i in mylist:
    print(type(i), end = " ")
#mylist = [int(i) for i in mylist] 

print('')
print(max(mylist))

ind_min = mylist.index(min(mylist))
ind_max = mylist.index(max(mylist))

c = mylist[ind_min]
mylist[ind_min] = max(mylist)
mylist[ind_max] = c

print(*mylist)
