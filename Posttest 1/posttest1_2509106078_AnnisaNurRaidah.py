class AlatMusik:
    nama_toko = "Hearts Melodi"
    total_alat = 0

    def __init__(self, id_produk, nama_alat, harga_alat, stok):
        self.id_produk = id_produk
        self.nama = nama_alat
        self.harga = harga_alat
        self.__stok = stok
        AlatMusik.total_alat += 1

    @property
    def stok(self):
        return self.__stok
    
    @stok.setter
    def stok(self, stok_baru):
        if stok_baru < 0:
            print("Stok Tidak Boleh Minus!\n")
        else:
            self.__stok = stok_baru

    def kurangi_stok(self, jumlah):
        if jumlah <= 0:
            print("Jumlah Stok Harus Lebih Dari 0\n")
        elif jumlah > self.__stok:
            print("Stok", self.nama, "Melebihi Jumlah Tersedia\n")
        else:
            self.__stok -= jumlah
            print("Stok", self.nama, "Berkurang, Stok Tersedia:", self.__stok, "\n")

    def tambah_stok(self, jumlah):
        if jumlah <= 0:
            print("Jumlah Stok Harus Lebih Dari 0\n")
        else:
            self.__stok += jumlah
            print("Stok", self.nama, "Bertambah, Stok Tersedia:", self.__stok, "\n")

    @classmethod
    def ubah_nama_toko(cls, nama_baru):
        cls.nama_toko = nama_baru
        print("Nama Toko Berubah Menjadi:", cls.nama_toko, "\n")

    def info(self):
        print("----------------------------------")
        print("         INFORMASI PRODUK         ")
        print("----------------------------------")
        print("ID Produk        :", self.id_produk)
        print("Nama Alat        :", self.nama)
        print("Harga            : Rp", self.harga)
        print("Stok             :", self.__stok, "\n")

class Pembeli:
    total_pembeli = 0

    def __init__(self, id_pembeli, nama, no_telp):
        self.id_pembeli = id_pembeli
        self.nama = nama
        self.__no_hp = no_telp
        Pembeli.total_pembeli += 1

    @property
    def no_hp(self):
        return self.__no_hp

    @no_hp.setter
    def no_hp(self, no_telp_baru):
        if len(no_telp_baru) < 11:
            print("Nomor Telepon Minimal 11 Digit!\n")
        else:
            self.__no_hp = no_telp_baru

class Transaksi:
    total_transaksi = 0

    def __init__(self, id_transaksi, tanggal, pembeli, alat, jumlah, uang_bayar):
        self.id_transaksi = id_transaksi
        self.tanggal = tanggal
        self.pembeli = pembeli
        self.alat = alat
        self.jumlah = jumlah
        self.total_harga = Transaksi.hitung_total(alat.harga, jumlah)
        self.uang_bayar = uang_bayar 
        self.kembalian = uang_bayar - self.total_harga
        Transaksi.total_transaksi += 1

    def cetak_struk(self):
        print("----------------------------------")
        print("         STRUK PEMBELIAN          ")
        print("----------------------------------")
        print("ID Transaksi :", self.id_transaksi)
        print("Tanggal      :", self.tanggal)
        print("Pembeli      :", self.pembeli.nama)
        print("No. HP       :", self.pembeli.no_hp)
        print("Barang       :", self.alat.nama, "x", self.jumlah)
        print("Total        : Rp", self.total_harga)
        print("Uang Bayar   : Rp", self.uang_bayar)
        print("Kembalian    : Rp", self.kembalian, "\n")

    @staticmethod
    def hitung_total(harga, jumlah):
        return harga * jumlah

Alat1 = AlatMusik("AM001", "Gitar", 850000, 10)
Alat2 = AlatMusik("AM002", "Keyboard", 2500000, 5)

Pembeli1 = Pembeli("PM001", "Carmen", "081234567890")
Pembeli2 = Pembeli("PM002", "Stella", "081298765432")

Alat1.info()
Alat1.tambah_stok(5)
Alat1.info()
Alat1.kurangi_stok(-1)

AlatMusik.ubah_nama_toko("Hearts Music Store")
print("Hitung Total:", Transaksi.hitung_total(100000, 3), "\n")

Alat2.stok = -5
Pembeli1.no_hp = "0813"

Transaksi1 = Transaksi("TR001", "21-09-2026", Pembeli1, Alat1, 2, 2000000)
Alat1.kurangi_stok(Transaksi1.jumlah)
Transaksi1.cetak_struk()

Transaksi2 = Transaksi("TR002", "21-09-2026", Pembeli2, Alat2, 1, 3000000)
Alat2.kurangi_stok(Transaksi2.jumlah)
Transaksi2.cetak_struk()

print("Stok Gitar:", Alat1.stok, "| Stok Keyboard:", Alat2.stok)
print("Total Alat:", AlatMusik.total_alat)
print("Total Pembeli:", Pembeli.total_pembeli)
print("Total Transaksi:", Transaksi.total_transaksi)