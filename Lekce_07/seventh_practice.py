# # 2.11
# import random
# dataset= [['Name','Item','Amount','Unit_Price']]
#
# customers = ['Bettison, Elnora',
#              'Doro, Jeffrey',
#              'Idalia, Craig',
#              'Conyard, Phil',
#              'Skupinski, Wilbert',
#              'McShee, Glenn',
#              'Pate, Ashley',
#              'Woodison, Annie']
#
# products = [('DROXIA', 33.86),('WRINKLESS PLUS',23.55),
#             ('Claravis', 9.85), ('Nadolol', 12.35),
#             ('Quinapril', 34.89), ('Doxycycline Hyclate', 23.43),
#             ('Metolazone', 43.06), ('PAXIL', 14.78)]
#
# def generate_dataset(num_rows):
#
#     for i in range(num_rows):
#
#         name = random.choice(customers)
#         item, price= random.choice(products)
#         amount = random.randint(1,100)
#         total_price = amount * price
#
#         row = [name,item, amount, price, total_price]
#         dataset.append(row)
#
#     return dataset
#
# print(generate_dataset(3))
#
# # 3.3
# name = 'Dylen'
# def func():
#     print(name)
#
# func()
#
# # def func():
# #     name1 = 'John'
# #     print(name1)
# #
# # full_name = name1 + ' Smith'
# #
# # print(full_name)
#
# # LEGB
# # Local
# # Enclosing
# # Global
# # Built-in
#
# # from pprint import pprint as pp
# # pp(__builtins__.__dict__)
#
# def count(sequence,item):
#     result = 0
#     for i in sequence:
#         if i == item:
#             result += 1
#     return result
#
# print(count('Hello', 'l'))
#
#
# # 3.6
# def order_sequence(my_list):
#     for i in range(1,len(my_list)):
#         pos = i
#         while pos > 0 and my_list[pos-1] > my_list[pos]:
#             my_list[pos],my_list[pos-1] =  my_list[pos-1], my_list[pos]
#             pos -= 1
#
#
# def generate_random_list(size):
#     lst = []
#     for i in range(size):
#         lst.append(random.randint(1,100))
#     return lst
#
# l = generate_random_list(10)
# print('Before sorting:',l)
# order_sequence(l)
# print('After sorting:', l)
#
# # 3.7
# def order_sequence():
#     for i in range(1,len(l)):
#         pos = i
#         while pos > 0 and l[pos-1] > l[pos]:
#             l[pos],l[pos-1] =  l[pos-1], l[pos]
#             pos -= 1
#     return l
#
# def generate_random_list(size):
#     lst = []
#     for i in range(size):
#         lst.append(random.randint(1,100))
#     return lst
#
# l = generate_random_list(10)
# print('Before sorting:',l)
# print('After sorting:', order_sequence())
#
# # 3.8
# name = 'John'
# surname = 'Smith'
#
# def func():
#     name = 'Bob'
#     fullname = ' '.join((name,surname))
#     print(fullname)
#     print(age)
#
# func()


# name = 'Bob'
# def func():
#     surname = 'Smith'
#     name = name + " " + surname
#     print(locals())
#     return name
#
# func()

# def func(a,b):
#     return a + b
#
# func()

def change_coins(amount, coins = [50,20,10,5,2,1]):
    coin_counts = {}

    for coin in coins:
        if not amount: break
        count,amount=divmod(amount,coin)
        if count:
            coin_counts[coin]=count

    return coin_counts

print(change_coins())
