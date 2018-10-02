a=1
b=2
if a < b:
    print('a je mensi nez b')

print('pokracuju')

text=''

if text:
    print('NESER')
print('cus')

if text and a < b:
    print('NESERU TED')
print('AHOJ')

if text or a < b:
    print('NESERU')
print('AHOJ KAMO')

print(bool([''][0]))
# FALSE
print(not bool(['']))
# FALSE

email='abc@c.cz'

'bflm' and '.' in email #-> je string true? and je tecka v emailu? jelikoz je string true, tak je cela podminka true


['@','.'] in email - ERROR
['@','.'] in [email] - diva se jestli tento list je v email listu coz je blbost
