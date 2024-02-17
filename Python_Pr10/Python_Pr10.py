#3
number = [5, 12, 8, 20, 10, 3, 7]

# Печать гистограммы
for num in number:
    print('*' * num)
#2.3
from random import *
vanused=[]
N=int(input("Mitu elemendi? "))
for i in range(N):
    vanus=randint(10,97)
    vanused.append(vanus)
print(vanused)
min_=min(vanused)
max_=max(vanused)
sum_=sum(vanused)
avg_=sum_/N
print("Minimum",min_)
print("Maksimum",max_)
print("Kogusumma",sum_)
print("keskminne",avg_)
#2.2
opilased = ['Juhan','Kati','Mario','Mario','Mati','Mati']
uus=[]
for nimi in opilased:
    if nimi not in uus: #not in
        uus.append(nimi)
print(uus)

#2.1
print("")
nimed=[]
for i in range(5):
    nimi=input("Sisestage {i+1}. nimi: ").capitalize()
    nimed.append(nimi)
#vim_nimi=nimi
print("Oli: ",nimed)
nimed.sort()
print("Sortimise pärast",nimed)
print("Vilmasena oli lisatud:",nimi)
print("")

vananimi=input("Mis nimi on vaja asandada? ")
if nimed.count(vananimi)>0:
    uusnimi=input("Mis on uus nimi? ").capitalize()
    #for nimi in nimed:
    #    if nimi==vananimi: 
    #        nimed[nimi.replace(vananimi,uusnimi)]
    i=0
    for nimi in nimed:
        if nimi==vananimi:
            nimed[i]=uusnimi
        i+=1

else:
    print(f"{vananimi} ei ole")
print(nimed)





