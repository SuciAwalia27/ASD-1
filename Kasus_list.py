barang=[]

perintah=0

while perintah != 7:

  print('''1. Menambah list
2. Menghapus list
3. Mengedit list
4. Menampilkan list
5. Mencari barang
6. Mencari index tertentu
7. Tutup''')
  perintah=int(input("Masukkan perintah:"))

# menambah
  if perintah == 1:
    	while True:
    		tambah=input("masukkan barang:")
    		barang.append(tambah)
    		
    		lanjut=input("apakah dilanjut?:")
    		if lanjut == "n":
    			break

# menghapus
  elif perintah == 2:
   		while True:
   			hapus=int(input("masukkan index barang yang ingin dihapus:"))
   			
   			barang.pop(hapus)
   			
   			lanjut=input("apakah dilanjut?:")
   			if lanjut == "n":
   				break

# mengedit
  elif perintah == 3:
    	while True:
    		ganti= int(input("masukkan index yang ingin diedit:"))
    		
    		barang [ganti]=input("masukkan barang baru:")
    		
    		lanjut=input("apakah dilanjut?:")
    		if lanjut == "n":
    			break

# menampilkan
  elif perintah == 4:
   		for i in range(len(barang)):
   			print(barang[i])

# mencari barang
  elif perintah == 5:
   	cari=input("barang yang dicari:")
   	
   	for i in range(len(barang)):
   			if barang [i] == cari:
   				print("barang ditemukan!")
   			else:
   				print("barang tidak ditemukan")

# mencari index
  elif perintah == 6:
   	cari2=input("masukkan barang yang dicari:")
   	
   	if cari2 in barang:
   	   print(barang.index(cari2))
   	else:
   		print("index tidak ditemukan")
