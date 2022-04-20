"""
3. Európa legmagasabb épületei             (18pont)

Az UTF-8 kódolású legmagasabb.txt állomány Európa legmagasabb épületeinek adatait
tartalmazza a következő minta szerint (forrás: wikipedia.org):

név; város; ország; magasság; emelet; épült
10 Upper Bank Street; London; Anglia; 151; 32; 2003
25 Bank Street; London; Anglia; 153; 33; 2003
30 St Mary Axe; London; Anglia; 179, 8; 41; 2003
...

Az épület nevét, városát és országát az épület magassága (méter, valós szám), az emeletek
száma és az épület építésének éve követi. Az adatokat pontosvessző választja el.

3.1 Olvassa be az UTF-8 kódolású legmagasabb.txt állományban lévő adatokat és
tárolja el egy saját osztály (Épület) típusú listában! Ügyeljen rá, hogy az állomány első
sora az adatok fejlécét tartalmazza! A magasság érték tárolása (konvertálása) előtt cserélje
le a szöveges típusú adatban a vesszőt pontra! Az osztály használata nem KÖTELEZŐ DE több pontot kaphat érte!!! 

3.2 Határozza meg és írja ki a képernyőre, hogy hány épület található a forrásállományban!

3.3 Határozza meg és írja ki a képernyőre az állományba található épületek emeleteinek az
összegét!

3.4 Határozza meg és írja ki a képernyőre a minta szerint, a legmagasabb épület adatait!
Feltételezheti, hogy nem alakult ki holtverseny!

3.5 Döntse el, hogy az adatok között található-e olasz épület! A keresését ne folytassa, ha a
választ meg tudja adni!
"""

#név;város;ország;magasság;emelet;épült
#10 Upper Bank Street;London;Anglia;151;32;2003

class Epuletek:
  def __init__(self,sor):
    nev,varos,orszag,magassag,emelet,epult = sor.strip().split(";")
    self.nev = nev
    self.varos = varos
    self.orszag = orszag
    self.magassag = float(magassag.replace(",","."))
    self.emelet = int(emelet)
    self.epult = epult

with open("legmagasabb.txt","r",encoding="utf-8") as f:
  fejlec = f.readline()
  Épület = [Epuletek(sor) for sor in f]

#3.2

print(f"3.2 feladat: Épületek száma: {len(Épület)} db.")

#3.3

emeletek = sum([sor.emelet for sor in Épület])

print(f"3.3 feladat: Emeletek összege: {emeletek}")

#3.4

legmagasabb = [(sor.magassag,sor) for sor in Épület]

magas, adat = max(legmagasabb)
print(f"""3.4 feladat: A legmagasabb épület adatai:
        Név: {adat.nev}
        Város: {adat.varos}
        Ország: {adat.orszag}
        Magasság: {adat.magassag} m
        Emeletek száma: {adat.emelet}
        Épités éve: {adat.epult}
          """)
#3.5

#olasz = [sor for sor in Épület if sor.orszag == "Olaszország"]
olasz = True
while olasz:
  for sor in Épület:
    if sor.orszag == "Olaszország":
      olasz = False
  break

if olasz == False:
  print("3.5 feladat: Van olasz épület az adatok között!")
elif olasz == True:
  print("3.5 feladat: Nincs olasz épület az adatok között!")
  