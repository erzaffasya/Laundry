from datetime import timedelta, datetime
from time import sleep
from Antrian import *

time = datetime.now()
pesanan = Queue()
hrgs=[['Rompi  ',10000],
      ['Jaket  ',10000],
      ['selimut',15000],
      ['sepatu ',15000]]
hrgk=[['1 kg',6000]]
urut=1






def struk(Data,No):
    print("\n"*5)
    print("▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒\n"
          "▒▒                 +--------------+                 ▒▒\n"
          "▒▒  +--------------| Struk laundy |--------------+  ▒▒\n"
          "▒▒  |              +--------------+              |  ▒▒\n"
          "▒▒  |                                            |  ▒▒")
    print("        Nama           : %s"%(Data.getdata(No,1)))
    print("        Nomor Telepon  : %s"%(Data.getdata(No,2)))
    print("        Alamat         : %s"%(Data.getdata(No,3)))
    print("        Jenis Laundry\n"
          "         -Kiloan\n"
          "          -Berat       : %s"%(Data.getdata(No,4)))
    print("          -Strika      : %s"%(Data.getdata(No,5)))
    print("         -Satuan\n"
          "          -Jenis       : %s"%(Data.getdata(No,6)))
    print("          -Jumlah      : %s"%(Data.getdata(No,7)))
    print("        Proses         : %s"%(Data.getdata(No,8)))
    print("        Tanggal Masuk  : %s"%(Data.getdata(No,9)))
    print("        Tanggal Keluar : %s"%(Data.getdata(No,10)))
    print("        Biaya          : %s"%(Data.getdata(No,11)))
    print("▒▒  |                                            |  ▒▒\n"
          "▒▒  |                                            |  ▒▒\n"
          "▒▒  +--------------------------------------------+  ▒▒\n"
          "▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒")
    print("\n"*5)
    input("Tekan enter....")
    
          

def cetak():
    print('Berikut Daftar Harga\n'
          '+----+-------------+----------+\n'
          '+ No | Paket       |   Harga  |\n'
          '+----+-------------+----------+')
    for i in range(len(hrgs)):
        print("| %d  | %s     |   %d  |"%(i+1,hrgs[i][0],hrgs[i][1]))
    print('+----+-------------+----------+')
    

while True:
    print("="*50)
    print("Menu :\n"
          "1. Daftar Harga\n"
          "2. Pesanan\n"
          "3. Cek Pesanan\n"
          "4. Proses Antrian\n"
          "5. Keluar\n")
    p=input("Masukkan pilihan anda :\n->")
    print("="*50)    
    if p=="1":
        cetak()
        print('\nHarga per kg\n'
              '+------+---------+\n'
              '| 1 kg | Rp.6000 |\n'
              '+------+---------+\n'
              '\nProses\n'
              '+--------+-----------+\n'
              '| cepat  | +Rp.10000 |\n'
              '| strika | +Rp.5000  |\n'
              '+--------+-----------+\n')
        input("\nTekan enter....")
    elif p=="2":
        biya=0
        menu=input("Menu\n"
                   "1. kiloan dan Lainnya\n"
                   "2. Kiloan\n"
                   "3. Lainnya\n"
                   "->")    
        print("Formulir pengisisan data Laundry")
        nama=input("Masukkan Nama :\n"
                   "->")
        nomr=input("Masukkan Nomor telephone :\n"
                 "->")
        almt=input("Masukkan Alamat :\n"
                 "->")
        if menu == "1":
            kilo=float(input("Berapa kilo pakaian anda :\n"
                             "->"))
            stka=input("Setrika ?\n1. Ya\n2. Tidak\n"
                         "->")
            if stka=='1':
                stka=5000
            else:
                stka=0
            
            cetak()
            pakt=int(input("masukkan Pilihan Anda :\n"
                            "->"))
            jumh=int(input("masukkan Banyaknya pakaian :\n"
                           "->"))
            pakt=hrgs[pakt-1][1]
            biya=(kilo*6000)+(pakt*jumh)
        elif menu == "2":
            pakt="-"
            kilo=float(input("Berapa kilo pakaian anda :\n"
                           "->"))
            stka=input("Setrika ?\n1. Ya\n2. Tidak\n"
                       "->")
            jumh="-"
            biya=kilo*6000
        else:
            kilo ="-"
            stka = '_'
            cetak()
            pakt=int(input("masukkan Pilihan Anda :\n"
                           "->"))
            jumh=int(input("masukkan Banyaknya pakaian :\n"
                           "->"))
            pakt=hrgs[pakt-1][1]
            biya=pakt*jumh
        jnis=input("Masukkan Jenis :\n"
                   "1. Cepat  (1 hari)\n"
                   "2. Normal (3 hari)\n"
                   "->")
        if jnis == "1" or jnis == "cepat":
            jnis="Cepat"
            i=1
            k=10
        else:
            jnis="Normal"
            i=3
            k=1
        tglm=time.strftime("%d %B %Y")
        time=datetime.now() + timedelta(days=i)
        tglk=time.strftime("%d %B %Y")
        print("Apakah Data di atas sudah Valid?")
        vald = input("Tekan y jika benar\n->").lower()
        if vald == 'y':
            pesanan.enqueue([urut,nama,nomr,almt,kilo,stka,jnis,jumh,jnis,tglm,tglk,biya])
            time = datetime.now()
            urut+=1
            print("Data berhasil Masuk dalam Antrian")
        else:
            print("Data Tidak masuk dalam Antrian")
    elif p=="3":
        print("Daftar Pesanan")
        print("No\tNama\tTanggal Masuk\t\tTanggal Keluar")
        for i in range(pesanan.size()-1,-1,-1):
            print("%d\t%.10s\t%s\t%s"%(pesanan.getdata(i,0),pesanan.getdata(i,1),pesanan.getdata(i,9),pesanan.getdata(i,10)))
        strk=input("Apakah anda ingin menampilkan struk pesanan? (y/n): ")
        if strk=="y":
            No=int(input("masukkan Nomor Antrian"))
            struk(pesanan,No*(-1))
        elif strk=="n":
            print()
        else:
            print("masukkan pilihan yang benar")
    elif p=="4":
        if not pesanan.isEmpty():
            pesanan.dequeue()
        else:
            print("tidak ada Antrian laundry")
    elif p=="5":
        print("Terima kasih")
        break
    else:
        print("pilikah anda salah")
