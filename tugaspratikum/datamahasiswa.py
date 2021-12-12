dict = {}

def tambah():
    print('Tambah Data')
    nama = input("Masukan Nama      : ")
    nim = int(input("Masukan NIM    : "))
    tugas = int(input("Nilai Tugas  : "))
    uts = int(input("Nilai UTS      : "))
    uas = int(input("Nilai UAS      : "))
    akhir = tugas * 0.30 + uts * 0.35 + uas * 0.35
    dict[nama] = nim, uts, uas, tugas, akhir

def tampilkan():
    if dict.items():
            print("-"*75)
            print("                                 Daftar Nilai                             ") 
            print("-"*75)
            print("|No. |    Nama    |     NIM     |  TUGAS  |  UTS  |  UAS  |  Akhir       |")
            print("-"*75)
            i = 0 
            for y in dict.items():
                i += 1
                print("| {no:2} | {0:10} | {1:11} | {2:5} | {3:5} | {4:7} | {5:7}      |".format
                (y[0][:13], y[1][0], y[1][1], y[1][2], y[1][3], y[1][4], no=i))        
    else:
           
            print("-"*75)
            print("                                 Daftar Nilai                              ") 
            print("-"*75)
            print("|No. |    Nama    |     NIM     |  TUGAS  |  UTS  |  UAS  |  Akhir       |")
            print("-"*75)
            print("|                           TIDAK ADA DATA                               |") 
            print("-"*75)      

def hapus():
    print("Hapus Data")
    nama = input("Masukan Nama      : ")    
    if nama in dict.keys():
        del dict[nama]
        print()
        print('========================================')
        print('=============DATA TERHAPUS==============')
        print('========================================')
    else:
        print("Data {0} Tidak di Temukan".format(nama))

def ubah():
    print('         MENGUBAH DATA MAHASISWA         ')
    print('=========================================')
    nama = input("Masukan Nama         : ")
    if nama in dict.keys():
       nim = int(input("Masukan NIM     : "))
       tugas = int(input("Nilai Tugas  : "))
       uts = int(input("Nilai UTS      : "))
       uas = int(input("Nilai UAS      : "))
       akhir = tugas * 0.30 + uts * 0.35 + uas * 0.35                
       dict[nama] = nim, tugas, uts, uas, akhir
    else:
        print("Nama {0} Tidak di Tentukan".format(nama))

while True:
    print('=====================================')
    print('|    PROGRAM NILAI DATA MAHASISWA   |')
    print('=====================================')
    data = input('(L)ihat \n(T)ambah \n(U)bah \n(H)apus \n(K)eluar \nPilih Menu Yang Tersedia :')
    if data in ('l', 'L'):
        tampilkan()
    elif data in ('t','T'):
        tambah()
    elif data in ('u','U'):
        ubah()
    elif data in ('h','H'):
        hapus()
    elif data in ('k','K'):
        print("Terima Kasih")
        break
    else:
        print('     Pilih Menu Yang Tersedia       ')
        print('====================================')

