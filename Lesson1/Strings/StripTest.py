inhalt = "   Python lernen  "
ausgabe = inhalt.strip()
print(ausgabe)

inhalt = "1.) Python lernen  "
ausgabe = inhalt.strip('1')
print(ausgabe)

inhalt = "1.) python lernen  "
ausgabe = inhalt.strip('.) 1234567890')
print(ausgabe)
