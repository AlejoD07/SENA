#def suma(a,b):
 #   c=a+b
  #  print(c)
   # pass

#a=int(input("Digite un valor: "))
#b=int(input("Digite segundo valor: "))

#suma(a,b)
#def suma1(a,b):
   # c=d+f
  #  return c
 #   pass

#d=int(input("Digite un valor: "))
#f=int(input("Digite segundo valor: "))

#r=suma1(d,f)
#print(r)
#------------------------------------------
#cedula=int(input("Digite su cedula sin puntos ni espacios: "))
#nombre=str(input("digite su nombre completo: "))
#salario_basico=int(input("digite su salario basico: "))
#dias_labo=int(input("Digite los dias laborados: "))
#ventas=int(input("Digite el valor total de ventas: "))
#descuentos=int(input("Digite si tiene prestamos: "))
#aux_trans=117112*dias_labo/30
#def calculadora(cedula,nombre,salario_basico,dias_labo,ventas,descuentos,aux_trans):
    #if salario_basico<=2000000:
      #  salario=salario_basico+aux_trans
     #   sueldo=salario*dias_labo/30
    #else:
      #  sueldo=salario_basico*dias_labo/30
     #   print(sueldo)
    #comision=ventas*2/100
    #total_devengado=sueldo+comision
   # salario_neto=total_devengado-descuentos
  #  print(f"\nCedula empleado:{cedula},\nnombre de empleado:{nombre},\nSalario basico:{salario_basico},\nAuxilio de trasnporte:{aux_trans},\nComision de ventas:{comision},\nDescuentos:{descuentos}")
 #   print("el salario total es:",salario_neto)
#
#c=calculadora(cedula,nombre,salario_basico,dias_labo,ventas,descuentos,aux_trans)
#print(c)
#--------------------------------
#lista=["Danna","Alejandro","Andrea","Alvaro","Daniel","Alejandra","Huber","Sebastian","Lina","Laura"]
#def recorrido(lista):
    #while lista

numeros=[5,10,3,5,1,46,33,6,32,523,52,3,2,2423,5,2,15,2]
cadena=""
coma=","
for i in numeros:
    print(i)
cadena+=str(i)+coma
print(cadena)
def contador(lista):
    numeros.sort(reverse=True)
    print(numeros)
def buscar(numeros):
    buscar=input('Digite el valor a buscar: ')
    while numeros != "no":
        print(buscar)
 
print( contador(numeros), buscar(numeros))
