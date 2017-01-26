#For verkefni
#Arnar Ólafsson
#26.1.17


#liður 1


#tölurnar skilgreindar og notandi beðinn um að slá inn tölu
tala1 = input("sláðu inn tölu 1")
tala2 = input("sláðu inn tölu 2")

#jöfnur fyrir tölurnar sem notandi valdi
summa = tala1 + tala2
margf = tala1 * tala2

#útkoma talnanna sem beðið var um
print("\nsumma talnanna er: %d" % summa)
print("marfjöldun talnanan er: %d " % margf)

#liður 2

#notandi beðinn um að slá inn for og eftirnafn
fornafn = input("\nsláðu inn fornafn: ")
eftirnafn = input("sláðu inn eftirnafn: ")

#svo heilsar forritið notanda
print("Halló %s %s" % (fornafn, eftirnafn))

#liður 3

#breytur skilgreindar og gefnar gildi
lagstafur = 0
hastafur = 0
H_eftir_L = 0
#notandi beðinn um að slá inn texta
texti = input("Sláðu inn texta: ")
#for lykkja notuð til að finna út hvort um hástaf eða lágstaf sé að ræða og
#if setningar notaðar til að telja hve margar
for c in range(len(texti)):
    if texti[c].isupper():
        hastafur += 1
       if texti[c+1].islower():
            H_eftir_L += 1
    if texti[c].islower():
        lagstafur += 1
        #niðurstöður prentaðar út hér að neðan 
print("Texti: %s" % texti)
print("Lágstafir: %s" %lagstafur)
print("Hástafir: %s" %hastafur)
print("Lágstafur á eftir Hástaf: %s" %H_eftir_L)







