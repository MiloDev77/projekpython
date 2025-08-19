import random
#1.Dictionary untuk menyimpan akun bank
# Akun
akun = {
    "admin": {
        "milo": {
            "nama": "Syamil Gymnastiar Nugroho",
            "pin": "2027",
            "saldo": 250000000000
        },
        "idan": {
            "nama": "Muhammad Wildan",
            "pin": "6969",
            "saldo": 59000000000
        },
        "akhdan": {
            "nama": "Muhammad Akhdan",
            "pin": "7777",
            "saldo": 45000000000
        },
        "bilal": {
            "nama": "Muhammad Bilal",
            "pin": "2008",
            "saldo": 45500000000
        }
    },
    "anggota": {


    }
}
#2.Fungsi
# ✨ Fungsi ✨
# Fungsi verifikasi pin
#2.1.Fungsi untuk memastikan apakah pin yang diinput sama dengan pin yang sudah ada
def verifikasi(tingkatan, user, pinVerif):
    hasil = True if pinVerif == konversi(tingkatan, user, "pin") else False
    return hasil
# Fungsi mengambil nilai dalam dictionary
#2.2.Fungsi untuk mengambil nilai dari dictionary dan mengembalikan nilai tersebut untuk diproses
def konversi(tingkatan, user, atribut):
    return akun[tingkatan][user][atribut]
# Randomizer Nomor Rekening
#2.3.Fungsi untuk membuat nomor rekening baru dengan random
def rekening():
    angka = ""
    for x in range(6):
        angkaRandom = random.randint(0, 9)
        angka += str(angkaRandom)
    return angka
# 💳 Fitur2 (fungsi ini dapt digunakan oleh admin maupun anggota) 💳
#2.4.Fungsi dasar untuk transfer tunai antara dua pengguna yang terdaftar di dictionary
def transfer(tingkatan, user, tingkatantarget, rekeningtarget, nominal, namabank):
    saldoUtama = konversi(tingkatan, user, "saldo")
    if rekeningtarget in akun[tingkatantarget]:
        saldoTarget = konversi(tingkatantarget, rekeningtarget, "saldo")
        if nominal < 0:
            print("\nNominal tidak valid!")
        elif nominal < saldoUtama:
            akun[tingkatan][user]["saldo"] = saldoUtama - nominal
            akun[tingkatantarget][rekeningtarget]["saldo"] = saldoTarget + nominal
            print(f"\n=== TRANSFER SUKSES ===\nNama Bank Dituju: {namabank}\nNama Akun: {konversi(tingkatantarget, rekeningtarget, 'nama')}\nNominal Transfer: {nominal}\nSaldo Anda Sekarang: {konversi(tingkatan, user, 'saldo')}")
        else:
            print("\nSaldo tidak cukup")
    else:
        print("\nAkun rekening tidak terdaftar")
#2.5.Fungsi untuk menambahkan saldo akun bank yang terdaftar di dictionary
def isiSaldo(tingkatan, user, nominal):
    tunaiAkhir = nominal - 2000
    akun[tingkatan][user]["saldo"] = konversi(tingkatan, user, "saldo") + tunaiAkhir
    print(f"Top up berhasil! saldo anda sekarang: {konversi(tingkatan, user, 'saldo')}")
#2.6.Fungsi untuk membayar tagihan menggunakan saldo yang dimilikinya dan memasukkan jenis tagihan, dan nomor tagihan (Tidak ada verifikasi jenis tagihan dan nomor tagihan, sehingga memungkinkan untuk sang user menginput jenis tagihan dan nomor tagihan secara ngasal)
def bayarTagihan(tingkatan, user, jenisTagihan, idTagihan, nominalTagihan):
    saldoUtama = konversi(tingkatan, user, "saldo")
    if nominalTagihan < saldoUtama:
        akun[tingkatan][user]["saldo"] = saldoUtama - nominalTagihan
        print(f"\n=== BERHASIL ===\nJenis Tagihan: {jenisTagihan}\nNomor Tagihan: {idTagihan}\nNominal Tagihan: {nominalTagihan}\nSaldo Anda Sekarang: {konversi(tingkatan, user, "saldo")}")
    elif nominalTagihan < 0:
        print("\nNominal tidak valid!")
    else:
        print("\nSaldo tidak cukup")
#2.7.Fungsi untuk menampilkan saldo akun bank yang sedang dipakai
def cekSaldo(tingkatan, user):
    print(f"\nSaldo anda sekarang: {konversi(tingkatan, user, "saldo")}")
    pass
