print("Nama         :   Dedi Aldiansyah")
print("Kelas        :   TI.22.B2")
print("Nim          :   312210452")
print("Mata Kuliah  :   Bahasa Pemrograman")
print("===================================")


jumlah = int(input("Masukkan jumlah n :"))
import random
for i in range (jumlah):
    print("Data ke", i+1,"=",(random.uniform(0.1,0.5)))