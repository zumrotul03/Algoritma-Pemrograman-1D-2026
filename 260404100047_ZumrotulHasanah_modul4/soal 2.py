total_gaji = 0
for hari in range(1, 8):
    print("Hari ke-hari")
    gaji_pokok = 100000
    lembur = int(input("Masukkan jam lembur: "))
    while lembur < 0 or (lembur > 4 and lembur != 6 and lembur != 8 and lembur <= 8):
        print("Jam lembur tidak sesuai ketentuan!")
        lembur = int(input("Masukkan ulang jam lembur: "))
    if lembur > 8:
        print("Jam lembur melebihi batas yang ditentukan!")
        upah_lembur = 0
    elif lembur == 0:
        upah_lembur = 0
    elif lembur >= 1 and lembur <= 3:
        upah_lembur = lembur * 25000
    elif lembur == 4:
        upah_lembur = 100000
    elif lembur == 6:
        upah_lembur = 200000
    elif lembur == 8:
        upah_lembur = 300000
    shift = input("Bekerja shift malam? (ya/tidak): ")
    if shift == "ya" or "iya":
        tambahan_shift = 50000
    else:
        tambahan_shift = 0
    gaji_harian = gaji_pokok + upah_lembur + tambahan_shift
    total_gaji += gaji_harian
    print("Gaji hari ke-hari: Rp gaji_harian")
print("Total gaji mingguan: Rp total_gaji")
