print("Nama         :   Dedi Aldiansyah")
print("Kelas        :   TI.22.B2")
print("Nim          :   312210452")
print("Mata Kuliah  :   Bahasa Pemrograman")
print("===================================")

x = int (input("Modal Awal :"))

a = 0*x
b = 0*x
c = 0.1*x
d = 0.1*x
e = 0.5*x
f = 0.5*x
g = 0.5*x
h = 0.2*x
y = [a,b,c,d,e,f,g,h]

for i in range (len(y)):
    print ("Laba bulan ke",i+1 ,"Sebesar :",y[i])

z = (a+b+c+d+e+f+g+h)
print("\nTotal laba selama 8 bulan : Rp.",z)