#2.8.Fungsi untuk mengambil saldo tunai dari akun bank yang sedang dipakai
def tarikTunai(tingkatan, user, nominalPenarikan):
    saldoUtama = konversi(tingkatan, user, "saldo")
    if nominalPenarikan < saldoUtama:
        akun[tingkatan][user]["saldo"] = saldoUtama - nominalPenarikan
        print(f"\n=== PENARIKAN BERHASIL ===\nSaldo Anda Sekarang: {konversi(tingkatan, user, "saldo")}")
    elif nominalPenarikan < 0:
        print("\nNominal tidak valid!")
    else:
        print("\nSaldo tidak cukup")


# Beranda Anggota 🎎
#3.Kode untuk menampilkan Beranda setalah user login ke akunnya
def anggota(userAnggota):
    pin = ""
    perulangan = True
    while perulangan == True:
        print(f"\n=== Selamat Datang! {konversi("anggota", userAnggota, "nama")} ===")
        fitur = int(input("Silahkan pilih beberapa aksi berikut!\n1. Isi Saldo\n2. Cek Saldo\n3. Transfer Sesama Bank\n4. Transfer Antar Bank\n5. Bayar Tagihan\n6. Tarik Tunai\n7. Ubah Pin\n8. Logout\nKetik angka di atas untuk memilih aksi: "))
        match fitur:
            case 1:
                nominal = int(input("\nMasukkan nominal yang ingin diisi (tambahkan 2000 sebagai biaya admin): "))
                isiSaldo("anggota", userAnggota, nominal)
                perulangan = True
            case 2:
                cekSaldo("anggota", userAnggota)
                perulangan = True
            case 3:
                jenisTingkatan = int(input("\n1) Admin\n2) Member\nKetik opsi angka di atas untuk memilih tingkat keanggotaan yang dituju (default \"Member\"): "))
                pilihanTingkatan = "admin" if jenisTingkatan == 1 else "anggota"
                norekening = input("masukkan nomor rekening: ").strip()
                nominaltfr = int(input("Isi nominal untuk transfer: "))
                pin = input("Masukkan pin anda: ").strip()
                while verifikasi("anggota", userAnggota, pin) != True and pin != "keluar":
                    pin = input("Pin salah! Masukkan dengan pin benar: ").strip()
                if pin == "keluar":
                    print("\nTranfer dibatalkan")
                else:
                    transfer("anggota", userAnggota, pilihanTingkatan, norekening, nominaltfr, "Sesama bank")
                perulangan = True
            case 4:
                jenisTingkatan = int(input("\n1) Admin\n2) Member\nKetik opsi angka di atas untuk memilih tingkat keanggotaan yang dituju: "))
                pilihanTingkatan = "admin" if jenisTingkatan == 1 else "anggota"
                rekeningbank = input("Nama bank yang dituju: ").strip()
                norekening = input("Masukkan nomor rekening: ").strip()
                nominaltfb = int(input("Isi nominal untuk transfer (tambahkan 2000 sebagai biaya admin): "))
                nominalAkhir = nominaltfb - 2000
                pin = input("Masukkan pin anda: ").strip()
                while verifikasi("anggota", userAnggota, pin) != True and pin != "keluar":
                    pin = input("Pin salah! Masukkan dengan pin benar: ").strip()
                if pin == "keluar":
                    print("\nTranfer dibatalkan")
                else:
                    transfer("anggota", userAnggota, pilihanTingkatan, norekening, nominalAkhir, rekeningbank)
                perulangan = True
            case 5:
                jenisTagihan = input("Jenis tagihan: ").strip()
                idTagihan = input("ID tagihan (berupa angka): ").strip()
                nominalTagihan = int(input("Nominal tagihan: "))
                pin = input("Masukkan pin anda: ").strip()
                while verifikasi("anggota", userAnggota, pin) != True and pin != "keluar":
                    pin = input("Pin salah! Masukkan dengan pin benar: ").strip()
                if pin == "keluar":
                    print("\nTranfer dibatalkan")
                else:
                    bayarTagihan("anggota", userAnggota, jenisTagihan, idTagihan, nominalTagihan)
                perulangan = True
            case 6:
                nominalPenarikan = int(input("Jumlah nominal ingin ditarik: "))
                pin = input("Masukkan pin anda: ").strip()
                while verifikasi("anggota", userAnggota, pin) != True and pin != "keluar":
                    pin = input("Pin salah! Masukkan dengan pin benar: ").strip()
                if pin == "keluar":
                    print("\nTranfer dibatalkan")
                else:
                    tarikTunai("anggota", userAnggota, nominalPenarikan)
                perulangan = True
            case 7:
                pin = input("Masukkan pin anda: ").strip()
                while verifikasi("anggota", userAnggota, pin) != True and pin != "keluar":
                    pin = input("Pin salah! Masukkan dengan pin benar: ").strip()
                if pin == "keluar":
                    print("\nPengubahan pin dibatalkan")
                else:
                    pinBaru = input("Masukkan pin baru anda (4 digit): ").strip()
                    while len(pinBaru) != 4:
                        pinBaru = input("Pin yang dimasukkan terlalu banyak! \nMasukkan pin baru anda (4 digit): ").strip()
                    akun["anggota"][userAnggota]["pin"] = pinBaru
                    print(f"\n=== PIN BERHASIL DIUBAH ===\nPin baru anda: {pinBaru}\n")
            case 8:
                print(f"\n=== Terima kasih telah menggunakan ATM ini. Sampai jumpa kembali {konversi("anggota", userAnggota, "nama")}!! 👋 ===\n")
                perulangan = False
            case _:
                print("\nKetik opsi dengan benar!")
                perulangan = True

