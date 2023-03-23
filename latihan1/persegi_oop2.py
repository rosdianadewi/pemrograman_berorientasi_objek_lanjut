class Persegi:
    def __init__(self):
        self.__panjang = None
        self.__lebar = None

    @property
    def panjang(self):
        return self.__panjang

    @panjang.setter
    def panjang(self, value):
        self.__panjang = value

    @property
    def lebar(self):
        return self.__lebar

    @lebar.setter
    def lebar(self, value):
        self.__lebar = value
               
    def Luas(self):
        L = self.__panjang * self.__lebar
        return L
    
    def Keliling(self):
        K = (2 * self.__panjang) + (2 * self.__lebar)
        return K
    
pj = float(input("Masukkan Nilai Panjang:"))
lb = float(input("Masukkan Nilai Lebar:"))
A = Persegi()
A.panjang = pj
A.lebar = lb
Luas = A.Luas()
Keliling = A.Keliling()
print("Luas adalah ",str(Luas))