import csv
from urllib.parse import unquote

import requests
from bs4 import BeautifulSoup

from pprint import pprint as pp
from unidecode import unidecode

# prevadi stranku do BS4
def load_page(url):
    content = requests.get(url).content
    return BeautifulSoup(content, "lxml")



def main():
    base_url = "https://volby.cz/pls/ps2017nss/ps3?xjazyk=CZ"
    region_url = 'https://volby.cz/pls/ps2017nss/'
    soup = load_page(base_url)

    regions = soup.find_all("h3", "kraj")
    dict_reg = {}

    for region in regions:
        name = region.text
        region_link = region.find('a')
        url = region_url + region_link.get('href')
        #slovnik nazev kraje - url
        dict_reg.update({name : url})

    #slovnník, který vrací na základě zkatky URL ze slovníku dict_reg
    short_reg = {'A' : dict_reg.get('Hlavní město Praha'),
                 'S' : dict_reg.get('Středočeský kraj'),
                 'C' : dict_reg.get('Jihočeský kraj'),
                 'P' : dict_reg.get('Plzeňský kraj'),
                 'K' : dict_reg.get('Karlovarský kraj'),
                 'U' : dict_reg.get('Ústecký kraj'),
                 'L' : dict_reg.get('Liberecký kraj'),
                 'H' : dict_reg.get('Královéhradecký kraj'),
                 'E' : dict_reg.get('Pardubický kraj'),
                 'M' : dict_reg.get('Olomoucký kraj'),
                 'T' : dict_reg.get('Moravskoslezský kraj'),
                 'B' : dict_reg.get('Jihomoravský kraj'),
                 'Z' : dict_reg.get('Zlínský kraj'),
                 'J' : dict_reg.get('Kraj Vysočina'),
                 }

    def menu():
        template = "Vyber {} pro {}"
        for key, value in dict_reg.items():
            for key2, value2 in short_reg.items():
                if value == value2:
                    print(template.format(key2, key))

    menu()
    reg_choice = input('Vyber kraj: ')


    if reg_choice in short_reg.keys():
        url = short_reg.get(reg_choice)
        # print(url)
        soup_region = load_page(url)
    else:
        print('Vybral sis špatně:')



# #vsechny tr na strance + obsah td
#     for tr in soup_region.find_all('tr'):
#         values = [unidecode(td.text) for td in tr.find_all('td')]
#         # print(values)
# # ulozeni dat do listu bez prazdnych listu
#     data = []
#     for tr in soup_region.find_all('tr'):
#         # values = [data.append(unidecode(td.text)) for td in tr.find_all('td', {'headers': 't1sa1'}) if td !=[]]
#         values = [data.append(unidecode(td.text)) for td in tr.find_all('td') if td !=[]]
#     print(data)

    #text hlavicka souhrnu dat krajske tabulky
    data = []
    header_all = soup_region.find('table',{'id': 'ps311_t1'})
    for tr in header_all.find_all('tr'):
        head = [unidecode(th.text) for th in tr.find_all('th') if th !=[]]
        values = [unidecode(td.text) for td in tr.find_all('td') if td !=[]]
        print(head, values)


    # #data souhrnu dat krajske tabulky
    # data = []
    # header_all = soup_region.find('table',{'id': 'ps311_t1'})
    # for tr in header_all.find_all('tr'):
    #     # values = [data.append(unidecode(td.text)) for td in tr.find_all('td', {'headers': 't1sa1'}) if td !=[]]
    #     values = [data.append(unidecode(td.text)) for td in tr.find_all('td') if td !=[]]
    # print(data)
    #
    #
    # results = soup_region.find('div',{'class': 't2_470'})
    # data = []
    # for th in results.find_all('th'):
    #     header = data.append(th.text.strip())
    # print(data)
    #
    # data = []
    # for tr in results.find_all('tr'):
    #     values = [data.append(unidecode(td.text)) for td in tr.find_all('td') if td !=[]]
    # pp(data)


    # data = []
    # header_all = soup_region.find('table',{'id': 'ps311_t1'})
    # for tr in header_all.find_all('tr'):
    #     for th in tr.find_all('th'):
    #         # th_c = th.replace("<br>", " ")
    #         print(type(th))
    #         # print(th_c)
    #         #
    #         # if th !=[]:
    #         #     data.append(unidecode(th_c.text))
    # print(data)



if __name__ == '__main__':
    main()

 # sauce = req.urlopen('https://volby.cz/pls/ps2017nss/ps3?xjazyk=CZ').read()
 # soup = bs.BeautifulSoup(sauce,'lxml')
