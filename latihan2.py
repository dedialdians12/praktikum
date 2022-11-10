print("Nama         :   Dedi Aldiansyah")
print("Kelas        :   TI.22.B2")
print("Nim          :   312210452")
print("Mata Kuliah  :   Bahasa Pemrograman")
print("===================================")

big = 0
while True:
    a = int(input("Masukkan bilangan : "))
    if big < a:
        big = a
    if a ==0:
            break
print("\n Bilangan terbesar adalah : ",big)