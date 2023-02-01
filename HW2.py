
#1.
print ("Vnesete broj")
broj = int (input ())
for i in range (broj):
    print (i)
print ("Progamata zavrsi :)" )


#2.
print ("Kolku pati bi sakale da konvertirate MKD vo EUR")
broj= int (input())
for i in range (broj):
    print ("Vnesete iznos vo MKD sto bi sakele da go konvertirate")
    iznos= int (input ())
    total= iznos /61.4
    print (" Za {} MKD ke dobiete {} EUR".format (iznos, total))
print ("Vi blogodarime na koristenjeto na uslugata. Imajte ubav den")


#3
print ("Kolku pati bi sakale da ja koristite programata")
pati = int (input())
for i in range (pati):
    print ("Vnesete broj")
    broj = int (input ())
    for i in range (broj):
        if i%2==0:
            print (i )
print ("Progamata zavrsi :)" )


#4
god1 = 0
god2 =0
da ="da"
total = 0
print ("Zdravo.")
while da == "da":
    ime = str (input ("Vnesete ime: "))
    prezime = str (input ("Vnesete prezime: "))
    godini = int(input("Vnesete godini: "))
    if godini <18:
        print("Liceto e maloletno")
        god1 +=1
    else:
        print ("Liceto e polnoletno")
        god2 +=1
    total=god1+god2
    da=input ("da prodolzime? 'da' ili 'ne'")
print ("Od vnesenite {} potadoci, {} se polnoletni lica i {} se maloletni lica".format (total,god2, god1))


#5
da="da"
total = 0
while da=="da":
    pr=str (input("Vnesete go vasiot produkt: "))
    ce= int (input ("Cena na {} izneusva: ".format (pr)))
    total +=ce
    da=input ("da prodolzime? 'da' ili 'ne'")
print ("Vkupno za naplata {} mkd".format (total))
print ("Izberete nacin na plakanje: 'kes' ili 'karticka'")
pay=str (input ())
if pay == "kes":
    dep=int(input("So kolku MKD ke platite: "))
    kusur=dep-total
    print ("Za vrakanje ima {} mkd".format (kusur))
elif pay =="karticka":
    pin=int (input ("Vnesete go Vasiot pin: "))
    print ("Transakcijata e uspesna. Imajte ubav den")
