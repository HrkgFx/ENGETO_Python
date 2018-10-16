
# MAXIMALNI ITEM v LISTU
def max(sequence):
    max_item = sequence[0]

    for item in sequence[1:]:
        if max_item < item:
            max_item = item

    return max_item


listB = [24, 13, -15, -36, 8, 22, 48, 25, 46, -9]
listB.sort(reverse=True) # listB gets modified

print listB
=> [48, 46, 25, 24, 22, 13, 8, -9, -15, -36]

NEBO

listB = [24, 13, -15, -36, 8, 22, 48, 25, 46, -9]
listC = sorted(listB, reverse=True) # listB remains untouched

print listC
=> [48, 46, 25, 24, 22, 13, 8, -9, -15, -36]
