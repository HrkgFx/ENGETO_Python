#
# price1=int(input('Zadej cenu 1. produktu: '))
# price2=int(input('Zadej cenu 2. produktu: '))
# price3=int(input('Zadej cenu 3. produktu: '))
#
# cart = [price1, price2, price3]
# print(len(cart))
#
#
# total=price1 + price2 + price3
# print(cart)
# print(total)

# cart = []
# total = 0
#
# pocet = int(input('Zadej počet produktu pro nakupni seznam: '))
# while pocet > len(cart):
#     price = int(input('Zadej cenu ' + str(len(cart)+1) + ': '))
#     cart.append(price)
#     total += price
#
# print(cart)
# print(total)

# cart = []
# total = 0
# swich = True
#
# while swich:
#     user_input = input('Zadej cenu ' + str(len(cart)+1) + ' a Q pro konec: ')
#     if user_input == 'Q' or user_input == 'q':
#             swich = False
#     else:
#         cart.append(int(user_input))
#         total += int(user_input)
#
#
# print(cart)
# print(total)


# cart = []
# total = 0
#
# while True:
#     user_input = input('Zadej cenu ' + str(len(cart)+1) + ' a Q pro konec: ')
#     if user_input == 'Q' or user_input == 'q':
#             break
#     cart.append(int(user_input))
#     total += int(user_input)
#
#
# print(cart)
# print(total)


# cisla 1 az 10

# x=0
# l1 = ['maslo', 'chleba', 'sunka', 'parky', 'paprika']
# while x < len(l1):
#     print('V kosiku mas: ' + l1[x])
#     x += 1


cart = []
total = 0
cart_price = {}

while True:
    user_input1 = input('Zadej co davas do kosiku (nebo Q pro konec): ')
    if user_input1 == 'Q' or user_input1 == 'q':
            break

    user_input2 = input('Zadej cenu: ')
    # cart_price.update(user_input1 = user_input2)
    cart_price[user_input1] = int(user_input2)
    cart.append(int(user_input2))
    total += int(user_input2)

#CTRL + C - vyhodi (chybu) automaticky z programu

print(cart_price)
print(total)