# 🎇 Admin Mode (Fitur Eksklusif Admin Mode) 🎇
#4.Fungsi untuk fitur yang hanya bisa diakses admin
#4.1.Fungsi untuk menampilkan total saldo dan jumlah seluruh anggota yang terdaftar di dictionary sebagai pengguna atau anggota biasa
def saldoAnggota():
    if len(akun["anggota"]) == 0:
        print ("\n Belum ada anggota yang terdaftar")
        return
    total = 0
    for norek in akun["anggota"]:
        total += akun["anggota"][norek]["saldo"]
    print (f"\n=== TOTAL SALDO ANGGOTA ===\nJumlah akun anggota: {len(akun['anggota'])}\nTotal saldo seluruh anggota: {total}")
#4.2.Fungsi untuk mendapatkan info-info dari akun pengguna biasa yang terdaftar di dictionary
def cekAkun():
    if len(akun["anggota"]) == 0:
        print ("\nBelum ada anggota yang terdaftar")
        return
    for x, data in akun["anggota"].items():
        print(f"\nNomor Rekening: {x}")
    norek = input("\nMasukkan nomor rekening anggota yang ingin di cek: ").strip()
    if norek in akun["anggota"]:
        data = akun["anggota"][norek]
        print(f"\n=== DETAIL AKUN ANGGOTA ===\nNomor Rekening: {norek}\nNama: {data['nama']}\nUmur: {data['umur']}\nStatus: {data['status']}\nSaldo: {data['saldo']}")
    else:
        print ("\nNomor rekening tidak ditemukan")
#4.3.Fungsi untuk membuat akun baru tanpa harus log out dari akun yang sedang dipakai
def buatAkun():
    nomorRekening = rekening()
    nama = str(input("\nIsi data berikut ini\nNama Lengkap: ")).lower().strip().title()
    umur = int(input("Umur: "))
    status = str(input("Status pekerjaan: "))
    pin = str(input("Buat pin yang kuat (4): ")).strip()
    while len(pin) != 4:
        pin = int(input("Pin yang dimasukkan terlalu banyak! \nBuat pin yang kuat (4): ")).strip()
    akun["anggota"][nomorRekening] = {
        "nama": nama,
        "umur": umur,
        "status": status,
        "pin": pin,
        "saldo": 1000000
    }
    print(f"\n=== AKUN BERHASIL DIBUAT ===\nNomor rekening: {nomorRekening}\nPin: {pin}\nSaldo awal: 1000000\n")
#4.4.Fungsi untuk menghapus akun anggota biasa yang terdaftar di dictionary
def hapusAkun():
    if len(akun["anggota"]) == 0:
        print ("\n Belum ada anggota yang terdaftar")
        return
    print("\n=== DAFTAR NOMOR REKENING ANGGOTA ===")
    for x in akun["anggota"]:
        print(f"Nomor Rekening: {x} |\n Nama: {akun['anggota'][x]['nama']}")
    norek = input("\nMasukkan nomor rekening anggota yang ingin dihapus: ").strip()
    if norek in akun["anggota"]:
        konfirmasi = str(input(f"Apakah anda yakin ingin menghapus {akun['anggota'][norek]['nama']} dengan nomor rekening {norek}? (ya/tidak)"))
        if konfirmasi == "ya":
            del akun["anggota"][norek]
            print ("\nAkun berhasil dihapus")
        elif konfirmasi == "tidak":
            print ("\nPenghapusan dibatalkan")
        else:
            str(input("Error!!! Masukkan kembali pilihan anda: (ya/tidak)"))
    else:
        print ("\nNomor rekening tidak ditemukan")
