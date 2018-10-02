# try:
#     while True:
#         print(1)
# except Exception: #kdyz dam jen except tak odchytava vsechny podminky, ale nema se pouzivat nejvysse ten Exception
#     print('KONEC!')

try:
    f = open('hahaha.txt') # OSError je nadrazena Errno 2
except OSError:
    print('Nejde otevrit.')
