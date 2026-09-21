class AlatMusik:
    nama_toko = "Hearts Melodi"
    total_alat = 0

    def __init__(self, id_produk, nama, harga, stok):
        self.id_produk = id_produk
        self.nama = nama
        self.harga = harga
        self.__stok = stok
        AlatMusik.total_alat += 1

    @property
    def stok(self):
        return self.__stok
    
    @stok.setter
    def stok(self, stok_baru):
        if stok_baru < 0:
            print(f"Stok {self.nama} Tidak Boleh Minus!\n")
        else:
            self.__stok = stok_baru
            print(f"Stok {self.nama} Berhasil Diubah Menjadi: {self.__stok}\n")

    def kurangi_stok(self, jumlah):
        if jumlah <= 0:
            print(f"Jumlah Stok {self.nama} Harus Lebih Dari 0\n")
        elif jumlah > self.__stok:
            print(f"Stok {self.nama} Melebihi Jumlah Stok Tersedia\n")
        else:
            self.__stok -= jumlah
            print(f"Stok {self.nama} Berkurang Sebanyak {jumlah}, Stok Tersedia: {self.__stok}\n")

    def tambah_stok(self, jumlah):
        if jumlah <= 0:
            print(f"Jumlah Stok {self.nama} Harus Lebih Dari 0\n")
        else:
            self.__stok += jumlah
            print(f"Stok {self.nama} Bertambah Sebanyak {jumlah}, Stok Tersedia: {self.__stok}\n")

    @classmethod
    def ubah_nama_toko(cls, nama_baru):
        cls.nama_toko = nama_baru
        print(f"Nama Toko Berubah Menjadi: {cls.nama_toko}\n")

    def info(self):
        print("----------------------------------")
        print("         INFORMASI PRODUK         ")
        print("----------------------------------")
        print(f"ID Produk        : {self.id_produk}")
        print(f"Nama Alat        : {self.nama}")
        print(f"Harga            : Rp {self.harga}")
        print(f"Stok             : {self.__stok}\n")

class Pembeli:
    total_pembeli = 0

    def __init__(self, id_pembeli, nama, no_telp, email):
        self.id_pembeli = id_pembeli
        self.nama = nama
        self.__no_telp = no_telp
        self.email = email
        Pembeli.total_pembeli += 1

    @property
    def no_telp(self):
        return self.__no_telp

    @no_telp.setter
    def no_telp(self, no_telp_baru):
        if len(no_telp_baru) < 11:
            print("Nomor Telepon Minimal 11 Digit!\n")
        else:
            self.__no_telp = no_telp_baru
            print(f"Nomor Telepon {self.nama} Berhasil Diubah\n") 

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
        print(f"ID Transaksi : {self.id_transaksi}")
        print(f"Tanggal      : {self.tanggal}")
        print(f"Pembeli      : {self.pembeli.nama}")
        print(f"No. Telepon  : {self.pembeli.no_telp}")
        print(f"Email        : {self.pembeli.email}")
        print(f"Barang       : {self.alat.nama} x {self.jumlah}")
        print(f"Total        : Rp {self.total_harga}")
        print(f"Uang Bayar   : Rp {self.uang_bayar}")
        print(f"Kembalian    : Rp {self.kembalian}\n")

    @staticmethod
    def hitung_total(harga, jumlah):
        return harga * jumlah

alat1 = AlatMusik("AM001", "Gitar", 850000, 10)
alat2 = AlatMusik("AM002", "Keyboard", 2500000, 5)

pembeli1 = Pembeli("PM001", "Carmen", "081234567890", "carmen@email.com")
pembeli2 = Pembeli("PM002", "Stella", "081298765432", "stella@email.com")

alat1.info()
alat1.tambah_stok(5)
alat1.info()
alat1.kurangi_stok(1)

AlatMusik.ubah_nama_toko("Hearts Music Store")
print(f"Hitung Total: {Transaksi.hitung_total(100000, 3)}\n")

alat2.stok = 10
alat2.stok = -5
pembeli1.no_telp = "08123456789"
pembeli1.no_telp = "0813"

transaksi1 = Transaksi("TR001", "21-09-2026", pembeli1, alat1, 2, 2000000)
transaksi1.cetak_struk()
alat1.kurangi_stok(transaksi1.jumlah)

transaksi2 = Transaksi("TR002", "21-09-2026", pembeli2, alat2, 1, 3000000)
transaksi2.cetak_struk()
alat2.kurangi_stok(transaksi2.jumlah)

print(f"Stok Gitar: {alat1.stok} | Stok Keyboard: {alat2.stok}")
print(f"Total Alat: {AlatMusik.total_alat}")
print(f"Total Pembeli: {Pembeli.total_pembeli}")
print(f"Total Transaksi: {Transaksi.total_transaksi}")