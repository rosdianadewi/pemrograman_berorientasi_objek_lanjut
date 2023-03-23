class Reamur:
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

def Celcius(R):
    C = 5/4 * R
    return C


def Kelvin(R):
    K = (5/4 * R) + 273
    return K


def Fahrenheit(R):
    F = (9/4 * R) + 32
    return F


print("Konversi Suhu dari Reamur")
print("==========================")
R = float(input("Masukkan suhu dalam Reamur:"))
C = Celcius(R)
K = Kelvin(R)
F = Fahrenheit(R)
print("Reamur =", str(R))
print("--------------")
print("Konversi ke Celcius = ", C)
print("Konversi ke Kelvin =", K)
print("Konversi ke Fahrenheit =", F)