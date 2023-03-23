class Celcius:
    def __init__(self):
        self.__celcius = None
        self.__fahrenheit = None
        self.__reamur = None
        self.__kelvin = None

    @property
    def celcius(self):
        return self.__celcius

    @celcius.setter
    def celcius(self, value):
        self.__celcius = value

    @property
    def fahrenheit(self):
        return self.__fahrenheit

    @fahrenheit.setter
    def fahrenheit(self, value):
        self.__fahrenheit = value
    @property
    def reamur(self):
        return self.__reamur

    @reamur.setter
    def reamur(self, value):
        self.__reamur = value

    @property
    def kelvin(self):
        return self.__kelvin

    @kelvin.setter
    def kelvin(self, value):
        self.__kelvin = value

def Fahrenheit(C):
    F = (9/5*C)+32
    return F


def Kelvin(C):
    K = C + 273
    return K


def Reamur(C):
    R = 4/5 * C
    return R


print("Konversi Suhu dari Celcius")
print("==========================")
C = float(input("Masukkan suhu dalam Celcius:"))
F = Fahrenheit(C)
K = Kelvin(C)
R = Reamur(C)
print("Celcius=", str(C))
print("--------------")
print("Konversi ke Fahrenheit = ", F)
print("Konversi ke Kelvin =", K)
print("Konversi ke Reamur=", R)