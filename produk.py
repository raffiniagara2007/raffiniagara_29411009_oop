class Produk:

    def __init__(self, nama, harga):
        self.nama = nama
        self.harga = harga

    def tampilkan_info(self):
        print(f"Nama Produk: {self.nama} | Harga: Rp{self.harga}")

    def hitung_total(self, jumlah):
        total = self.harga * jumlah
        print(f"Total harga {self.nama} ({jumlah} buah): Rp{total}")



produk1 = Produk("Keyboard", 250000)
produk2 = Produk("Mouse", 150000)


produk1.tampilkan_info()
produk2.tampilkan_info()


produk1.hitung_total(2)
produk2.hitung_total(3)