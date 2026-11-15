anggota = []

while True:
    nama = input("Masukkan nama: ")

    if nama == "selesai":
        break

    anggota.append(nama)

for nama in anggota:
    if nama == "admin" or len(nama) == 4 or len(nama) == 8 :
        print(nama, " Valid")
    elif nama == "admin":
        print(nama, "valid")
    else:
        print(nama, " tidak Valid")

hapus = input("Nama yang ingin dihapus: ")

if hapus in anggota:
    anggota.remove(hapus)
else:
    print("Nama tidak ditemukan")

print(anggota)