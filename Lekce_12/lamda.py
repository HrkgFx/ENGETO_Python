# lamda arg: arg+2
# lamda co se bude vracet: a kod
# kdy se to pouziva?
# funkce sorted

x = [3,2,4,5,4]
sorted(x)

print(sorted(x, key = lambda x: -x))

# [1.2.3]
# lmada x: -x
# -1
# -2
# -3


y = map(lambda x:-x,[1,4,5,67,3])
for x in y:
    print(x)

y = list(map(lambda x:-x,[1,4,5,67,3]))
print(y)

# toto je blbe zapisove
print(list(map(lambda x: str.upper(x),['a','b','c','d'])))

# jen metodu, nechci ji spoustet
print(list(map(str.upper,['a','b','c','d'])))

# map pouziva se na hromadnejsi upravy

# RGB
# 0,0,255
# 255,0,255
# 0,0,0 - cerna
#
# [1367.6 , 32, -425] funkce ktera me to pak prevadi na 0 - 255



def sude(x):
    if x%2==0:
        return x

print(list(filter(sude, [2,3,4,5])))

l1 = list(filter(sude, range(10)))
print(l1)


def fn(x):
    if x == 1:
        return x
    return x*fn(x-1)
