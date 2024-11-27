class DataMahasiswa():
    """ objek untuk menyimpan data mahasiswa"""
    def __init__(self, nama, nim):
        self.nama = nama
        self.nim = nim

    def add(self):
        """menambahkan data mahasiswa ke database"""

        
        try:
            with open('data/mahasiswa.txt', 'a') as file:  # buka file mahasiswa.txt dengan mode append (a)
                file.write(f'{self.nama},{self.nim}\n')  # tulis data dengan fornat Format: NIM,Nama
            print(f"Data berhasil ditambahkan: {self.nama}, {self.nim}")
        except Exception as e: # error handling
            print(f"Terjadi kesalahan saat menambahkan data: {e}")


class BacaData(DataMahasiswa):
    """ objek untuk membaca data mahasiswa"""
    def __init__(self, filename='data/mahasiswa.txt'): # set default filename = 'data/mahasiswa.txt'
        self.data = {} # dictionary untuk menyimpan data mahasiswa
        try:
            with open('data/mahasiswa.txt', 'r') as file: # buka file mahasiswa.txt dengan mode read (r)
                for line in file: # baca setiap baris di file
                    nama, nim =  line.strip().split(',', 1) # pisah nama dan nim dengan koma','
                    self.data.update({nama:nim}) # tambahkan data mahasiswa ke dictionary data
        except FileExistsError: # error handling jika file tidak ditemukan
            print(f"File {filename} tidak ditemukan")
        except Exception as err: # error handling
            print(f"Terjadi kesalahan saat membaca data: {err}")

    def print(self):
        """menampilkan data mahasiswa"""
        if not self.data:
            print('Data mahasiswa kosong')
        else:
            for nama, nim in self.data.items(): # iterasi setiap data mahasiswa
                print(f'Nama Lengkap: {nama}, NIM: {nim}') # tampilkan nim dan nama mahasiswa