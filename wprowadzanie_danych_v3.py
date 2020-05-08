import math




obc = int(input('Podaj strefę śniegową: 90; 120; 160:'))
szer = float(input('Podaj szerokość zadaszenia:'))
glb = float(input('Podaj głębokośc zadaszenia:'))

# Moduł liczący sztangi krokwi #
krokwieilosc = math.ceil(szer / 0.7) + 1
krokwiem = krokwieilosc * glb
dlg = krokwiem // 6.5
y = krokwiem - dlg * 6.5
dszt = math.floor(krokwieilosc / 2)
if 2.2 < glb <= 3.2 and krokwieilosc % 2 != 0:
    krt = int(1)
elif 2.2 < glb <= 3.2 and krokwieilosc % 2 == 0:
    krt = int(0)
    dlg = dszt
elif glb <= 2.2:
    krt = krokwieilosc / 2
    dlg = 0
elif glb > 3.2:
    dlg = 0
    krt = krokwieilosc
# krokwie i pokrywy
cenakrokwi = dlg * 78.233 + krt * 54.16 + dlg * 31.99 + krt * 22.15
# krokwie + akcesoria
krokwieakc = cenakrokwi + krokwieilosc * 4.11 + krokwieilosc * 2 * 0.83
# uszczelki
if krokwiem * 2 < 100:
    krokwieall = krokwieakc + 35.7 + 36.55
elif krokwiem * 2 >= 100:
    krokwieall = krokwieakc + 2 * 35.7 + 2 * 36.55
# warunek na wzmocnienie krokwi
if obc == 90 and glb >= 3.4:
    krokwieall = krokwieall + (krokwieilosc - 2) * 54.799
    print('obciążenie = 90, wzmocnienie krokwi')
elif obc == 90 and glb < 3.4:
    krokwieall = krokwieall
    print('obciążenie = 90, bez wzmocnienia krokwi')
if obc == 120 and glb >= 3:
    krokwieall = krokwieall + (krokwieilosc - 2) * 54.799
    print('obciążenie = 120, wzmocnienie krokwi')
elif obc == 120 and glb < 3:
    krokwieall = krokwieall
    print('obciążenie = 120, bez wzmocnienia krokwi')
if obc == 160 and glb >= 2.8:
    krokwieall = krokwieall + (krokwieilosc - 2) * 54.799
    print('obciążenie = 160, wzmocnienie krokwi')
elif obc == 160 and glb < 2.8:
    krokwieall = krokwieall
    print('obciążenie = 160, bez wzmocnienia krokwi')
# Moduł liczący rynne
if szer <= 4.5:
    rynnakrt = int(1)
    rynnadlg = int(0)
elif 6.5 >= szer > 4.5:
    rynnakrt = int(0)
    rynnadlg = int(1)
elif 6.5 < szer <=9:
    rynnakrt =int(2)
    rynnadlg = int(0)
elif 11 > szer > 9:
    rynnakrt = int(1)
    rynnadlg = int(1)
# plaskownik L
if szer <= 6:
    L = int(1)
else: L = int(2)
#profile rynny + uszczelka + filtr + nakladka !!!!PRZELEW RYNNY na koncu!!!!!
rynnaprofile = rynnadlg*147.72 + rynnakrt*102.27 + L*10.32 + rynnakrt*40.05 + rynnadlg*57.85 + 88.39 + 17.68 + 17.33+szer*3.7*0.39

# KALENICA + uszczelka + nakladka przyscienna
kalenicaprofile = rynnadlg*69.18 + rynnadlg*29.74 + rynnakrt*47.9 + rynnakrt*20.59 + 71.14 + 5.63

