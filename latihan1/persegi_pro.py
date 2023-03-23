class Persegi:
    def Luas(self, panjang, lebar):
        L = panjang * lebar
        return L
    
    def Keliling(self, panjang, lebar):
        K = (2 * panjang) + (2 * lebar)
        return K
    
A = Persegi()
pj = int(input("Masukkan Nilai Panjang:"))
lb = int(input("Masukkan Nilai Lebar:"))
Luas = A.Luas(pj,lb)
print("Luas adalah ",str(Luas))