#Clase animal

class Animal:
    def __init__(self,especie,nombre,color,patas):
        self.__especie = especie
        self.__nombre = nombre
        self.__color = color
        self.__patas = patas
    
    def get_especie(self):
        return self.__especie
    def get_nombre(self):
        return self.__nombre
    def get_color(self):
        return self.__color
    def get_patas(self):
        return self.__patas

    def caminar(self):
        print(f"Tu animal camina a {self.__patas} patas")
    
    def envenenar(self):
        es_Venenosa = (input("Tu araña es venenosa(si/no): "))
        if es_Venenosa == "si":
            print("Tu araña envenena. Ten cuidado!")
        elif es_Venenosa == "no":
            print("Tu araña no es venenosa")
        else:
            print("Elige una opción correcta")  

    def nombrar(self):
        print(f"el nombre de tu animal es:{self.__nombre}")






         
                 