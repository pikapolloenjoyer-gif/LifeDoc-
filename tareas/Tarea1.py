#Realizar un progama que me pregunte 5 cosas que me gusten y mostrar esa información

#Pido la información
info= input("Escribe 5 cosas que te gusten: ")
#Muestro info
print(info)


#Realizar un programa que me pregunte y nombre y haga una presentacion con mi nombre presentarlo.

#Pregunto el nombre
nombre = input("Cual es tu nombre? ")
#Muestro el nombre
print("Mucho gusto ",nombre)     
    
#Realizar un programa que muestre una cedula  hecha con caracteres(sea creativo).
   
#Escribo los número hasta el primer guión

primerg = "402-"

#Escribo los número hasta el segundo guión

segundog ="4971144-"

#Escribo los número restantes

tercerg ="7"

#Muestro el resultado

print(primerg ,segundog,tercerg)


#Realizar un programa que pida 5 informacion y con eso haga una historia.

#Pido las info

info1 = input("Cual es tu nombre? ")
info2 = input("¿Cual es tu nacionalidad? ")
info3 = input("Donde vives? ")
info4 = input("Cuantos años tienes? ")  
info5 = input("Cómo se llama tu madre? ")  
            
#Hago la historia y la muestra en pantalla

print(info1, end= ' ')                
print("nace en", info2, end=' ')    
print("crece y vive en los multis,", info3, end= ' ')   
print("Con", info4, end= ' ')         
print("se apunta al curso de python basico del ITLA, y cuando sale del curso su madre",info5, end= ' ')
print("Lo viene a buscar") 
