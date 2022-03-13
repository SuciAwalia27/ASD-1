#Variabel adalah tempat menyimpan data

#tipe data ada 4 jenis

#(string,boolean,integer,dan float)

Nama ="suci awalia"#adalah tipe data string

Kelas = "informatika F"#adalah tipe data string

Nilai_bahasa = 7.5#adalah tipe float

Nilai_agama= 8#adalah tipe data integer

mahasiswa=True#adalah tipe data boolean

print("Nama saya   :"+Nama)

print("Kelas       :"+Kelas)

print("Nilai_bahasa:",Nilai_bahasa)

print("Nilai agama :",Nilai_agama)

if mahasiswa:

  print("saya adalah mahasiswa")

else:

  print("saya bukan mahasiswa")

 

#Operator aritmetika

#penjumlahan(+)

#pengurangan(-)

#perkalian(*)

#perpangkatan(**)

#pembgian(/)

#sisa bagi(%)

#pembagian bilangan bulat(//)

#Penjumlahan

NilaiA=4

NilaiB=8

Hasil= NilaiA + NilaiB

print(NilaiA,"+",NilaiB, "=",Hasil)

#Pengurangan

NilaiA=4

NilaiB=8

Hasil= NilaiA - NilaiB

print(NilaiA,"-",NilaiB, "=",Hasil)

#Perkalian

NilaiA=4

NilaiB=8

Hasil= NilaiA * NilaiB

print(NilaiA,"*",NilaiB, "=",Hasil)

#perpangkatan

NilaiA=4

NilaiB=8

Hasil= NilaiA ** NilaiB

print(NilaiA,"**",NilaiB,"=",Hasil)

#pembagian

NilaiA=4

NilaiB=8

Hasil= NilaiA / NilaiB

print(NilaiA,"/", NilaiB, "=",Hasil)

#sisa bagi

NilaiA=4

NilaiB=8

Hasil=NilaiA % NilaiB

print(NilaiA,"%",NilaiB, "=",Hasil)

#pembagian bilangan bulat

NilaiA=4

NilaiB=8

Hasil= NilaiA // NilaiB

print(NilaiA,"//", NilaiB,"=",Hasil)

#operator perbandingan

#sama dengan (==)

#tidak sama dengan(!=)

#lebih kecil atau sama dengan(<=)

#lebih besar atau sama dengan (>=)

#sama dengan

a= 5

b= 10

Hasil= a == b

print(a,"==",b,"=",Hasil)

#tidak sama dengan

a= 5

b= 10

Hasil= a != b

print(a,"!=",b,"=",Hasil)

#lebih besar atau sama dengan

a= 5

b= 10

Hasil= a >= b

print(a,">=",b,"=",Hasil)

#lebih kecil atau sama dengan

a= 5

b= 10

Hasil= a <= b

print(a,"<=",b,"=",Hasil)

#Operator logika

#not,or,and

#not adalah kebalikan dari data awal

b= True

c= not b

print("data c:",b)

b= False

c= not b

print("data c:",b)

#or jika salah satunya bernilai true maka hasilnya akan true

b=True

c=True

d=b or c

print(b,"or",c,"=",d)

b=True

c=False

d=b or c

print(b,"or",c,"=",d)

b=False

c=True

d=b or c

print(b,"or",c,"=",d)

b=False

c=False

d=b or c

print(b,"or",c,"=",d)

#and jika salah satunya bernilai false maka hasilnya akan false

b=True

c=True

d=b and c

print(b,"and",c,"=",d)

b=True

c=False

d=b and c

print(b,"and",c,"=",d)

b=False

c=True

d=b and c

print(b,"and",c,"=",d)

b=False

c=False

d=b and c

print(b,"and",c,"=",d)
