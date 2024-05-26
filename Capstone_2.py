# Data sebagai inventaris barang di toko
toko_barang = [
    {"id": 1, "nama": "Kaset Game", "stok": 20, "harga": 300000},
    {"id": 2, "nama": "Stik", "stok": 50, "harga": 200000},
    {"id": 3, "nama": "Voucher", "stok": 30, "harga": 100000}
]

# Fungsi custom untuk menampilkan daftar barang
def tampilkan_barang():
    print("\n")
    print("Daftar Barang di Toko:")
    for barang in toko_barang:
        print(f"ID: {barang['id']}, Nama: {barang['nama']}, Stok: {barang['stok']}, Harga: {barang['harga']}")
    print("="*50)

# Fungsi untuk membeli barang
def beli_barang():
    tampilkan_barang()
    id_barang = int(input("Masukkan ID barang yang ingin dibeli: "))
    jumlah_beli = int(input("Masukkan jumlah yang ingin dibeli: "))
    
    for barang in toko_barang:
        if barang["id"] == id_barang:
            if barang["stok"] >= jumlah_beli:
                total_harga = jumlah_beli * barang["harga"]
                uang_diberikan = int(input(f"Total harga adalah Rp{total_harga:,}. Masukkan jumlah uang yang diberikan: "))
                if uang_diberikan >= total_harga:
                    kembalian = uang_diberikan - total_harga
                    barang["stok"] -= jumlah_beli
                    print(f"Berhasil membeli {jumlah_beli} {barang['nama']} dengan total harga Rp{total_harga:,}!")
                    print(f"Uang yang diberikan: Rp{uang_diberikan:,}, Kembalian: Rp{kembalian:,}")
                else:
                    print(f"Uang yang diberikan tidak mencukupi! Pembelian gagal.")
                return
            else:
                print("Stok tidak mencukupi!")
                return
    print("Barang tidak ditemukan!")

# Fungsi untuk login sebagai admin
def login_admin():
    password = input("Masukkan password admin: ")
    return password == "admin"

# Fungsi untuk menambah barang baru
def tambah_barang():
    if login_admin():
        id_barang = int(input("Masukkan ID barang baru: "))
        # Validasi untuk memastikan ID barang tidak duplikat
        for barang in toko_barang:
            if barang["id"] == id_barang:
                print("ID barang sudah ada! Silakan masukkan ID yang berbeda.")
                return
        
        nama_barang = input("Masukkan nama barang baru: ")
        stok_barang = int(input("Masukkan stok barang baru: "))
        harga_barang = int(input("Masukkan harga barang baru: "))
        
        barang_baru = {"id": id_barang, "nama": nama_barang, "stok": stok_barang, "harga": harga_barang}
        toko_barang.append(barang_baru)
        print("Barang baru berhasil ditambahkan!")
    else:
        print("Password admin salah!")

# Fungsi untuk menghapus barang
def hapus_barang():
    if login_admin():
        id_barang = int(input("Masukkan ID barang yang akan dihapus: "))
        for barang in toko_barang:
            if barang["id"] == id_barang:
                toko_barang.remove(barang)
                print("Barang berhasil dihapus!")
                return
        print("Barang tidak ditemukan!")
    else:
        print("Password admin salah!")

# Fungsi untuk mengupdate stok barang
def update_stok_barang():
    if login_admin():
        id_barang = int(input("Masukkan ID barang yang akan diupdate: "))
        for barang in toko_barang:
            if barang["id"] == id_barang:
                stok_baru = int(input(f"Masukkan stok baru untuk {barang['nama']}: "))
                barang["stok"] = stok_baru
                print("Stok berhasil diperbarui!")
                return
        print("Barang tidak ditemukan!")
    else:
        print("Password admin salah!")

# Fungsi untuk mengupdate harga barang
def update_harga_barang():
    if login_admin():
        id_barang = int(input("Masukkan ID barang yang akan diupdate: "))
        for barang in toko_barang:
            if barang["id"] == id_barang:
                harga_baru = int(input(f"Masukkan harga baru untuk {barang['nama']}: "))
                barang["harga"] = harga_baru
                print("Harga berhasil diperbarui!")
                return
        print("Barang tidak ditemukan!")
    else:
        print("Password admin salah!")

# Menu utama
def main():
    while True:
        print("\n")
        print("Fauzi Game Store: The Trusted Seller" ) 
        print("="*37)                                           
        print("|           Menu Utama              |")  
        print("="*37)            
        print("| 1. Tampilkan Daftar Barang        |")
        print("| 2. Beli Barang                    |")
        print("| 3. Tambah Barang (Admin)          |")
        print("| 4. Hapus Barang (Admin)           |")
        print("| 5. Update Stok Barang (Admin)     |")
        print("| 6. Update Harga Barang (Admin)    |")
        print("| 7. Keluar                         |")
        print("="*37)
        pilihan = input("Pilih menu: ")
        
        if pilihan == "1":
            tampilkan_barang()
        elif pilihan == "2":
            beli_barang()
        elif pilihan == "3":
            tambah_barang()
        elif pilihan == "4":
            hapus_barang()
        elif pilihan == "5":
            update_stok_barang()
        elif pilihan == "6":
            update_harga_barang()
        elif pilihan == "7":
            print("Terima kasih telah menggunakan program ini!")
            break
        else:
            print("Pilihan tidak valid!")

if __name__ == "__main__":
    main()
