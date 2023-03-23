class Persegi:
    @staticmethod
    def Luas( panjang, lebar):
        L = panjang * lebar
        return L
    
    @staticmethod
    def Keliling( panjang, lebar):
        K = (2 * panjang) + (2 * lebar)
        return K
    
pj = int(input("Masukkan Nilai Panjang:"))
lb = int(input("Masukkan Nilai Lebar:"))
L = Persegi.Luas(pj,lb)
print("Luas adalah ",str(L))