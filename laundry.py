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


#def banding(hari,bulan,tahun):
    

def struk(Data,No):
    print("\n"*5)
    print("▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒\n"
          "▒▒                 +--------------+                 ▒▒\n"
          "▒▒  +--------------| Struk Laundy |--------------+  ▒▒\n"
          "▒▒  |              +--------------+              |  ▒▒\n"
          "▒▒  |                                            |  ▒▒")
    print("        Nama           : %s"%(Data.getdata(No,1)))
    print("        Nomor Telepon  : %s"%(Data.getdata(No,2)))
    print("        Alamat         : %s"%(Data.getdata(No,3)))
    print("        Jenis Laundry")
    print("         -Kiloan")
    print("          -Berat       : %s"%(Data.getdata(No,4)))
    print("          -Strika      : %s"%(Data.getdata(No,5)))
    print("         -Satuan")
    print("          -Jenis       : %s"%(Data.getdata(No,6)))
    print("          -harga       : %s"%(Data.getdata(No,7)))
    print("          -Jumlah      : %s"%(Data.getdata(No,8)))
    print("        Proses         : %s"%(Data.getdata(No,9)))
    print("        Tanggal Masuk  : %s"%(Data.getdata(No,10)))
    print("        Tanggal Keluar : %s"%(Data.getdata(No,11)))
    print("        Biaya          : Rp.%d"%(Data.getdata(No,12)))
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
        try:
            biya=0
            menu=input("Menu\n"
                       "1. kiloan dan Lainnya\n"
                       "2. Kiloan\n"
                       "3. Lainnya\n"
                       "->")    
            print("Formulir pengisisan data Laundry")
            nama=input("Masukkan Nama :\n"
                       "->")
            nomr=int(input("Masukkan Nomor telephone :\n"
                     "->"))
            almt=input("Masukkan Alamat :\n"
                     "->")
            if menu == "1":
                kilo=float(input("Berapa kilo pakaian anda :\n"
                                 "->"))
                stka=int(input("Setrika ?\n1. Ya\n2. Tidak\n"
                             "->"))
                cetak()
                pakt=int(input("masukkan Pilihan Anda :\n"
                                "->"))
                jumh=int(input("masukkan Banyaknya pakaian :\n"
                               "->"))

                hpkt=hrgs[pakt-1][1]
                pakt=hrgs[pakt-1][0]

                if   stka== 1:
                    biya=(kilo*6000)+(hpkt*jumh) + 5000
                    stka="Ya"
                elif stka== 2:
                    biya=(kilo*6000)+(hpkt*jumh)
                    stka="Tidak"
            elif menu == "2":
                kilo=float(input("Berapa kilo pakaian anda :\n"
                               "->"))
                stka=input("Setrika ?\n1. Ya\n2. Tidak\n"
                           "->")
                hpkt='-'
                pakt='-'
                jumh="-"
                if   stka== 1:
                    biya=(kilo*6000) + 5000
                    stka="Ya"
                elif stka== 2:
                    biya=(kilo*6000)
                    stka="Tidak"
            elif menu == "3":
                cetak()
                pakt=int(input("masukkan Pilihan Anda :\n"
                               "->"))
                jumh=int(input("masukkan Banyaknya pakaian :\n"
                               "->"))
                kilo="-"
                stka= '_'
                hpkt=hrgs[pakt-1][1]
                pakt=hrgs[pakt-1][0]
                biya=hpkt*jumh
            jnis=int(input("Masukkan Jenis :\n"
                       "1. Cepat  (1 hari)\n"
                       "2. Normal (3 hari)\n"
                       "->"))
            if jnis == 1:
                i=1
                jnis="Cepat"
                biya=biya + 10000
            elif jnis == 2:
                i=3
                jnis="Normal"
            tglm=time.strftime("%d %B %Y")
            time=datetime.now() + timedelta(days=i)
            tglk=time.strftime("%d %B %Y")
            print("Apakah Data di atas sudah Valid?")
            vald = input("Tekan y jika benar\n->").lower()
            if vald == 'y':
                pesanan.enqueue([urut,nama,nomr,almt,kilo,stka,pakt,hpkt,jumh,jnis,tglm,tglk,biya])
                struk(pesanan,urut*-1)
                urut+=1
                print("Data berhasil Masuk dalam Antrian")
            else:
                print("Data Tidak masuk dalam Antrian")
        except:
            print("\n\tMaaf, Kesalahan Input\n")
    elif p=="3":
        print("Daftar Pesanan")
        print("No\tNama\tTanggal Masuk\t\tTanggal Keluar")
        for i in range(pesanan.size()-1,-1,-1):
            print("%d\t%.10s\t%s\t%s"%(pesanan.getdata(i,0),pesanan.getdata(i,1),pesanan.getdata(i,10),pesanan.getdata(i,11)))
        strk=input("Tekan y untuk menampilkan struk\n->")
        if strk=="y":
            No=int(input("masukkan Nomor Antrian\n->"))
            if No not in pesanan.getkolom(0):
                print("\n\tData Tidak Ada...\n")
            else:
                struk(pesanan,No*(-1))
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