class Kelvin:
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

def Celcius(K):
    C = K - 273
    return C


def Reamur(K):
    R = 4/5 * (K - 273)
    return R


def Fahrenheit(K):
    F = 9/5 * (K - 273) + 32
    return F


print("Konversi Suhu dari Kelvin")
print("==========================")
K = float(input("Masukkan suhu dalam Kelvin:"))
C = Celcius(K)
R = Reamur(K)
F = Fahrenheit(K)
print("Kelvin =", str(K))
print("--------------")
print("Konversi ke Celcius = ", C)
print("Konversi ke Reamur =", R)
print("Konversi ke Fahrenheit =", F)