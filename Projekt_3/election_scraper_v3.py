import csv
from urllib.parse import unquote

import requests
from bs4 import BeautifulSoup

from pprint import pprint as pp
from unidecode import unidecode

import codecs

# prevadi stranku do BS4
def load_page(url):
    content = requests.get(url).content
    return BeautifulSoup(content, "lxml")


def main():
    base_url = "https://volby.cz/pls/ps2017nss/ps3?xjazyk=CZ"
    region_url = 'https://volby.cz/pls/ps2017nss/'

    # timeout is set to 5 second and print OK
    try:
        s = requests.Session()
        page_response = s.get(base_url, timeout=5)
        if page_response.status_code == 200:
            print('OK')
        else:
            print(page_response.status_code)
            # notify, try again
    except requests.Timeout as e:
        print("It is time to timeout")
        print(str(e))

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

    # menu()
    # reg_choice = input('Vyber kraj: ')
    reg_choice = 'A'

    if reg_choice in short_reg.keys():
        url = short_reg.get(reg_choice)
        soup_region = load_page(url)
    else:
        print('Vybral sis špatně:')

    # #text hlavicka souhrnu dat krajske tabulky
    # data = []
    # header_all = soup_region.find('table',{'id': 'ps311_t1'})
    # for tr in header_all.find_all('tr'):
    #     head = [unidecode(th.text) for th in tr.find_all('th') if th !=[]]
    #     values = [unidecode(td.text) for td in tr.find_all('td') if td !=[]]
    #     print(head, values)

    summary_table = soup_region.find('table', {'id' : 'ps311_t1'})
    # replace br tags for " "
    for br in summary_table("br"):
        br.replace_with(" ")

    # SUMMARY_TABLE
    # words in th header
    header = []
    for th in summary_table.find_all('th'):
        header.append(th.text.strip())

    # numbers in td header
    numbers = []
    for td in summary_table.find_all('td'):
        numbers.append(unidecode(td.text.strip()))
    # print(header,numbers)

    # WRITING TO CSV
    with codecs.open("output.csv", "w", "utf-8") as file:
        file_writer = csv.writer(file)
        file_writer.writerow([header[0] + ' ' + header[7], header[1], header[2], header[3], header[4], header[5], header[6]])
        file_writer.writerow([numbers[0], numbers[3], numbers[4], numbers[5], numbers[6], numbers[7], numbers[8]])
        # for product in products:
        #     data = extract_product(product)
        #     file_writer.writerow(data)

    # RESULTS_TABLE

    table = soup_region.find_all('div', {'class' : 't2_470'})

    header_results = []
    for th in table[0].find_all('th'):
        header_results.append(th.text.strip())
    print(header_results)

    political_party = []
    for tr in table[0].find_all('tr'):
        party = []
        for td in tr.find_all('td'):
            party.append(unidecode(td.text.strip()))
        if party != []:
            political_party.append(party)
    # pp(political_party)

    for tr in table[1].find_all('tr'):
        party = []
        for td in tr.find_all('td'):
            party.append(unidecode(td.text.strip()))
        if party != []:
            political_party.append(party)
    pp(political_party)

    # political_party = []
    # for td in table[0].find_all('td'):
    #     political_party.append(unidecode(td.text.strip()))
    # print(political_party)


    # head_res=[]
    # reg_results_th =[head_res.append(th.text.strip()) for th in soup_region.find_all('th', {'class' : 't1sa1 t1sa2 t1sb1 t1sb2 t1sb3 t1sb4'})]
    # print(head_res)

    # for tr in soup_region.find_all('tr'):
    #     for th in tr.find_all('th'):
    #         print(th)

    # reg_results_div = soup_region.find('table', {'class' : 't2_470'})
    # # tables = reg_results_div.find_all('table')
    # # print(tables)
    # print(reg_results_div)


    # header = []
    # for th in reg_results_div.find_all('th'):
    #     # header.append(th.text.strip())
    #     print(th)


# <th colspan="3" id="sa1">Okrsky</th>
# <th id="sb1">celkem</th>
# <td class="cislo" headers="sa1 sb1">1&nbsp;109</td>
#
# <th rowspan="2" id="sa2">Voliči<br>v seznamu</th>
# <td class="cislo" headers="sa2">916&nbsp;940</td>
#
# <th rowspan="2" id="sa3">Vydané<br>obálky</th>
# <td class="cislo" headers="sa3">615&nbsp;519</td>
#
# <th rowspan="2" id="sa4">Volební<br>účast v %</th>
# <td class="cislo" headers="sa4">67,13</td>
#
# <th rowspan="2" id="sa5">Odevzdané<br>obálky</th>
# <td class="cislo" headers="sa5">614&nbsp;958</td>
#
# <th rowspan="2" id="sa6">Platné<br>hlasy</th>
# <td class="cislo" headers="sa6">611&nbsp;450</td>
#
# <th rowspan="2" id="sa7">% platných<br>hlasů</th>
# <td class="cislo" headers="sa7">99,43</td>




if __name__ == '__main__':
    main()
