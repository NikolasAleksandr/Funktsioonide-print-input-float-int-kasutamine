#Ylesanne "Funktsioonide print(),input(), float(), int() kasutamine"
from random import *
#1
print("Tere, maailm!".center(50))
nimi=input("\tMis on sinu nimi?: ") 
print("Tere, maailm! Tervitan sind {0}".format(nimi))
vanus=int(input("Kui vana sa oled"))
print("Tere, maailm! Tervitan sind {0}! Sa oled {1} aastat vana.".format(nimi, vanus))


#2
vanus = 18 #int
eesnimi = "Jaak" #str
pikkus = 16.5 #float
kas_kaib_koolis = True #bool

#3
kommid_laual=int(input("Laul olevate kommide arv: "))
print("Laual on", kommid_laual, "komm(i).")
soovitud_kommid = int(input("Mitu kommi soovid laualt ara votta? "))
kommid_laual -= soovitud_kommid
print("Laual on nuud", kommid_laual, "komm(i).")

#4
puu_ymbermoot=float(input("Sisesta puu ymbermoot (meetrites): "))
puu_labimoot = puu_ymbermoot / 3.14
print("Puu labimoot on", puu_labimoot)

#5
print("Ristkyyliku mootmed")
N=float(input("Sisesta ristkyyliku esimene kaatet (meetrites): "))
M=float(input("Sisesta ristkyyliku teine kaatet (meetrites): "))
d = (N**2 + M**2)**0.5
print("Ristkyyliku diagonaal on umbes", d, "meetrit.")

#6
try:
    aeg = float(input("Mitu tundi kulus soiduks? "))
    teepikkus = float(input("Mitu kilomeetrit soitsid? "))
    kiirus = teepikkus / aeg
    print("Sinu kiirus oli " + str(kiirus) + " km/h")
except :
    print("Andmetüübi viga!")
    

#7
arv1 = int(input("Sisesta esimene taisarv: "))
arv2 = int(input("Sisesta teine taisarv: "))
arv3 = int(input("Sisesta kolmas taisarv: "))
arv4 = int(input("Sisesta neljas taisarv: "))
arv5 = int(input("Sisesta viies taisarv: "))
keskmine = (arv1 + arv2 + arv3 + arv4 + arv5) / 5
print("Arvude aritmeetiline keskmine on:", keskmine)

#7
arv1=randint(1,100)
arv2=randint(1,100)
arv3=randint(1,100)
arv4=randint(1,100)
arv5=randint(1,100)
print("Arvude {0},{1}, {2}, {3} ja {4} aritmeetiline keskmine on {5}".format(arv1,arv2,arv3,arv4,arv5, (arv1+arv2+arv3+arv4+arv5)/5))

#8
konn = """
   @..@
  (----)
 ( \__/ )
 ^^ "" ^^
"""

print(konn)

#9
a = int(input("Sisesta esimese kylje pikkus: "))
b = int(input("Sisesta teise kylje pikkus: "))
c = int(input("Sisesta kolmanda kylje pikkus: "))
ymbermoot = a + b + c
print("Kolmnurga ymbermoot on:", ymbermoot)

#10
pitsa_hind = 12.90
jootraha_protsent = 10
jootraha = pitsa_hind * (jootraha_protsent / 100)
kogusumma = pitsa_hind + jootraha
print(f"Pitsa hind: {pitsa_hind}€")
print(f"Jootraha ({jootraha_protsent}%): {jootraha}€")
print(f"Igayks peab maksma: {kogusumma / 2}€")


