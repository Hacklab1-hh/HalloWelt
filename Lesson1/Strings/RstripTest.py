inhalt = "   Python 3 rocks    "
ausgabe = inhalt.rstrip()
print(ausgabe + ", daher Python lernen")


inhalt = "   Python 3 rocks 1233 4444"
ausgabe = inhalt.rstrip('4')
print(ausgabe + ", daher Python lernen")

inhalt = "   Python 3 rocks 1233 4444"
ausgabe = inhalt.rstrip('1234 ?XYZ')
print(ausgabe + ", daher Python lernen")


inhalt = " Python rocks \n \r\n "
ausgabe = inhalt.rstrip('')
print(ausgabe + ", damit sichtbar wird, was gelöscht wurde")


inhalt = " Python rocks \n \r\n "
ausgabe = inhalt.rstrip('\n ')
print(ausgabe + ", damit sichtbar wird, was gelöscht wurde")

inhalt = " Python rocks \n \r\n "
ausgabe = inhalt.rstrip('\n \r')
print(ausgabe + ", damit sichtbar wird, was gelöscht wurde")
