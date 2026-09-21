# Program Sistem Penjualan Toko Alat Musik

- **Nama:** Annisa Nur Raidah
- **NIM:** 2509106078
- **Kelas:** B2

## Deskripsi Program

Program ini mencatat data alat musik, data pembeli, dan transaksi dari pembelian. Program ini tentang toko yang menjual alat musik dengan transaksi yang dilakukan secara offline. Pembeli akan memilih alat musik, membayar tunai, lalu stok alat musik berkurang stoknya dan struk pembelian dicetak beserta kembalian yang diterima.

## Struktur Class

**1. AlatMusik**

- Atribut kelas: `nama_toko`, `total_alat`
- Atribut public: `id_produk`, `nama`, `harga`
- Atribut private: `__stok`
- Instance method: `kurangi_stok()`, `tambah_stok()`, `info()`
- Class method: `ubah_nama_toko()`

**2. Pembeli**

- Atribut kelas: `total_pembeli`
- Atribut public: `id_pembeli`, `nama`, `email`
- Atribut private: `__no_telp`

**3. Transaksi**

- Atribut kelas: `total_transaksi`
- Atribut public: `id_transaksi`, `tanggal`, `pembeli`, `alat`, `jumlah`, `total_harga`, `uang_bayar`, `kembalian`
- Instance method: `cetak_struk()`
- Static method: `hitung_total()`

## Pengujian

Pengujian ada di bagian main code. Saat program di run hasilnya seperti ini:

- `alat1.info()`: menampilkan informasi Gitar dengan stok 10
- `alat1.tambah_stok(5)`: "Stok Gitar Bertambah, Stok Tersedia: 15"
- `alat1.kurangi_stok(-1)`: "Jumlah Stok Gitar Harus Lebih Dari 0"
- `AlatMusik.ubah_nama_toko("Hearts Music Store")`: nama toko berubah menjadi "Hearts Music Store"
- `Transaksi.hitung_total(100000, 3)`: hasilnya 300000
- `alat2.stok = 10`: "Stok keyboard Berhasil Diubah Menjadi: 10"
- `alat2.stok = -5`: "Stok Keyboard Tidak Boleh Minus!", stok tetap 10
- `pembeli1.no_telp = "08123456789"`: diterima, nomor telepon Carmen berubah
- `pembeli1.no_telp = "0813"`: "Nomor Telepon Carmen Minimal 11 Digit!"
- transaksi1 (2 Gitar, bayar Rp 2.000.000): total Rp 1.700.000, kembalian Rp 300.000, stok Gitar menjadi 13
- transaksi2 (1 Keyboard, bayar Rp 3.000.000): total Rp 2.500.000, kembalian Rp 500.000, stok Keyboard menjadi 9
- `Stok Gitar:` 13, `Stok Keyboard:` 9
- `Total Alat:` 2
- `Total Pembeli:` 2
- `Total Transaksi:` 2
