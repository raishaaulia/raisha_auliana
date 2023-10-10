print(57 * "-")
print("          Silahkan login akun untuk melanjutkan")
print("              Masuk menggunakan akun anda ")
print(57 * "-", "\n")

print("LOGIN")
print("1. Login sebagai admin ")
print("2. Login sebagai customer")
print("3. Keluar")
login = input("Masukkan pilihan login: ")
print("")
print(57 * "-")

# login
if login == "1":
    print("Masuk sebagai admin")
    email1 = "salonbatavia@gmail.com"
    password1 = "salon123"
    email_admin = input("Masukkan alamat email: ")
    password_admin= input("Masukkan password: ")
    if email_admin == email1 and password_admin == password_admin:
        print("Anda berhasil masuk sebagai admin")
    else:
        print("Alamat email atau password salah")
        print("Silahkan coba lagi")
elif login == "2":
    print("Anda berhasil masuk sebagai customer")
    email1 = input("Masukkan nama: ")
    notelp = input("Masukkan No. Telp: ")
    perawatan = input("Pilih perawatan yang ingin dipilih: ")
    print("Anda sudah masuk ke dalam antrian. Silahkan menunggu panggilan")
elif login == "3":
    print("Keluar dari program")
else:
    print("Pilihan tidak valid")

# Inisialisasi tabel
from prettytable import PrettyTable
table = PrettyTable()

# Data awal dalam tabel
table.field_names = ["No", "Perawatan", "Harga"]
table.add_row([1, "Hair Cut", "Rp. 50.000"])
table.add_row([2, "Hair Cut + Creambath", "Rp. 100.000"])
table.add_row([3, "Creambath", "Rp. 40.000"])
table.add_row([4, "Hair Color", "Rp. 150.000"])
table.add_row([5, "Scalp Massage", "Rp. 60.000"])
table.add_row([6, "Body Massage", "Rp. 200.000"])
table.add_row([7, "Manicure", "Rp. 80.000"])
table.add_row([8, "Pedicure", "Rp. 90.000"])
table.add_row([9, "Foot Spa", "Rp. 120.000"])
table.add_row([10, "Facial", "Rp. 156.000"])

# fungsi create
def create():
    No = int(input("Masukkan Nomor: "))
    Perawatan = input("Masukkan Perawatan: ")
    Harga = input("Masukkan Harga: Rp. ")
    table.add_row([No, Perawatan, Harga])
    print(table)
    print("Data berhasil ditambahkan ke tabel")

# fungsi read
def read():
    print(table)

# fungsi update
def update():
    No = input("Masukkan Nomor: ")
    Perawatan = input("Masukkan Perawatan Terbaru: ")
    Harga = input("Masukkan Harga Terbaru: Rp. ")
    for i, row in enumerate(table._rows):
        if int(row[0]) == No:
            table._rows[i] = [row[0], input("Masukkan Harga Terbaru: ")]
    print("Data berhasil diupdate")
            
       
# fungsi delete
def delete():
    No = (input("Pilih nomor yang akan dihapus: "))
    for i, row in enumerate(table._rows):
        if int(row[0]) == No:
            table.del_row(i)
    print("Data berhasil dihapus")

while True:
    print("\nMenu Utama:")
    print("1. Tambah List Perawatan")
    print("2. Lihat List Perawatan")
    print("3. Update List Perawatan")
    print("4. Hapus List Perawatan")
    print("5. Keluar", "\n")
    
    pilihan_menu = input("Pilih menu: ")
    
    if pilihan_menu == "1":
        create()
    elif pilihan_menu == "2":
        read()
    elif pilihan_menu == "3":
        update()
    elif pilihan_menu == "4":
        delete()
    elif pilihan_menu == "5":
        print("Keluar Dari Program")
        break
    else:
        print("Menu tidak valid. Silakan coba lagi.")
