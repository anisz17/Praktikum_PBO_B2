# Program Sistem Penjualan Toko Alat Musik

- **Nama:** Annisa Nur Raidah
- **NIM:** 2509106078
- **Kelas:** B2

## Deskripsi Program

Program ini adalah toko yang menjual alat musik dengan transaksi yang dilakukan secara offline. Pembeli akan memilih alat musik, membayar tunai, lalu stok alat musik berkurang stoknya dan struk pembelian dicetak beserta kembalian yang diterima.

## Struktur Class

**1. AlatMusik**

- Atribut kelas: `nama_toko`, `total_alat`
- Atribut public: `id_produk`, `nama`, `harga`
- Atribut private: `__stok`
- Instance method: `kurangi_stok()`, `tambah_stok()`, `info()`
- Class method: `ubah_nama_toko()`

**2. Pembeli** (data pembeli)

- Atribut kelas: `total_pembeli`
- Atribut public: `id_pembeli`, `nama`
- Atribut private: `__no_hp`

**3. Transaksi** (catatan pembelian)

- Atribut kelas: `total_transaksi`
- Atribut public: `id_transaksi`, `tanggal`, `pembeli`, `alat`, `jumlah`, `total_harga`, `uang_bayar`, `kembalian`
- Instance method: `cetak_struk()`
- Static method: `hitung_total()`

## Cara Menjalankan

```bash
python posttest1_2509106078_AnnisaNurRaidah.py
```

## Pengujian

Pengujian ada di bagian main code. Saat program di run hasilnya seperti ini:

- `Alat1.tambah_stok(5)`: stok Gitar menjadi 15
- `Alat1.kurangi_stok(-1)`: muncul pesan "Jumlah Stok Harus Lebih Dari 0"
- `AlatMusik.ubah_nama_toko(...)`: nama toko berubah menjadi "Hearts Music Store"
- `Transaksi.hitung_total(100000, 3)`: hasilnya 300000
- `Alat2.stok = -5`: muncul pesan "Stok Tidak Boleh Minus!", stok tidak berubah
- `Pembeli1.no_hp = "0813"`: muncul pesan "Nomor Telepon Minimal 11 Angka!", nomor tidak berubah
- Transaksi 1 (2 gitar, bayar Rp 2.000.000): total Rp 1.700.000, kembalian Rp 300.000
- Transaksi 2 (1 keyboard, bayar Rp 3.000.000): total Rp 2.500.000, kembalian Rp 500.000
