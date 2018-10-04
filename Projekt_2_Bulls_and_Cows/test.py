from operator import itemgetter

with open('all_results.txt') as rs:
    result_line = rs.readlines()

result_line = [line.strip('\n') for line in result_line]
print(result_line)

to_list = [item.split(', ') for item in result_line]
print(to_list)

# transform str to int on index 1 on attempts
for x in to_list[1:]:
    x[1] = int(x[1])
    print(x[1])

print(to_list)
print(50*'*')

top_time = sorted(to_list[1:], key=itemgetter(2))
print('TT',top_time)
top_score = sorted(to_list[1:], key=itemgetter(1))
print('TS',top_score)

print(top_time)
print(50*'*')
print('TOP Time')
for i in top_time:
    print(i)

print(50*'*')
print('TOP Attempts')
for i in top_score:
    print(i)

print(50*'*')


    # if top_score == []:
    #     top_score.extend[i]
    # else:
    #     for item in len(top_score):
    #         if i[1] <= top_score[0][1]:
    #         top_score.extend[i]
