n = int(input()[1:])
mylist = []
for i in range(n):
    s = input()
    if s.count('#') > 0:
        mylist.extend(s.split('#'))
        del mylist[-1]
    else:
        mylist.append(s)
    mylist[i] = mylist[i].rstrip()

print(*mylist, sep='\n')
