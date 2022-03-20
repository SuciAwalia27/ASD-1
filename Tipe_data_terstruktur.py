#List[]

a=["Suci","Nahda","Uppa","Dewi"]

print(a)

print(type(a))

#Tuple(),

b=(25,5,2.5)

print(b)

print(type(b))

#Set{},

c={18,"Tahun",False,True}

print(c)

print(type(c))

#Dictionary{},

d={"Nama":"Suci",

"Umur":"18",

"Status":"Belum kawin"}

print(d)

print(type(d))

#Menampilkan List,Tuple,Set, Dictionary kedalam bentuk perulangan

List=["Suci","Nahda","Uppa","Dewi"]

Tuple=(25,5,2.5)

Set={18,"Tahun",False,True}

Dictionary={"Nama":"Suci",

"Umur":"18",

"Status":"Belum kawin"}

print(d)

print(type(d))

#Perulangan List

for data1 in List:

  print(List)

#Perulangan Tuple

for data2 in Tuple:

  print(Tuple)

#Perulangan Set

for data3 in Set:

  print(Set)

#Perulangan Dictionary

for data4 in Dictionary:

  print(data4, ":",Dictionary[data4])

#Mengupadate nilai dalam List

List=["Suci","Nahda","Uppa","Dewi"]

print(List)

List[0]="Akbar"

print(List)

#Menghapus nilai dalam List

List=["Suci","Nahda","Uppa","Dewi"]

print(List)

del List[0]

print(List)

#Menambahkan nilai dalam List

List=["Suci","Nahda","Uppa","Dewi"]

print(List)

List.append("Hilmi")

print(List)

#Karena tuple itu sifat nilainya tidak bisa diubah jadi dituple kita tidak bisa menambah dan mengupdate nilai kecuali menghapusnya

#Menghapus nilai dalam Tuple

Tuple=(25,5,2.5)

del Tuple

#Set ini adalah tipe data terstruktur yang nilainya acak,

#Set bersifat mutabel(bisa diubah) dalam artian bisa ditambah dan dikurangi (hapus) kecuali di-update

#Menghapus nilai dalam set

Set={18,"Tahun",False,True}

Set.discard("Tahun")

print(Set)

#Menambah nilai dalam set

Set.add("Bahagia")

print(Set)

#Mengupdate nilai dalam Dictionary

Dictionary={"Nama":"Suci",

"Umur":"18",

"Status":"Belum kawin"}

Dictionary["Status"]="Kawin"

print(Dictionary)

#Menghapus nilai dalam Dictionary

del Dictionary["Umur"]

print(Dictionary)

#Menambah nilai dalam Dictionary

Dictionary.update({"Pekerjaan":"Pelajar"})

print(Dictionary)