#5.Kode untuk menampilkan menu untuk admin
def admin(userAdmin):
    pin = ""
    perulangan = True
    while perulangan == True:
        print(f"\n=== Halo {konversi("admin", userAdmin, "nama")} 👋 ===")
        fitur = int(input("Silahkan pilih beberapa aksi berikut!\n1. Isi Saldo\n2. Cek Saldo\n3. Transfer Sesama Bank\n4. Transfer Antar Bank\n5. Bayar Tagihan\n6. Tarik Tunai\n7. Ubah Pin\n\n✨Fitur Admin✨\n8. Total Saldo Anggota\n9. Cek Akun Anggota\n10. Buat Akun Anggota\n11. Hapus Akun Anggota\n12. Logout\nKetik angka di atas untuk memilih aksi: "))
        match fitur:
            case 1:
                nominal = int(input("\nMasukkan nominal yang ingin diisi (tambahkan 2000 sebagai biaya admin): "))
                isiSaldo("admin", userAdmin, nominal)
                perulangan = True
            case 2:
                cekSaldo("admin", userAdmin)
                perulangan = True
            case 3:
                jenisTingkatan = int(input("\n1) Admin\n2) Member\nKetik opsi angka di atas untuk memilih tingkat keanggotaan yang dituju (default \"Member\"): "))
                pilihanTingkatan = "admin" if jenisTingkatan == 1 else "anggota"
                norekening = input("masukkan nomor rekening: ").strip()
                nominaltfr = int(input("Isi nominal untuk transfer: "))
                pin = input("Masukkan pin anda: ").strip()
                while verifikasi("admin", userAdmin, pin) != True and pin != "keluar":
                    pin = input("Pin salah! Masukkan dengan pin benar: ").strip()
                if pin == "keluar":
                    print("\nTranfer dibatalkan")
                else:
                    transfer("admin", userAdmin, pilihanTingkatan, norekening, nominaltfr, "Sesama bank")
                perulangan = True
            case 4:
                jenisTingkatan = int(input("\n1) Admin\n2) Member\nKetik opsi angka di atas untuk memilih tingkat keanggotaan yang dituju: "))
                pilihanTingkatan = "admin" if jenisTingkatan == 1 else "anggota"
                rekeningbank = input("Nama bank yang dituju: ").strip()
                norekening = input("Masukkan nomor rekening: ").strip()
                nominaltfb = int(input("Isi nominal untuk transfer (tambahkan 2000 sebagai biaya admin): "))
                nominalAkhir = nominaltfb - 2000
                pin = input("Masukkan pin anda: ").strip()
                while verifikasi("admin", userAdmin, pin) != True and pin != "keluar":
                    pin = input("Pin salah! Masukkan dengan pin benar: ").strip()
                if pin == "keluar":
                    print("\nTranfer dibatalkan")
                else:
                    transfer("admin", userAdmin, pilihanTingkatan, norekening, nominalAkhir, rekeningbank)
                perulangan = True
            case 5:
                jenisTagihan = input("Jenis tagihan: ").strip()
                idTagihan = input("ID tagihan (berupa angka): ").strip()
                nominalTagihan = int(input("Nominal tagihan: "))
                pin = input("Masukkan pin anda: ").strip()
                while verifikasi("admin", userAdmin, pin) != True and pin != "keluar":
                    pin = input("Pin salah! Masukkan dengan pin benar: ").strip()
                if pin == "keluar":
                    print("\nTranfer dibatalkan")
                else:
                    bayarTagihan("admin", userAdmin, jenisTagihan, idTagihan, nominalTagihan)
                perulangan = True
            case 6:
                nominalPenarikan = int(input("Jumlah nominal ingin ditarik: "))
                pin = input("Masukkan pin anda: ").strip()
                while verifikasi("admin", userAdmin, pin) != True and pin != "keluar":
                    pin = input("Pin salah! Masukkan dengan pin benar: ").strip()
                if pin == "keluar":
                    print("\nTranfer dibatalkan")
                else:
                    tarikTunai("admin", userAdmin, nominalPenarikan)
                perulangan = True
            case 7:
                pin = input("Masukkan pin anda: ").strip()
                while verifikasi("admin", userAdmin, pin) != True and pin != "keluar":
                    pin = input("Pin salah! Masukkan dengan pin benar: ").strip()
                if pin == "keluar":
                    print("\nPengubahan pin dibatalkan")
                else:
                    pinBaru = input("Masukkan pin baru anda (4 digit): ").strip()
                    while len(pinBaru) != 4:
                        pinBaru = input("Pin yang dimasukkan terlalu banyak! \nMasukkan pin baru anda (4 digit): ").strip()
                    akun["anggota"][userAdmin]["pin"] = pinBaru
                    print(f"\n=== PIN BERHASIL DIUBAH ===\nPin baru anda: {pinBaru}\n")
            case 8:
                saldoAnggota()
                perulangan = True
            case 9:
                cekAkun()
                perulangan = True
            case 10:
                buatAkun()
                perulangan = True
            case 11:
                hapusAkun()
                perulangan = True
            case 12:
                print(f"\n=== Terima kasih telah menggunakan ATM ini. Sampai jumpa kembali {konversi("admin", userAdmin, "nama")}!! 👋 ===\n")
                perulangan = False
            case _:
                print("Ketik opsi dengan benar!")
                perulangan = True
