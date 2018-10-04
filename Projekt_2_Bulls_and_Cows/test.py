with open('all_results.txt') as rs:
    result_line = rs.readlines()

result_line = [line.strip('\n') for line in result_line]
# print(result_line)

to_list = [item.split(', ') for item in result_line]
print(to_list)

top_score = []
#transform str to int on index 1 on attempts
for x in to_list[1:]:
    x[1] = int(x[1])
    print(x[1])

print(to_list)
print(50*'*')

top_score = []
for i in to_list[1:]:
    print(i)
#     if top_score == []:
#         top_score.append[i]
#     else:
#         if i[1] <= top_score[0][1]:
#             top_score.append[i]
