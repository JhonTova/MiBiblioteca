from os import system
import datetime
Libro1 = []
Libro2 = []
Libro3 = []
FechaPrestamo = []
class usuario:
    def __init__(self, nombre = 0, apellido= 0, cedula= 0, telefono= 0):
        self._nombre = nombre
        self._apellido = apellido
        self._cedula = cedula
        self._telefono = telefono
    def set_nombre(self, nombre):
        self._nombre = nombre
    def get_nombre(self):
        return self._nombre
    def set_apellido(self, apellido):
        self._apellido = apellido
    def get_apellido(self):
        return self._apellido
    def set_cedula(self, cedula):
        self._cedula = cedula
    def get_cedula(self):
        return self._cedula
    def set_telefono(self, telefono):
        self.telefono = telefono
    def get_telefono(self):
        return self._telefono
class libros:
    def Menulibros(self):
        print("1 = Ver libro 1 >>> ")
        print("2 = Ver libro 2 >>> ")
        print("3 = Ver libro 3 >>> ")
        desicion = int(input("Digite su desicion <<< "))
        if desicion == 1:
            self.libro1()
        if desicion == 2:
            self.libro2()
        if desicion == 3:
            self.libro3()
    def libro1(self):
        Menu=[
            ["Titulo : Introducion a java"],
            ["3A. Edicion"],
            ["Autor: Liang, Y. Daniel"],
            ["ISBN: 0-13-0434323-X"],
            ["Prentice-Hall, New jersey USA, Viernes 18 noviembre 2001"],
            ["784 Paginas"] 
        ]
        for x in range(6):
            print(Menu[x][0])
        self.__init__()
    def libro2(self):
        Menu=[
            ["Titulo : Introducion a java"],
            ["3A. Edicion"],
            ["Autor: Liang, Y. Daniel"],
            ["ISBN: 0-13-0434323-X"],
            ["Prentice-Hall, New jersey USA, Viernes 18 noviembre 2001"],
            ["785 Paginas"] 
        ]
        for x in range(6):
            print(Menu[x][0])
        self.__init__()
    def libro3(self):
        Menu=[
            ["Titulo : Introducion a java"],
            ["3A. Edicion"],
            ["Autor: Liang, Y. Daniel"],
            ["ISBN: 0-13-0434323-X"],
            ["Prentice-Hall, New jersey USA, Viernes 18 noviembre 2001"],
            ["786 Paginas"] 
        ]
        for x in range(6):
            print(Menu[x][0])
        self.__init__()
