def int_conver(*items): # jedna hvezdicka vraci tuple
    nums = []
    for i in items:
        try:
            nums.append(int(i))
        except ValueError:
            pass
    return nums

print(int_conver('Hello', '23','12', 'Bob', 'new', '4312','5'))
