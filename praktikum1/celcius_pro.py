#KONVERSI CELCIUS KE FAHRENHEIT
class Celcius:
    @staticmethod
    def to_fahrenheit(celsius):
        return (celsius * 9/5) + 32
    @staticmethod
    def to_kelvin(celsius):
        return celsius + 273.15
    @staticmethod
    def to_reamur(celsius):
        return celsius * 4/5
mycelcius = 75
myfahrenheit = Celcius.to_fahrenheit(mycelcius)
print(myfahrenheit)
mycelcius = 60
myreamur = Celcius.to_reamur(mycelcius)
print(myreamur)
mycelcius = 90
mykelvin = Celcius.to_kelvin(mycelcius)
print(mykelvin)