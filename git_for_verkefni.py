#For verkefni
#Arnar Ólafsson
#26.1.17


#liður 1

tala1 = input("sláðu inn tölu 1")
tala2 = input("sláðu inn tölu 2")

summa = tala1 + tala2
margf = tala1 * tala2

print("\nsumma talnanna er: %d" % summa)
print("marfjöldun talnanan er: %d " % margf)

#liður 2

fornafn = input("\nsláðu inn fornafn: ")
eftirnafn = input("sláðu inn eftirnafn: ")

print("Halló %s %s" % (fornafn, eftirnafn))

#liður 3
lagstafur = 0
hastafur = 0
H_eftir_L = 0
texti = input("Sláðu inn texta: ")
for c in range(len(texti)):
    if texti[c].isupper():
        hastafur += 1
       if texti[c+1].islower():
            H_eftir_L += 1
    if texti[c].islower():
        lagstafur += 1
print("Texti: %s" % texti)
print("Lágstafir: %s" %lagstafur)
print("Hástafir: %s" %hastafur)
print("Lágstafur á eftir Hástaf: %s" %H_eftir_L)







