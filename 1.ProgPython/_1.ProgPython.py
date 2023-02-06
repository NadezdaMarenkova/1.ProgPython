from math import*


# Ülesanne 1
# Kirjuta programm, mis sind tervitab.

print("\t*  Hello World!!!  *")

# Ülesanne 2
# Koosta programm on öeldud tehte 3 + 8 / (4 - 2) * 4 vastuse?
# +Kuidas mõjutab sulgude kasutamine/kasutamata jätmine tööd?
# +Katseta erinevaid kombinatsioone paralleelselt ning lisa ka selgitavad tekstid, et väljund oleks arusaadav.
print("\t*  Посчитаем пример :)  *")
print("\n3 + 8 / (4 - 2) * 4 = ")

print(3 + 8 / (4 - 2) * 4)
"""
Самый простой способ, что бы вывести ответ.
В ответе будет присудствовать плавающая точка.
"""
print(int(3 + 8 / (4 - 2) * 4))
"""
Ответ будет без плавающей точки.
"""
print(3 + 8 / 4 - 2 * 4) 
"""
Пробуем убрать скобки из примера.
Поменялась последовательность решения примера.
"""

# Ülesanne 2.1
# Ruudu sees asub ring. Ringi raadius on 3.
# Leia ja väljasta ekraanile ruudu pindala, ruudu ümbermõõt, 
# ringi pindala, ringi ümbermõõt.

"""
print("Площадь квадрата: ", 6**2)
print("Периметр квадрата: ", 4*6)
print("Площадь круга: ", pi*3**2)
print("Периметр круга: ", 2*pi*3) 
"""
# r - радиус, а - сторона квадрата(r+r)

print("\n\t*  Следующее задание!  *")

r=3 
a=r+r 

S1=a**2
P1=4*a
S2=pi*r**2
P2=2*pi*r 

print("\nПлощадь квадрата: ", S1)
print("Периметр квадрата: ", P1)
print("Площадь круга: ", round (S2, 2))
print("Периметр круга: ", round (P2, 2))

# Ülesanne 2.2
"""
Koosta programm, mis arvutab välja Maa ümbermõõdu ekvaatori kohal 2-eurostes 
müntides ehk teisisõnu: kui palju 2-euroseid münte tuleb panna üksteise kõrvale, 
et rida ulatuks ümber Maa. Kasuta teadmist, et Maa raadius ekvaatori kohal on 6378 km.

Algandmed (Maa raadius, mündi läbimõõt jne) omista programmi alguses sisukate nimedega
muutujatele. Kuna ümbermõõdu arvutamiseks tuleb kasutada  PI-d (3,14...), siis võid 
selle (umbkaudse) väärtuse otse programmi kirjutada.  
Püüdke välja mõelda viise, kuidas juhuslikest vigadest valemis hoiduda 
(teisendamised, ümardamise täpsus jne). Võimalusel võrrelge tulemusi teistega. 
Kui on erinevusi, leidke ühiselt põhjused.
Kas programm on piisavalt hästi kirjutatud, et algandmete muutumise korral 
(näiteks juhul, kui on vaja arvutada Marsi ümbermõõtu 1-eurostes müntides) 
on parandusi selge ja lihtne teha?
"""
# Rmaa - радиус земли

# Dmunt2 - диаметр 2-х евровой монеты
# Dmunt1 - диаметр 1-й евровой монеты
# Сmaa - периметр земли
# Rmaa - радиус Земли
# KK - кол-во монет
# Rplanet - радиус 
# Cplanet - периметр

Rmaa=6378
Rmars=3389,5
Dmunt2=0.00002575
Dmunt1=0.00002325

#Maa
Cmaa=2*pi*Rmaa 
K1=Cmaa//Dmunt2

print("\n\t*  Хочешь узнать, сколько монет понадобиться, \n\tчтобы вычислить длину окружности Земли над экватором?  *")


print("\nПериметр земли: ", round(Cmaa,1))
print(int(K1), " -  2-евровых монет нужно положить рядом друг с другом, чтобы линия проходила вокруг Земли.")

