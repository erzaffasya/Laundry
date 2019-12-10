from datetime import timedelta, datetime
from Antrian import *

time = datetime.now()
pesanan = Queue()
hargasatuan = [['Rompi  ', 10000],
               ['Jaket  ', 10000],
               ['selimut', 15000],
               ['sepatu ', 15000]]
hargakiloan = [['1 kg', 6000]]
urutan = 1

s = "pythonds"
print('{:.4}'.format("py"))
print("%.1s" % (s))


def struk(Data, No):
    print("\n" * 5)
    print("▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒\n"
          "▒▒                 +--------------+                 ▒▒\n"
          "▒▒  +--------------| Struk laundy |--------------+  ▒▒\n"
          "▒▒  |              +--------------+              |  ▒▒\n"
          "▒▒  |                                            |  ▒▒")
    print("        Nama           : %s " % (Data.getdata(No, 1)))
    print("        Nomor Telepon  : %s" % (Data.getdata(No, 2)))
    print("        Alamat         : %s" % (Data.getdata(No, 2)))
    print("        Jenis Laundry\n"
          "         -Kiloan\n"
          "          -Strika      : %s" % (Data.getdata(No, 1)))
    print("          -Berat       : %s" % (Data.getdata(No, 1)))
    print("         -Satuan\n"
          "          -Jenis       : %s" % (Data.getdata(No, 1)))
    print("          -Jumlah      : %s" % (Data.getdata(No, 1)))
    print("        Proses         : %s" % (Data.getdata(No, 3)))
    print("        Tanggal Masuk  : %s" % (Data.getdata(No, 4)))
    print("        Tanggal Keluar : %s" % (Data.getdata(No, 5)))
    print("        Biaya          : %s" % (Data.getdata(No, 1)))
    print("▒▒  |                                            |  ▒▒\n"
          "▒▒  |                                            |  ▒▒\n"
          "▒▒  +--------------------------------------------+  ▒▒\n"
          "▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒")
    print("\n" * 5)


def cetak():
    print('Berikut Daftar Harga\n'
          '+----+-------------+----------+\n'
          '+ No | Paket       |   Harga  |\n'
          '+----+-------------+----------+')
    for i in range(len(hargasatuan)):
        print("| %d  | %s     |   %d  |" % (i + 1, hargasatuan[i][0], hargasatuan[i][1]))
    print('+----+-------------+----------+')


while True:
    print("=" * 50)
    print("Menu :\n"
          "1. Daftar Harga\n"
          "2. Pesanan\n"
          "3. Cek Pesanan\n"
          "4. Proses Antrian\n"
          "5. Keluar\n")
    p = input("Masukkan pilihan anda :\n->")
    print("=" * 50)
    if p == "1":
        cetak()
        print('\nHarga per kg\n'
              '+------+---------+\n'
              '| 1 kg | Rp.6000 |\n'
              '+------+---------+\n'
              '\nProses\n'
              '+-------+-----------+\n'
              '| cepat | +Rp.10000 |\n'
              '+-------+-----------+\n')

    elif p == "2":
        menu = input("Menu\n"
                     "1. kiloan dan Lainnya\n"
                     "2. Kiloan\n"
                     "3. Lainnya\n"
                     "->")
        print("Formulir pengisisan data Laundry")
        nama = input("masukkan nama anda :\n"
                     "->")
        No = input("masukkan Nomor telephone anda :\n"
                   "->")
        if menu == "1":
            kilo = float(input("Berapa kilo pakaian anda :\n"
                               "->"))
            cetak()
            paket = int(input("masukkan Pilihan Anda :\n"
                              "->"))
            jum = int(input("masukkan Banyaknya pakaian :\n"
                            "->"))
        elif menu == "2":
            paket = "-"
            kilo = float(input("Berapa kilo pakaian anda :\n"
                               "->"))
        else:
            kilo = '-'
            cetak()
            paket = int(input("masukkan Pilihan Anda :\n"
                              "->"))
            jum = int(input("masukkan Banyaknya pakaian :\n"
                            "->"))
        jenis = input("Masukkan Jenis :\n"
                      "1. Cepat  (1 hari)\n"
                      "2. Normal (3 hari)\n"
                      "->")
        if jenis == "1" or jenis == "cepat":
            jenis = "Cepat"
            i = 1
            k = 10
        else:
            jenis = "Normal"
            i = 3
            k = 1
        tglmasuk = time.strftime("%d %B %Y")
        time = datetime.now() + timedelta(days=i)
        tglkeluar = time.strftime("%d %B %Y")
        print("Apakah Data di atas sudah Valid?")
        valid = input("Tekan y jika benar\n->").lower()
        if valid == 'y':
            pesanan.enqueue([urutan, nama, No, jenis, tglmasuk, tglkeluar])
            time = datetime.now()
            urutan += 1
            print("Data berhasil Masuk dalam Antrian")
        else:
            print("Data Tidak masuk dalam Antrian")
    elif p == "3":
        print("Daftar Pesanan")
        print("No\tNama\tTanggal Masuk\t\tTanggal Keluar")
        for i in range(pesanan.size() - 1, -1, -1):
            print("%d\t%.10s\t%s\t%s" % (
            pesanan.getdata(i, 0), pesanan.getdata(i, 1), pesanan.getdata(i, 4), pesanan.getdata(i, 5)))
        struks = input("Apakah anda ingin menampilkan struk pesanan? (y/n): ")
        if struks == "y":
            No = int(input("masukkan Nomor Antrian"))

            struk(pesanan, No * (-1))
        elif struks == "n":
            print()
        else:
            print("masukkan pilihan yang benar")
    elif p == "4":
        if not pesanan.isEmpty():
            pesanan.dequeue()
        else:
            print("tidak ada Antrian laundry")
    elif p == "5":
        print("Terima kasih")
        break
    else:
        print("pilikah anda salah")