from operator import itemgetter

with open('all_results.txt') as rs:
    result_line = rs.readlines()

# remove next line \n
result_line = [line.strip('\n') for line in result_line]
# print(result_line)

# convert to list from file - row is one item in list
to_list = [item.split(', ') for item in result_line]
# print(to_list)

# transform str to int on index 1 on attempts
for x in to_list[1:]:
    x[1] = int(x[1])
    # print(x[1])

#sort list by first index - attempts
top_score = sorted(to_list[1:], key=itemgetter(1))
#sort list by second index - time
top_time = sorted(to_list[1:], key=itemgetter(2))

# print(88*'-')
# print('| {:^20}'.format(to_list[0][0]))

len_header = len(("|{0:^12}|{1:^12}|{2:^18}|".format(*to_list[0])))
t_line = len_header * '-'
print(t_line)

print("|{0:^12}|{1:^12}|{2:^18}|".format(*to_list[0]))
print(t_line)

for i in top_score:
        if len(top_score) < 10:
            print("|",i[0],"|",i[1],"|",i[2],"|")
            print("|{0:^12}|{1:^12}|{2:^18}|".format(*top_score[]))


print('Ahoj moje jmeno je: {1:^9.5} a prijmeni: {0:#>20}.'.format(*jmeno))
