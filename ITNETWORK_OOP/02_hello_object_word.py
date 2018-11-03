# # 1/
# class Pozdrav:
#     def pozdrav(self, jmeno):
#         print("Ahoj, jak se máš {0}?".format(jmeno))
#
#
# ahoj = Pozdrav()
# # ahoj.pozdrav()
# ahoj.pozdrav('Robe')

# # 2/
# class Pozdrav:
#     def pozdrav(self, jmeno):
#         print("{0} {1}!".format(self.text, jmeno))
#
# ahoj = Pozdrav()
# ahoj.text = "Ahoj uživateli"
# ahoj.pozdrav("Karel")
# ahoj.pozdrav("Petr")
# ahoj.text = "Vítám tě tu programátore"
# ahoj.pozdrav("Richarde")

# # 3/
class Pozdrav:
    """
    Trida reprezentuje pozdraveni, které slouzi ke zdraveni uzivatelu.
    """

    def pozdrav(self, jmeno):
        return "{0} {1}!".format(self.text, jmeno)

ahoj = Pozdrav()
ahoj.text = "Ahoj uživateli"
print(ahoj.pozdrav("Karel"))
print(ahoj.pozdrav("Petr"))
ahoj.text = "Vítám tě tu programátore"
print(ahoj.pozdrav("Richarde"))


help(Pozdrav)
