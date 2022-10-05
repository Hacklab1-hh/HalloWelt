


zahl1 = 8
zahl2 = 2

enthalten = zahl1//zahl2
rest = zahl1%zahl2
out = "Die Zahl " + str(zahl2) + " ist " + str(enthalten) + " mal in " + zahl1.__str__() + \
      " enthalten , \nes bleibt ein Rest von " + rest.__str__() + " übrig!"


print(out)
