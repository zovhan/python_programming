jumlah_pembeli = int(input("masukkan jumlah pembeli tiket: "))
for i in range(jumlah_pembeli):
    print("pembeli {i+1}")

    harga_anak = 30000
    harga_dewasa = 50000
    harga_lansia = 35000

    usia = int(input("masukkan usia pembeli: "))
    jumlah_tiket = int(input("masukkan jumlah tiket yang anda ingin beli: "))

    if usia < 12:
        harga_tiket = harga_anak
    elif 12 <= usia <= 60:
        harga_tiket = harga_dewasa
    else:
        harga_tiket = harga_lansia
    total_per_pembeli = harga_tiket =jumlah_tiket
    print(f"harga untuk pembeli {i+11}Rp {total_per_pembeli}") 
    harga_tiket += total_per_pembeli
    print(f"total harga untuk semua tiket yang dibeli: Rp {harga_tiket}")


