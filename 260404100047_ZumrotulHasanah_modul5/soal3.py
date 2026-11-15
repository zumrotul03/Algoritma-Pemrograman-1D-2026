def nilai_mahasiswa(nama, tugas, uts, uas):
    akhir = (tugas * 0.3) + (uts * 0.3) + (uas * 0.4)

    if akhir >= 85:
        grade = "A"
    elif akhir >= 70:
        grade = "B"
    elif akhir >= 55:
        grade = "C"
    else:
        grade = "D"

    if grade == "D":
        status = "Tidak Lulus"
    else:
        status = "Lulus"

    return akhir, grade, status


nama = input("Masukkan nama mahasiswa: ")
tugas = float(input("Masukkan nilai tugas: "))
uts = float(input("Masukkan nilai UTS: "))
uas = float(input("Masukkan nilai UAS: "))

akhir, grade, status = nilai_mahasiswa(nama, tugas, uts, uas)

print("\nNama:", nama)
print("Nilai Akhir:", akhir)
print("Grade:", grade)
print("Status:", status)