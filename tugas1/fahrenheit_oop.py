class Fahrenheit:
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

def Celcius(F):
    C = 5/9 * (F - 32)
    return C


def Kelvin(F):
    K = 5/9 * (F - 32) + 273
    return K


def Reamur(F):
    R = 4/9 * (F - 32)
    return R


print("Konversi Suhu dari Fahrenheit")
print("==========================")
F = float(input("Masukkan suhu dalam Fahrenheit:"))
C = Celcius(F)
K = Kelvin(F)
R = Reamur(F)
print("Fahrenheit=", str(F))
print("--------------")
print("Konversi ke Celcius = ", C)
print("Konversi ke Kelvin =", K)
print("Konversi ke Reamur=", R)