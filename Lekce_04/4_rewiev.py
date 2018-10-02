database = {'id123': {},'id124': {},'id125': {},'id126': {}}
FirstDict = {'name': 'Thomas', 'age': 45, 'Country': 'Czechia', 'City': 'Brno'}
SecondDict = {'name': 'Daniel', 'age': 34, 'Country': 'Czechia', 'City': 'Prague'}
ThirdDict = {'name': 'Eva', 'age': 43, 'Country': 'Czechia', 'City': 'Olomouc'}

database.update(id123=FirstDict)
# database['id123'] = FirstDict
database.update(id124=SecondDict)
database.update(id125=ThirdDict)
database.update(id126=ThirdDict['City'])
print(database)




TramStations = {
    'No.1' : ['Reckovice', 'Semilasso', 'Husitska', 'Jungmannova', 'Kartouzska', 'Sumavska', 'Hrnicrska', 'Pionyrska', 'Antoninska', 'Moravske nam.', 'Malinovske nam', 'Hlavni nadr.', 'Nove sady', 'Hybesova', 'Vaclavska', 'Mendlovo nam.', 'Vystaviste main', 'Vystaviste G2', 'Lipova', 'Pisarky'],
    'No.2' : ['Zidenice', 'Kuldova', 'Vojenska nemocnice', 'Tkalcovska', 'Kornerova', 'Malinovske nam.', 'Hlavni nadr.', 'Nove Sady', 'Hybesova', 'Vaclavska', 'Mendlovo nam.', 'Porici', 'Nemocnice UM', 'Celni', 'Hluboka', 'Ustredni hrbitov'],
    'No.4': ['Husovice','Nam. republiky','Vozovna Husovice','Mostecka','Travnickova', 'Tkalcovska', 'Kornerova', 'Malinovske nam.', 'Hlavni nadr.', 'Nove sady', 'Silingrovo nam.', 'Ceska', 'Komenskeho nam.', 'Obilni trh', 'Uvoz']}

station=(set(TramStations['No.1']) & set(TramStations['No.2']) & set(TramStations['No.4']))
print(station)

station=set(TramStations['No.1']).intersection(set(TramStations['No.2']),set (TramStations['No.4']))
print(station)