class Main(usuario,libros):
    def __init__(self):
        super(Main,self).__init__()
        print("Bienvenido a la biblioteca >>> ")
        print("1 = Ver libreria >>> ")
        print("2 = Prestar libro >>> ")
        print("3 = Regresar libro >>> ")
        print("4 = Salir >>> ")
        desicion = int(input("Digite su desicion <<< "))
        if desicion == 1:
            super(Main,self).Menulibros()
        if desicion == 2:
            Biblioteca = usuario()
            Biblioteca.set_nombre(input("Digite su nombre <<< "))
            Biblioteca.set_apellido(input("Digite su apellido <<< "))
            Biblioteca.set_cedula(input("Digite su cedula <<< "))
            Biblioteca.set_telefono(input("Digite su numero de telefono <<< "))
            system("cls")
            print("1 = Libro 1 >>> ")
            print("2 = Libro 2 >>> ")
            print("3 = Libro 3 >>> ")
            desicion = int(input(("Que libro deseas pedir prestado >>> ")))
            if desicion == 1:
                if 1 in Libro1:
                    print("Libro no disponible >>> ")
                    self.__init__()
                else:
                    print("Libro #1 Prestado con exito >>> ")
                    print("Prestado a : ", (Biblioteca.get_nombre()), (Biblioteca.get_apellido()))
                    print("Numero de ID :", (Biblioteca.get_cedula()))
                    Fecha = datetime.datetime.now()
                    FechaPrestamo2 = datetime.datetime.strftime(Fecha, "%d/%m/%Y")
                    FechaPrestamo.append(FechaPrestamo2)
                    print("Dia prestado :",datetime.datetime.strftime(Fecha, "%d/%m/%Y"), "Hora :", datetime.datetime.strftime(Fecha, "%H:%M:%S"))
                    Libro1.append(1)
                    self.__init__()
            if desicion == 2:
                if 1 in Libro2:
                    print("Libro no disponible >>> ")
                    self.__init__()
                else:
                    print("Libro #2 Prestado con exito >>> ")
                    print("Prestado a : ", (Biblioteca.get_nombre()), (Biblioteca.get_apellido()))
                    print("Numero de ID :", (Biblioteca.get_cedula()))
                    Fecha = datetime.datetime.now()
                    FechaPrestamo2 = datetime.datetime.strftime(Fecha, "%d/%m/%Y")
                    FechaPrestamo.append(FechaPrestamo2)
                    print("Dia prestado :",datetime.datetime.strftime(Fecha, "%d/%m/%Y"), "Hora :", datetime.datetime.strftime(Fecha, "%H:%M:%S"))
                    Libro2.append(1)
                    self.__init__()
            if desicion == 3:
                if 1 in Libro3:
                    print("Libro no disponible >>> ")
                    self.__init__()
                else:
                    print("Libro #3 Prestado con exito >>> ")
                    print("Prestado a : ", (Biblioteca.get_nombre()), (Biblioteca.get_apellido()))
                    print("Numero de ID :", (Biblioteca.get_cedula()))
                    Fecha = datetime.datetime.now()
                    FechaPrestamo2 = datetime.datetime.strftime(Fecha, "%d/%m/%Y")
                    FechaPrestamo.append(FechaPrestamo2)
                    print("Dia prestado :",datetime.datetime.strftime(Fecha, "%d/%m/%Y"), "Hora :", datetime.datetime.strftime(Fecha, "%H:%M:%S"))
                    Libro3.append(1)
                    self.__init__()
        if desicion == 3:
            print("Bienvenido >>> ")
            print("1 = Libro 1 >>> ")
            print("2 = Libro 2 >>> ")
            print("3 = Libro 3 >>> ")
            desicion = int(input("Digite que libro desea regresar <<< "))
            Biblioteca = usuario()
            Biblioteca.set_nombre(input("Digite su nombre <<< "))
            Biblioteca.set_apellido(input("Digite su apellido <<< "))
            Biblioteca.set_cedula(input("Digite su cedula <<< "))
            Biblioteca.set_telefono(input("Digite su numero de telefono <<< "))
            if desicion == 1 :
                if 1 in Libro1:
                    system("cls")
                    print("Gracias por regresar el libro >>> ")
                    Fecha = datetime.datetime.now()
                    print("Prestado a : ", (Biblioteca.get_nombre()), (Biblioteca.get_apellido()))
                    print("Numero de ID :", (Biblioteca.get_cedula()))
                    print("Fecha prestado :",FechaPrestamo)
                    print("Dia regresado :",datetime.datetime.strftime(Fecha, "%d/%m/%Y"), "Hora :", datetime.datetime.strftime(Fecha, "%H:%M:%S"))
                    Libro1.clear()
                    self.__init__()
                else:
                    print("Libro no prestado, debes prestarlo para poder regresarlo")
                    self.__init__()
            if desicion == 2 :
                if 1 in Libro2:
                    system("cls")
                    print("Gracias por regresar el libro >>> ")
                    Fecha = datetime.datetime.now()
                    print("Prestado a : ", (Biblioteca.get_nombre()), (Biblioteca.get_apellido()))
                    print("Numero de ID :", (Biblioteca.get_cedula()))
                    print("Fecha prestado :",FechaPrestamo)
                    print("Dia regresado :",datetime.datetime.strftime(Fecha, "%d/%m/%Y"), "Hora :", datetime.datetime.strftime(Fecha, "%H:%M:%S"))
                    Libro2.clear()
                    self.__init__()
                else:
                    print("Libro no prestado, debes prestarlo para poder regresarlo")
                    self.__init__()
            if desicion == 3 :
                if 1 in Libro3:
                    system("cls")
                    print("Gracias por regresar el libro >>> ")
                    Fecha = datetime.datetime.now()
                    print("Prestado a : ", (Biblioteca.get_nombre()), (Biblioteca.get_apellido()))
                    print("Numero de ID :", (Biblioteca.get_cedula()))
                    print("Fecha prestado :",FechaPrestamo)
                    print("Dia regresado :",datetime.datetime.strftime(Fecha, "%d/%m/%Y"), "Hora :", datetime.datetime.strftime(Fecha, "%H:%M:%S"))
                    Libro3.clear()
                    self.__init__()
                else:
                    print("Libro no prestado, debes prestarlo para poder regresarlo")
                    self.__init__()
        if desicion == 4:
            print("Adios... >>> ")
            exit()
Biblioteca = Main()