# Sesi Daftar dan Login
#6.Fungsi untuk mendaftarkan akun bank dan masuk ke akun bank
#6.1.Fungsi untuk membuat akun bank dan memasukkannya ke dictionary
def daftar():
    nomorRekening = rekening()
    nama = str(input("\nIsi beberapa data kredensial berikut\nNama Lengkap: ")).lower().strip().title()
    umur = int(input("Umur: "))
    status = str(input("Status pekerjaan: ")).strip()
    pin = str(input("Buat pin yang kuat (4 digit): ")).strip()
    while len(pin) != 4:
        pin = str(input("Buat pin persis 4 digit: ")).strip()
    akun["anggota"][nomorRekening] = {
        "nama": nama,
        "umur": umur,
        "status": status,
        "pin": pin,
        "saldo": 1000000
    }
    print(f"\nSilahkan catat data anda berikut!\nNomor rekening anda: {nomorRekening}\nPin anda: {pin}\nSelamat anda telah membuat akun! (gratis saldo 1000000 untuk fresh account)\n")
#6.2.Fungsi untuk masuk ke akun bank yang sudah dimasukkan ke dictionary (Jika akun tidak terdaftar maka akan diarahkan untuk membuat akun) 
def login():
    norek = str(input("Masukkan nomor rekening anda: ")).strip()
    if norek in akun["admin"]:
        pinAdmin = konversi("admin", norek, "pin")
        pin = str(input("\n❗ Admin Detected ❗\nMasukkan pin anda: ")).strip()
        while pin !=  pinAdmin and pin != "keluar":
            pin = str(input("Masukkan pin dengan benar! (ketik keluar untuk mengakhiri): ")).strip()
        if pin == pinAdmin:
            print("💻 Mode Admin Aktif 💻")
            admin(norek)
        else:
            print("\nAnda mengakhiri sesi login...\n")
    elif norek in akun["anggota"]:
        pinAnggota = konversi("anggota", norek, "pin")
        pin = str(input("\nAkun anda terdaftar!\nMasukkan pin anda: ")).strip()
        while pin != pinAnggota and pin != "keluar":
            pin = str(input("Masukkan pin anda dengan benar! (ketik keluar untuk mengakhiri): ")).strip()
        if pin == pinAnggota:
            anggota(norek)
        else:
            print("\nAnda mengakhiri sesi login...\n")
    else:
        print("Akun tidak terdaftar")
        pilih = input("Apakah ingin daftar? (Ketik \"ya\" untuk buat. Ketik \"tidak\" untuk berhenti): ").lower().strip()
        if pilih == "ya":
            daftar()
        elif pilih == "tidak":
            print("\nSesi berakhir...\n")
        else:
            print("\nPilihan tidak valid\n")
# 🎨 Kode Eksekusi 🎨
#7.Kode Untuk Menampilkan Menu Awal Program
perulangan = True
while perulangan == True:
    pilihan = str(input("Pilih (ketik pilihan):\n1. Login\n2. Daftar\n3. Akhiri\n")).lower().strip()
    match pilihan:
        case "daftar":
            daftar()
            perulangan = True
        case "login":
            login()
            perulangan = True
        case "akhiri":
            perulangan = False
        case _:
            print("\nKetik pilihan dengan benar!\n")
            perulangan = True
