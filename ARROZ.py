from multiprocessing.sharedctypes import Value
import operator
meses= dict(
    enero=126,
    febrero=324,
    marzo=345,
    abril=745,
    mayo=134,
    junio=135,
    julio=647,
    agosto=472,
    septiembre=247,
    octubre=357,
    noviembre=846,
    diciembre=853
)
max_key= max(meses.items(), key=operator.itemgetter(1))[0]
print("la maxima produccion de arroz fue en el mes de:", max_key)
min_key=min(meses.items(), key=operator.itemgetter(1))[0]
print("la minima produccion de arroz fue en el mes de:", min_key)
d=tuple(meses.values())
c=len(d)
suma=0
for pro in d:
    suma+=pro
    a=suma/c
print("el promedio de la produccion fue:", a)

for key in meses.keys():
    if (meses[key]>=pro):
        print("el mes", key,"es mayor que el promedio")
    
    elif (meses[key]<=pro):
        print(f"el mes: {key}, es menor que el promedio")