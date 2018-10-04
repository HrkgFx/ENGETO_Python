with open('all_results.txt') as rs:
    result_line = rs.readlines()

result_line = [line.strip('\n') for line in result_line]
# print(result_line)

to_list = [item.split(', ') for item in result_line]
print(to_list)

# num_int = [list(map(int, x)) for x in to_list[1:][1]]
# print(num_int)

# num_test = [x for x in to_list[1:][1]]
for x in to_list[1:]:
    print(x)
    # x = [int(i) for i in x[1]]
    x[1] = list(map(int, x[1]))
    print(x[1])
# best_attempts = []

# for i in to_list[1:]:
#     print(i)
#     for j in i[1]:
#         num_int = list(map(int, j)
#         print(num_int)
