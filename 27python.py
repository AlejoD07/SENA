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

lista=("Danna","Alejandro","Andrea","Alvaro","Daniel","Alejandra","Huber","Sebastian","Lina","Laura")
def recorrido(lista):
    for i in lista:
     print(i)
print(recorrido(lista))
#def orden(lista):
 #   lista.sort(reverse=True)
  #  print(f"{lista}")
#print(orden(lista))
def buscar(lista):
    while lista != 'a':
        print('La letra no es la que busco')
        lista = input('introduce una letra ')
    print ('la letra es a, por eso salgo del bucle')
print(buscar(lista))
def longitud(lista):
    c=len(lista)
    print(c)
print(longitud(lista))
