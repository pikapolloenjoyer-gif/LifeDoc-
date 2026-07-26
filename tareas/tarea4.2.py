
#Tarea4.2:Realizar un programa que valide si un usuario puso las credenciales correctas darle tres oportunidades.



#La credencial
contraseña1 = input("Ingrese una contraseña: ")
contraseña2 = input("Confirme su contraseña: ")

#Condiciones para validación
if contraseña2 != contraseña1:
    print("La contraseña es incorrecta, intente de nuevo")
    contraseña2 = input("Confirme su contraseña: ")

if contraseña2 != contraseña1:
    print("La contraseña es incorrecta, intente de nuevo")
    contraseña2 = input("Confirme su contraseña: ")

if contraseña2 != contraseña1:
    print("La contraseña es incorrecta, no tienes más intentos impostor")

elif contraseña2 == contraseña1:
    print("La contraseña es correcta :)")
                


