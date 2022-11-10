Latihan 1

Menampilkan n bilangan acak yang lebih kecil dari 0.5.

Bila di implementasikan dengan bahasa Python. program dapat digambarkan seperti dibawah ini.

![image](https://user-images.githubusercontent.com/48305171/201068313-fdecff4f-4f94-41a3-a9f2-7a0eda818d3e.png)

A. Langkah-langkah

Selanjutnya saya akan mengurutkan langkah-langkah atau algoritmanya.

![image](https://user-images.githubusercontent.com/48305171/201068447-4317b787-618c-44de-af16-5652cdac6c92.png)

```
jumlah = int(input("Masukkan jumlah n :"))
import random
for i in range (jumlah):
    print("Data ke", i+1,"=",(random.uniform(0.1,0.5)))
```

Hasil

![image](https://user-images.githubusercontent.com/48305171/201068654-6bb10400-9a69-4203-b11e-39cc1c7e2ab0.png)

Masukkan nilai (n) : 4

Program akan mencetak data ke 1 sampai 5 dengan nilai kurang dari 0.5

B. Penjelasan

1. jumlah=int(input("Masukkan jumlah n")) Untuk menentukan jumlah input yang di inginkan sesuai tipe data, yaitu interger tipe data bilangan bulat.

2. import random

3. for i in range (jumlah): Untuk pengulangan dengan range jumlah.

4. print("Data ke",1+i"=",(random.uniform(0.1,0.5))) Untuk menampilkan atau mencetak urutan data sesai jumlah inputan dengan hasil dibawah 0.5.

Latihan 2

Menampilkan bilangan terbesar dari n buah data yang diinputkan dan masukkan angka 0 untuk berhenti.

Bila disimpulkan program di atas dapat digambarkan sebagai berikut.

![image](https://user-images.githubusercontent.com/48305171/201070272-3241595c-8b88-4105-9e9f-98d81ff498a3.png)

Langkah-langkah
Selanjutnya saya akan mengurutkan algoritma atau langkah-langkahnya. Perhatikan program berikut.

![image](https://user-images.githubusercontent.com/48305171/201070666-695c5f05-1bcc-453f-baf5-ea809f1eaa89.png)

```
big = 0
while True:
    a = int(input("Masukkan bilangan : "))
    if big < a:
        big = a
    if a ==0:
            break
print("\n Bilangan terbesar adalah : ",big)
```

Hasil

![image](https://user-images.githubusercontent.com/48305171/201070882-cda90ba5-6ebc-433a-9081-460697e5db63.png)

Penjelasan

1. print ('Menampilkan Bilangan Terbesar Dari N Buah Data Yang Diinputkan') Untuk menampilkan kalimat Menampilkan Bilangan Terbesar Dari N Buah Data Yang Diinputkan

2. max= 0 kode max disini untuk menentukan nilai max nya dalah 0

3. while true: Untuk perulangan hingga waktu yang tidak di tentukan atau selamanya

4. a=int(input("Masukan Bilangan :")) a untuk menginput tipe data interger ( bilangan bulat )

5. if max < a max=a jika max kurang dari a maka max = a

6. if a==0: break jika a= 0 maka akan berhenti dengan syarat break yang terpenuhi

7. print("Bilangan Tebesar Adalah :", max) Menampilkan *Bilangan Tebesar Adalah : Nilai maxiumnya.

Program 1

Menghitung Jumlah Laba Hasil Investasi Seorang Pengusaha Selama 8 Bulan.

Soal

Seorang pengusaha menginvestasikan uangnya untuk memulai usahanya dengan modal awal 100 juta, pada bulan pertama dan kedua belum mendapatkan laba. pada bulan ketiga baru mulai mendapatkan laba sebesar 1% dan pada bulan ke 5, pendapatan meningkat 5%, selanjutnya pada bulan ke 8 mengalami penurunan keuntungan sebesar 2%, sehingga laba menjadi 3%. Hitung total keuntungan selama 8 bulan berjalan usahanya.

Contoh program dengan bahasa Python.

![image](https://user-images.githubusercontent.com/48305171/201072045-d5aff289-18bf-4121-9094-677ef0de8203.png)

A. Langkah-langkah
untuk lebih jelasnya lagi coba simak gambar dibawah ini.

![image](https://user-images.githubusercontent.com/48305171/201072168-4896db0c-eb85-403e-86dc-c1670a0c4274.png)

```
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
```

Hasil

![image](https://user-images.githubusercontent.com/48305171/201072353-380e74e8-3ec8-41b3-bb36-f81c01e6f993.png)

B. Penjelasan

print ('Jumlah Laba Hasil Investasi Seorang Pengusaha Selama 8 Bulan') Untuk Menampilkan kalimat Jumlah Laba Hasil Investasi Seorang Pengusaha Selama 8 Bulan

x=100000000 Dengan pemisalan atau dideklarasikan x adalah 100000000

print (" Modal Awal:",x) Menampilkan kalimat Modal Awal : dan data yang berisi di x yaitu 100000000

a=0x, b=0x, c=0.01x, d=0.01x, e=0.05x, f=0.05x, g=0.05x, h=0.03x Untuk Mendeklarasikan presentase laba tiap bulan dan di kali dengan x atau data inputan modal investasi yaitu 100000000

y=[a,b,c,d,e,f,g,h] untuk menentukan syarat y= yang berisi a,b,c,d,e,f,g,h

For i in range (len (y)) Print (“laba bulan ke-“,i+1,”sebesar:” ,y[i]) untuk perulangan data dengan isi data yaitu Ydengan menampilkan urutan laba perbulan sesuai range yang di tentukan dengan hasil ke untukan yang di inpput dari data Y

Z= (a+b+c+d+e+f+g+h) Print (“jumlah laba selama 8 bulan adalah:”) Z berisi data penjumlahan data angka yang ada didalam kode a,b,c,d,e,f,g,h yang akan di tampilakan atau dicetak di jumlah laba selama 8 bulan