"""
#Mars
Cmars=2*pi*Rmars
K2=Cmars//Dmunt1

print("\nПериметр марса: ", round(Cmars,1))
print(int(K2), " -  1-евровых монет нужно положить рядом друг с другом, чтобы линия проходила вокруг Марса.")
"""

print("\n\n\nЮпитер - 69911\t\tМарс - 3389,5\t\tСатурн - 58232\t\tУран - 25362\nНептун - 24622\t\tВенера - 6051,8\t\tМеркурий - 2439,7\tЗемля - 6371")
Rplanet=float(input("\nВведи радиус любой планеты: "))
Cplanet=2*pi*Rplanet
print("Периметр твоей планеты: ", round(Cplanet,1))

print("\n\n\nМОНЕТА  -  ДИАМЕТР\n0.01  -  16.25\n0.02  -  18.75\n0.05  -  21.25\n0.1   -  19.75\n0.2   -  22.25\n0.5   -  24.25\n1    -  23.25\n2    -  25.75")
Dmunt=(float(input("\nВведи диаметр любой монеты: "))/1000000)
KK=Cplanet//Dmunt
print(int(KK), " - монет нужно положить рядом друг с другом, чтобы линия проходила вокруг Земли.")

# Ülesanne 3
# Eelnevaid teadmisi kasutades kirjuta programm, mis väljastaks:
# kill-koll kill-koll killadi-koll kill-koll kill-koll killadi-koll kill-koll kill-koll killkoll
# kill-koll

# Kas kasutasid muutujaid? Millistel juhtudel oleks muutujate kasutamine kindlasti otstarbekas?

print("\n\t*  Что на счет песенки? :)  *")


Ki="kill"
Ko="- koll  "
kil="killadi"
kk="killkoll  "
print()
print(Ki,Ko,Ki,Ko,kil,Ko,Ki,Ko,Ki,Ko,kil,Ko,Ki,Ko,Ki,Ko,kk,Ki,Ko)
#Будет легче вывести данную считалочку(фразу) без переменных, проще скопировать и просто вывести на экран

# Ülesanne 4
"""Koosta programm, mis väljastaks järgmised laulusõnad:

Rong see sõitis tsuhh tsuhh tsuhh,
piilupart oli rongijuht.
Rattad tegid rat tat taa,
rat tat taa ja tat tat taa.
Aga seal rongi peal,
kas sa tead, kes olid seal?

Kuidas lahendasid ülesande? Kas seda saaks teha kuidagi paremini? 
Kui lihtne oleks sellest programmist teha uus, kui
soovitakse hoopis järgmist laulu?

Rong see sõitis tuut tuut tuut,
piilupart oli rongijuht.
Rattad tegid kill koll koll,
kill koll koll ja kill koll kill.


....Sisend, väljund, tingimus....
"""

#Просто выводим текст пользователю
print("\n\t*  А вот и текст песни:  *")
print("\nRong see sõitis tsuhh tsuhh tsuhh,\npiilupart oli rongijuht.\nRattad tegid rat tat taa,\nrat tat taa ja tat tat taa.\nAga seal rongi peal,\nkas sa tead, kes olid seal?")

#Даем пользователю выбор, хочет ли он продолжить
kusimus=int(input("\n\t*  Показывать текст дальше?  *\n\t1 - Да\n\t0 - Нет \n"))
if kusimus==1:
    print("\nRong see sõitis tuut tuut tuut,\npiilupart oli rongijuht.\nRattad tegid kill koll koll,\nkill koll koll ja kill koll kill.")
else:
    print("Тогда идем дальше! :) ")
   




# Ülesanne 5
# Koosta programm, mis küsib kasutajalt ristküliku lähiskülgede pikkused ning väljastab 
# ekraanile ristküliku ümbermõõdu ja pindala.


#Пользователь вводит длину двух сторон. 
print("\n\t*  Посчитаем периметр и площадь прямоугольника!  *")
A=float(input("\nВведите длину стороны A: "))
B=float(input("\nВведите длину стороны B: "))

#Вычисляем по формулам периметр и площадь прямоугольника. 
P=2*(A+B)
S=A*B

#Выдаем ответ пользователю.
print("\nПлощадь прямоугольника: ", round(S, 1))
print("Периметр прямоугольника:  ", round(P, 1))

