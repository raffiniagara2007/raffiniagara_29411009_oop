from produk import Produk

for i in range (2):
    nama = input("Nama produk : ")
    harga = int(input("Harga : "))
    jumlah = int(input("Jumlah : "))

    produk = Produk(nama, harga)

    produk .tampilkan_info()
    total = produk.hitung_total(jumlah)

    print("Total:, total")
    print()