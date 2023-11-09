print("Простейший калькулятор")
def action(op, x, y):
    if op == '+':
        return (x + y)
    if op == '-':
        return (x - y)
    if op == '*':
        return(x * y)
    if op == '/':
        return(x / y)
    if op == '//':
        return(x // y)
    if op == '**':
        return(x ** y)
    elif op == '%':
        return(x % y)
    else:
        print("Ошибка. Неправильный ввод выражения")


def alist(s):
    mylist = []
    a = ''

    z = 0
    while z < len(s):

        if s[z] == ')':
            if a != '':
                mylist.append(int(a))
            mylist.append(s[z])
            a = ''
        elif s[z] == '(':
            mylist.append(s[z])


        elif z == len(s) - 1:
            a += s[z]
            mylist.append(int(a))


        elif s[z] in '0123456789':
            a += s[z]


        elif (s[z] + s[z + 1]) in '**//':
            if a != '':
                mylist.append(int(a))
            mylist.append(s[z] + s[z + 1])
            a = ''
            z += 1
        elif s[z] in '+-*/%':
            if a != '':
                mylist.append(int(a))
            mylist.append(s[z])
            a = ''

        if s[z] in '(+-*/%' and s[z + 1] in '+-':
            a += s[z + 1]
            z += 1

        z += 1

    return mylist


def p1(oper):
    pr = ['*', '/', '%', '//']
    ind = [oper.index(c) for c in pr if c in oper]
    ind.sort()

    return [oper[n] for n in ind]


def p2(oper):
    pr = ['+', '-']
    ind = [oper.index(c) for c in pr if c in oper]
    ind.sort()

    return [oper[n] for n in ind]

def calculator(primer):
    priority = ['(', '**'] + p1(primer) + p2(primer)

    w = 0
    while w < len(priority):
        c = priority[w]
        print(f'__{c}__', *primer)
        if c in primer:
            if c == '(':
                a_ind = primer.index('(')
                b_ind = primer.index(')')
                a = calculator(primer[a_ind+1: b_ind])
                del primer[a_ind: b_ind+1]
                primer.insert(a_ind, a)

                priority = ['(', '**'] + p1(primer) + p2(primer)
                w = -1
            else:
                a_ind = primer.index(c) - 1
                a = action(c, primer[a_ind], primer[a_ind+2])
                del primer[a_ind : a_ind+3]
                primer.insert(a_ind, a)

                priority = ['(', '**'] + p1(primer) + p2(primer)
                w = -1
        w += 1


    return primer[0]

def output():
    print('Введите выражение:')
    s = input()
    p = alist(s)
    print('Результат выражения =', calculator(p))
    output()
output()
