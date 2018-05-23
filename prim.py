# primzahlen überprüfen

zahl = input("Bitte Zahl eingeben")
z = int(zahl)
a = False
for i in range(2,z):

    if(z % i == 0):
        a = True
    
      

if (a == True):
   print("Keine Primzahl")
else:
    print("Primzahl")
