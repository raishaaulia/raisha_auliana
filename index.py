# konversi mata uang asing ke rupiah

print("! Login akun terlebih dahulu untuk melanjutkan !" + "\n")

# menerapkan login
print(39 * "*")
name = input("Masukkan nama: ")
nim = input("Masukkan nim: " )
print(7 * "-")
print("CAPTCHA" + "\n" + "Th95V" )
print(7 * "-")
captcha = input("Masukkan captcha:" + "\n")
print(39 * "*")

# menampilkan pilihan
print("Hello, " + name + "!" + "\n")
print("Mata uang yang akan dikonversi")
print(" 1. US Dollar (Rp. 15.395)")
print(" 2. Yen (Rp. 103)")
print(" 3. Ringgit (Rp. 3.284)" + "\n")

# input 
angka1 = float(input("> Masukkan jumlah yang ingin dikonversi = "))
mata_uang = input("> Pilih mata uang (US Dollar, Yen, Ringgit) : ")
konversi_mata_uang1 = 15395
konversi_mata_uang2 = 103
konversi_mata_uang3 = 3284

# percabangan
print("")
if mata_uang == "US Dollar":
    hasil = angka1/konversi_mata_uang1
    print(f"Hasil konversi adalah ${hasil}")
    print("")
elif mata_uang == "Yen":
    hasil = angka1/konversi_mata_uang2
    print(f"Hasil konversi adalah ¥{hasil}")
    print("")
elif mata_uang == "Ringgit":
    hasil = angka1/konversi_mata_uang3
    print(f"Hasil konversi adalah RM{hasil}")
    print("")

print("! Program telah selesai !")
