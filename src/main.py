from myClass import *


def menu():
    print("Menu:")
    print("\t1. Tambah Data Mahasiswa")
    print("\t2. Hapus Data Mahasiswa")
    print("\t3. Lihat Data Mahasiswa")
    print("\t4. Tambah Data Kehadiran")
    print("\t5. Hapus Data Kehadiran")
    print("\t6. Hapus File")
    print("\t7. Keluar")
    try:
        choice = int(input("Masukkan pilihan: "))
    except ValueError: # error handling jika input bukan angka
        print("Pilihan tidak valid harap masukkan angka 1-5")
        return menu()
    if choice not in range(1, 10): # jika input tidak di rentang 1-5
        print("Pilihan tidak valid harap masukkan angka 1-5")
        return menu() # panggil fungsi menu() lagi untuk mengulang input
    
    return choice

def TambahDataMahasiswa():
    """fungsi untuk menambahkan data mahasiswa"""
    print("Masukkan data mahasiswa: ")
    nama = input("\tMasukkan Nama Lengkap : ")
    nim = input("\tMasukkan NIM : ")

    nama = [item.strip() for item in nama.split(',')] # pisah nama dengan koma
    nim = [item.strip() for item in nim.split(',')] # pisah nim dengan koma

    if len(nama) != len(nim): 
        print("Data tidak valid. jumlah data nim dan nama tidak sama") # cek apakah jumlah nama dan nim sama
        return TambahDataMahasiswa() # panggil fungsi TambahDataMahasiswa() lagi untuk mengulang input

    dataMahasiswa = DataMahasiswa(nama, nim) # buat objek DataMahasiswa dengan nama dan nim sebagai parameter
    if dataMahasiswa.exists():
        print("Salah satu data mahasiswa sudah ada di database")
        return TambahDataMahasiswa() # panggil fungsi TambahDataMahasiswa() lagi untuk mengulang input
    else:
        dataMahasiswa.add() # panggil method add() dari class DataMahasiswa untuk menambahkan data mahasiswa

def HapusDataMahasiswa():
    """fungsi untuk menghapus data mahasiswa"""
    print("Masukkan data mahasiswa yang akan dihapus: ")
    nama = input("\tMasukkan Nama Mahasiswa: ")
    nama = [item.strip().lower() for item in nama.split(',')] # pisah nama dengan koma

    dataMahasiswa = DataMahasiswa(nama)

    dataMahasiswa.delete() # panggil method delete() dari class DataMahasiswa untuk menghapus data mahasiswa


def LihatDataMahasiswa():
    """fungsi untuk menampilkan data mahasiswa"""
    BacaData().print() # panggil method print() dari class BacaData untuk menampilkan data mahasiswa

def TambahDataKehadiran():
    """fungsi untuk menambahkan data kehadiran mahasiswa"""
    print("Menghapus data mahasiswa: ")
    nama = input("\tMasukkan Nama Mahasiswa: ")
    kehadiran = input("\tMasukkan Kehadiran (Hadir/Tidak Hadir): ").lower()



    if kehadiran not in ['hadir', 'tidak hadir']: # cek apak2ah input kehadiran valid
        print("Kehadiran tidak valid")
        return TambahDataKehadiran() # panggil fungsi TambahDataKehadiran() lagi untuk mengulang input
    hadir = Kehadiran(nama, kehadiran) # buat objek Kehadiran dengan nama dan kehadiran sebagai parameter
    if hadir.exists():
        print(f"Nama {nama} sudah ada di daftar")
        return TambahDataKehadiran()
    else:
        hadir.add() # panggil method add() dari class Kehadiran untuk menambahkan data kehadiran mahasiswa

def HapusDataKehadiran():
    print("Menghapus data kehadiran mahasiswa: ")
    nama = input("\tMasukkan Nama Mahasiswa: ")
    nama = [item.strip().lower() for item in nama.split(',')] # pisah nama dengan koma

    dataKehadiran = Kehadiran(nama)
    dataKehadiran.delete() # panggil method delete() dari class DataMahasiswa untuk menghapus data mahasiswa


def HapusFile():
    fileName = input("Masukkan nama file yang akan dihapus (nama.txt): ")
    FileManager(f'dataBase/{fileName}').delete()
    
def main(): # PROGRAM UTAMA
    print("------Selamat datang di program Data Mahasiswa----")
    while True:
        choice = menu()
        if choice == 1:
            TambahDataMahasiswa() 
        elif choice == 2:
            HapusDataMahasiswa()
        elif choice == 3:
            LihatDataMahasiswa()
        elif choice == 4:
            TambahDataKehadiran()
        elif choice == 5:
            HapusDataKehadiran()
        elif choice == 6:
            HapusFile()
        elif choice == 7:
            print("Terima kasih telah menggunakan program ini")
            break
        else:
            print("Pilihan tidak valid")


if __name__ == '__main__':
    main() # panggil fungsi main() jika script dijalankan langsung




