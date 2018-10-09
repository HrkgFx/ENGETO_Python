# Generátor a verifikátor rodného čísla
# Rozřazovací test na Python Hackathon vol.4. Program birthnumber.py bude pracovat v 2 módech -
# buď bude generovat nové rodné číslo (žádný argument), nebo bude verifikovat poskytnuté číslo z příkazového řádku (1 argument).
# Podmínky pro generování a ověřování rodného čísla jsou následující:
# číslo musí obsahovat buď 10 čísel (pro lidi, kteří se narodili po roce 1954), nebo 9 čísel (pro lidi, kteří se narodili do roku 1953),
# číslo má 2 části - datum narození a kontrolní součet (CCCC) v tvaru YYMMDD/CCCC,
# celé číslo musí být dělitelné číslem 11,
# ženy mají v měsíci narození přidanou hodnotu 50. Příklad: 861107/2239 odpovídá rodnému číslu muže, který se narodil 7.11.1986. 025226/1306 odpovídá rodnému číslu ženy naroezené 26.02.2002.
