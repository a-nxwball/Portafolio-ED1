"""
Taller1: {Ana, Luis, Carlos, Marta}
Taller2: {Ana, Carlos, Jorge, Pedro}
Taller3: {Luis, Marta, Pedro, Ana}
Taller4: {Carlos, Jorge, Marta, Ana}
Objetivos
1. Participantes en todos los talleres:
    Encuentra el conjunto de participantes que asistio a todos los talleres
2. Participante en al menos dos talleres:
    Encuentra el conjunto de participantes que asistio a al menos dos talleres
3. Participantes Unicos (Solo en un taller):
    Encuentra el conjunto de Participantes a solo un taller
4. Particpantes que Asistieron a un taller especifico (Taller 2):
    Encuentra el conjunto de participantes que asistio al taller 2 pero no a los otros talleres
"""
taller1 = {"Ana", "Luis", "Carlos", "Marta"}
taller2 = {"Ana", "Carlos", "Jorge", "Pedro"}
taller3 = {"Luis", "Marta", "Pedro", "Ana"}
taller4 = {"Carlos", "Jorge", "Marta", "Ana"}



#1. Participantes en todos los talleres:
#Encuentra el conjunto de participantes que asistio a todos los talleres
todos_los_talleres = taller1 & taller2 & taller3 & taller4
print("EN TODOS LOS TALLERES: ", todos_los_talleres)

#2. Participante en al menos dos talleres:
#Encuentra el conjunto de participantes que asistio a al menos dos talleres
al_menos_dos_talleres = taller2 | taller1 | taller3 | taller4
print(type(al_menos_dos_talleres))
print("EN AL MENOS DOS TALLERES: ", al_menos_dos_talleres)

#3. UN SOLO TALLER
Un_solo_taller = taller2 - taller1 - taller3 - taller4

if Un_solo_taller == set():
    print("Ningun participante asistio solo a un taller.")
else:
    print("ASISTIO A UN SOLO TALLER", Un_solo_taller)

#4. Asistio al taller 2 pero no los otros
Solo_al_dos = taller2 - taller1 - taller3 - taller4
if Un_solo_taller == set():
    print("Ningun participante asistio solo al taller 2.")
else: 
    print("ASISTIO AL TALLER 2 PERO NO A LOS OTROS: ", Solo_al_dos)