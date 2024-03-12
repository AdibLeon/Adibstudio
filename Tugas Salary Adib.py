def main():
    print("\n====================================")
    print("======== $ PROGRAM SALARY $ ========")
    print("====================================\n")
    
    nama_karyawan = input("Nama karyawan: ")
    gaji_pokok = float(input("Masukkan gaji pokok: "))
    jam_kerja = int(input("Masukkan Jam Kerja Harian: "))
    jumlah_hari_kerja_per_minggu = int(input("Masukkan hari kerja mingguan: "))

    print("\nNama karyawan:", nama_karyawan)
    print("Gaji pokok:", "Rp.",gaji_pokok)
    print("Jumlah jam kerja per hari:", jam_kerja,"Jam")
    print("Jumlah hari kerja per minggu:", jumlah_hari_kerja_per_minggu,"hari")
    print("\nPilih Rincian Gaji Mingguan/Harian:")
    print("1. Gaji Harian")
    print("2. Gaji Mingguan")
    pilihan = int(input("Pilih [1/2]: "))

    if pilihan == 1:
        gaji_harian = gaji_pokok / jam_kerja
        print("Gaji harian:", "Rp.",gaji_harian)
    elif pilihan == 2:
        gaji_mingguan = gaji_pokok / (jam_kerja * jumlah_hari_kerja_per_minggu)
        print("Gaji mingguan:", "Rp.",gaji_mingguan)
    else:
        print("Pilihan tidak valid.")

if __name__ == "__main__":
    main()