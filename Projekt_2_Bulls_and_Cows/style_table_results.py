from operator import itemgetter

with open('all_results.txt') as rs:
    result_line = rs.readlines()

# remove next line \n
result_line = [line.strip('\n') for line in result_line]

# convert to list from file - row is one item in list
to_list = [item.split(', ') for item in result_line]

# transform str to int on index 1 on attempts
for x in to_list[1:]:
    x[1] = int(x[1])

#sort list by first index - attempts
top_score = sorted(to_list[1:], key=itemgetter(1))
#sort list by second index - time
top_time = sorted(to_list[1:], key=itemgetter(2))

#counting length header
len_header = len(("|{0:^12}|{1:^12}|{2:^18}|".format(*to_list[0])))

#horizontal table line
t_line = len_header * '-'

#header table
print(t_line)
print("|{0:^12}|{1:^12}|{2:^18}|".format(*to_list[0]))
print(t_line)

#print row in all_results.txt
for index,value in enumerate(top_score):
        if index < 10:
            print("|{0:^12}|{1:^12}|{2:^18}|".format(*top_score[index]))
        else:
            print(t_line)
            break
print(t_line)
