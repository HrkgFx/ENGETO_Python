# json je slovnik
# CSV --> list
# JSON ---> dict

import json
# json string prevede na dictionary a naopak

f = open('test.json')
json_string = f.read()
# f.close()
#
json_dict = json.loads(json_string)
#
# # print(json_dict)
# for i in json_dict.get('results'):
#     # print(60*'*')
#     print(i.get('geometry'))

# print(60*'*')
# print(json_dict.get('results')[0].get('geometry'))

print(json_dict)

json_dict = json.loads(json_string)

json_dict.get('results').append('Nic jsem nenašel.')
f = open('test.json', 'w')
json_write = json.dumps(json_dict)
f.write(json_write)
f.close()

print(json_dict)