#Slupy
if obc == 90:
    if szer <= 3 or (szer <= 3.5 and glb < 3.2):
        iloscslupow = int(2)
    elif 5.5 >= szer >= 4 or (5.5>=szer >= 3.5 and glb >= 3.2) or (4<=szer<=6 and glb<=3.6) or (4<=szer<=6.5 and glb<=3.4)or(4<=szer<=7 and glb<=2.2):
        iloscslupow = int(3)
    elif 7.5 >=szer>=9 or (9>=szer>=6 and glb>=3.8) or (9>=szer>=6.5 and glb>=3.6) or (9>=szer>=7 and glb>=2.4) or (7.5<=szer<=9.5 and glb<=3.8) or (7.5<=szer<=10 and glb<=3) or (7.5<=szer<=10.5 and glb<=2.6):
        iloscslupow = int(4)
    else: iloscslupow = int(5)
elif obc == 120:
    if szer <= 2.5 or (szer <= 3 and glb < 3.8):
        iloscslupow = int(2)
    elif 5.5 >= szer >= 3.5 or (6>=szer >= 5.5 and glb <= 3.6) or (6<=szer<=6.5 and glb<=3.2):
        iloscslupow = int(3)
    elif 8.5>=szer>=7 or (6.5>=szer>=6 and glb>=3.8) or (7>=szer>=6.5 and glb>=3.4) or (9>=szer>=7 and glb<=3.8) or (7.5<=szer<=9.5 and glb<=2.2):
        iloscslupow = int(4)
    else: iloscslupow = int(5)
elif obc == 160:
    if szer <= 2.5 or (szer <= 3 and glb < 3.4):
        iloscslupow = int(2)
    elif 5.5 >= szer >= 3.5 or (5>=szer >= 3 and glb >= 3.4) or (5<=szer<=6 and glb<=3):
        iloscslupow = int(3)
    elif 8>=szer>=6.5 or (6.5>=szer>=6 and glb>=3.2) or (8.5>=szer>=8 and glb<=3.8) or (9>=szer>=7 and glb<=3):
        iloscslupow = int(4)
    else: iloscslupow = int(5)
if iloscslupow == 2:
    slpkrt = int(1)
    pkrpkrt = int(1)
    pkrskrt = int(1)
    slpdlg = int(0) 
elif iloscslupow == 3:
    slpkrt = int(0)
    pkrpkrt = int(2)
    pkrskrt = int(1)
    slpdlg = int(1) 
elif iloscslupow == 4:
    slpkrt = int(2)
    pkrpkrt = int(3)
    pkrskrt = int(1)
    slpdlg = int(0) 
else:
    slpkrt = int(1)
    pkrpkrt = int(4)
    pkrskrt = int(2)
    slpdlg = int(1) 
#Slupy z pokrywami + kątownik
slupypok = slpkrt*92.49 + slpdlg*120.24 + pkrpkrt*26.75 + pkrskrt*46.18 + iloscslupow *3.11
#slupy calosc z akcesoriami
if szer > 6.5:
    lacznik = float(19.24)
else: lacznik = int(0)
z = 2*iloscslupow
slupyall = slupypok + z*0.27 + z*0.19 +iloscslupow*3.89+z*2*0.14+0.3+z*2*0.13+18.31+lacznik
#rygle
rygiel = (math.ceil(szer / 2.15))*7.68 + L*15.86 + 38.76
#inne akc3soria + butyl
if glb <= 2.3:
    prkrawedziowykrt = int(1)
    prkrawedziowydlg = int(0)
elif 3.2 >= szer >2.3:
    prkrawedziowykrt = int(0)
    prkrawedziowydlg = int(1)
else:
    prkrawedziowykrt = int(2)
    prkrawedziowydlg = int(0)
prkrawedziowy = prkrawedziowydlg*15.02 +prkrawedziowykrt*10.86 + 18.31
material = rygiel+slupyall+kalenicaprofile+rynnaprofile+krokwieall+prkrawedziowy
m = math.ceil(material)
# ------KONIEC SKRYPTU----------

print('Ilość słupów:',iloscslupow)
szklo = 0.3*(szer*glb*111)+(szer*glb*111)
print("Cena brutto materiału Cover:",m,'euro')
zl = m*4.4
cena = (0.03*zl+zl)+szklo
brutto = 0.23*cena+cena
print("Ostateczna cena brutto wynosi:",round(brutto,2),'zł')
