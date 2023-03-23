class Persegi:
    def __init__(self, panjang, lebar):
        self.panjang = panjang
        self.lebar = lebar
    
    def Luas(self):
        L = self.panjang * self.lebar
        return L
    
    def Keliling(self):
        K = (2 * self.panjang) + (2 * self.lebar)
        return K
    
pj = float(input("Masukkan Nilai Panjang:"))
lb = float(input("Masukkan Nilai Lebar:"))
A = Persegi(pj,lb)
Luas = A.Luas()
Keliling = A.Keliling()
print("Luas adalah ",str(Luas))