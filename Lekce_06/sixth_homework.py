def max(lst):
    max_item = lst[0]
    for x in lst:
        if x > max_item:
            max_item = x
    return max_item

def min(lst):
    min_item = lst[0]
    for x in lst:
        if x < min_item:
            min_item = x
    return min_item

print(max([1,200,1515,12,221122,555454,1212,32323]))
print(min([65656,1,200,1515,12,221122,555454,1212,32323]))

def my_find(seq, item):
    for i, obj in enumerate(seq):
        if obj == item:
            return i
    return -1

print(my_find(['pear', 'apple', (23, 45), 653, {'name': 'John'}] , 'apple'))


# 1/
def reversed(item):
    rev_item = []
    for i in item:
        rev_item.insert(0,i)
    return rev_item

x = reversed(range(10))
print(x)

# 2/
def my_reversed(sequence):
    return list(sequence[::-1])
