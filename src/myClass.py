from pathlib import Path
from datetime import datetime

separators = {
    'data_mahasiswa.txt': ',',
    'data_kehadiran.txt': '_'
}

def write_log(action):
    """Menulis log ke file log"""
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    with open('DataBase/history.log','a') as log_file:
        log_file.write(f"{timestamp} - {action}\n")

class DataMahasiswa():
    """ objek untuk menyimpan data mahasiswa"""
    def __init__(self, nama, nim=None, filename=f'data_mahasiswa.txt'):
        """constructor class DataMahasiswa

        Args:
            nama (list): parameter untuk menyimpan nama mahasiswa bisa berupa list
            nim (list): parameter untuk menyimpan nim mahasiswa bisa berupa list
            filename (str, optional): nama file dimana data akan di simpan. Defaults to f'data_mahasiswa.txt'.
        """
        self.nama = nama
        self.nim = nim
        self.path = Path(f'dataBase/{filename}') # default directory (dimana data di simpan)
        

    

    def add(self): # set default filename = 'data/data_mahasiswa.txt'
        """menambahkan data mahasiswa ke database
        """
        try:
            if not self.path.exists(): # Jika file tidak ditemukan, buat file baru
                write_log(f"File tidak ditemukan, membuat file baru: {self.path}")
            
            with open(self.path, 'a') as file: # Buka file dengan mode append (a) dan mulai simpan data
                for nama, nim in zip(self.nama, self.nim): # Menggabungkan nama dan nim menjadi satu
                    file.write(f'{nama},{nim}\n') # Tulis data ke file dengan format: Nama,NIM
                    print(f"Data berhasil ditambahkan: {nama}, {nim}")
                    write_log(f"Data {nama}, {nim} berhasil ditambahkan ke {self.path}") 
        except PermissionError: # Jika user tidak memiliki izin untuk mengakses file
            print(f"Tidak memiliki izin untuk mengakses file '{self.path}'.")
        except Exception as e:
            print(f"Terjadi kesalahan: {e}")

    def exists(self):
        """mengecek apakah data mahasiswa yang akan diinputkan sudah ada di database"""
        try:
            with open(self.path, 'r') as file: # Buka file dengan mode read (r)
                for line in file: # Baca setiap baris di file
                    nama, nim = line.strip().split(',') # Pisah nama dan nim dengan koma
                    if nama in self.nama or nim in self.nim:
                        return True
                    else:
                        return False
        except FileNotFoundError: # Jika file tidak ditemukan
            print(f"File '{self.path}' tidak ditemukan.")



    def delete(self):
        try:
            with open(self.path, 'r') as file:
                lines = file.readlines()  # Baca semua baris di file

            # Filter data yang akan dihapus berdasarkan nama
            filtered = [line for line in lines if line.split(',', 1)[0].strip().lower() not in self.nama] #

            # tulis log data yang dihapus
            deleted_lines = [line for line in lines if line.split(',', 1)[0].strip().lower() in self.nama]
            for deleted in deleted_lines:
                print(f"Baris dihapus: {deleted.strip()}")
                write_log(f"Baris dihapus: {deleted.strip()} di file {self.path}")

            if not deleted_lines: # Jika tidak ada satu pun data yang dihapus
                print(f"Data dengan yg akan dihapus tidak ditemukan")
            else:
                with open(self.path, 'w') as file:
                    file.writelines(filtered)  # Tulis ulang data yang tersaring

        except FileNotFoundError:
            print(f"File '{self.path}' tidak ditemukan.")
        except Exception as e:
            print(f"Terjadi kesalahan saat menghapus data: {e}")



class BacaData():
    """ objek untuk membaca data mahasiswa"""
    def __init__(self, filename='data_mahasiswa.txt'): # set default filename = 'data/data_mahasiswa.txt'
        self.path = f'dataBase/{filename}'
        self.data = {} # dictionary untuk menyimpan data mahasiswa sementara

        try:
            with open(self.path, 'r') as file: # buka file data_mahasiswa.txt dengan mode read (r)
                for line in file: # baca setiap baris di file
                    nama, nim =  line.strip().split(',', 1) # pisah nama dan nim dengan koma','
                    self.data.update({nama:nim}) # tambahkan data mahasiswa ke dictionary data

        except FileExistsError: # error handling jika file tidak ditemukan
            print(f"File {self.path} tidak ditemukan")

        except Exception as err: # error handling
            print(f"Terjadi kesalahan saat membaca data: {err}")

    def print(self):
        """menampilkan data mahasiswa"""
        if not self.data: # cek apakah data mahasiswa kosong
            print('Data mahasiswa kosong')
        else:
            for nama, nim in self.data.items(): # iterasi setiap data mahasiswa
                print(f'Nama Lengkap: {nama}, NIM: {nim}') # tampilkan nim dan nama mahasiswa


class Kehadiran(DataMahasiswa):
    """ Kelas untuk menangani data kehadiran mahasiswa """

    def __init__(self, nama, kehadiran='Tidak Hadir', filename='data_kehadiran.txt'):
        super().__init__(nama, nim=None, filename=filename)  # Hanya menggunakan nama, nim diatur None
        self.kehadiran = kehadiran
    def add(self): # set default filename = 'data/data_mahasiswa.txt'
        """menambahkan data mahasiswa ke database
            filename: Parameter untuk menentukan file yang akan diisi data(direrctory default = dataBase) 
        """
        try:
            if not self.path.exists(): # Jika file tidak ditemukan, buat file baru
                write_log(f"File tidak ditemukan, membuat file baru: {self.path}")
            
            with open(self.path, 'a') as file: # Buka file dengan mode append (a) dan mulai simpan data
                    file.write(f'{self.nama} - {self.kehadiran}\n') # Tulis data ke file dengan format: self.nama,kehadiran
                    print(f"Data berhasil ditambahkan: {self.nama} - {self.kehadiran}")
                    write_log(f"Data {self.nama} - {self.kehadiran} berhasil ditambahkan ke {self.path}") 
        except PermissionError: # Jika user tidak memiliki izin untuk mengakses file
            print(f"Tidak memiliki izin untuk mengakses file '{self.path}'.")
        except Exception as e:
            print(f"Terjadi kesalahan: {e}")

    def exists(self):
        """ Mengecek apakah nama mahasiswa ada di data mahasiswa (override method) """       
        try:
            with open(self.path, 'r') as file:
                for line in file:
                    nama = line.strip().split(" - ")[0]  # hanya ambil nama
                    if nama == self.nama:
                        return True
                return False # Jika nama tidak ditemukan

        except FileNotFoundError:
            print(f"File '{self.path}' tidak ditemukan.")
            return False
        except Exception as e:
            print(f"Terjadi kesalahan: {e}")
            return False
    
    def print(self):
        """ Menampilkan data kehadiran mahasiswa """
        try:
            with open(self.path, 'r') as file:
                for line in file:
                    nama, kehadiran = line.strip().split(" - ")
                    print(f"Nama: {nama}, Kehadiran: {kehadiran}")
        except FileNotFoundError:
            print(f"File '{self.path}' tidak ditemukan.")
        except Exception as e:
            print(f"Terjadi kesalahan: {e}")

    def delete(self):
        try:
            with open(self.path, 'r') as file:
                lines = file.readlines()  # Baca semua baris di file

            # Filter data yang akan dihapus berdasarkan nama
            filtered = [line for line in lines if line.split(' - ', 1)[0].strip().lower() not in self.nama] #

            # tulis log data yang dihapus
            deleted_lines = [line for line in lines if line.split(' - ', 1)[0].strip().lower() in self.nama]
            for deleted in deleted_lines:
                print(f"Baris dihapus: {deleted.strip()}")
                write_log(f"Baris dihapus: {deleted.strip()} di file {self.path}")

            if not deleted_lines: # Jika tidak ada satu pun data yang dihapus
                print(f"Data dengan yg akan dihapus tidak ditemukan")
            else:
                with open(self.path, 'w') as file:
                    file.writelines(filtered)  # Tulis ulang data yang tersaring

        except FileNotFoundError:
            print(f"File '{self.path}' tidak ditemukan.")
        except Exception as e:
            print(f"Terjadi kesalahan saat menghapus data: {e}")
        
        

class FileManager():
    def __init__(self, filePath, logFile='history.log'):
        self.path = Path(filePath)
        self.log = Path(logFile)

    def delete(self):
        """Method untuk menghapus file"""
        
        # Validasi apakah file dengan path itu ada
        if not self.path.exists():
            print(f"File '{self.path}' tidak ditemukan.")
            return # Menghentikan eksekusi method delete()
        
        # Meminta konfirmasi user untuk menghapus file
        validation = input(f"File '{self.path}' akan dihapus, lanjutkan? (y/n): ").lower()
        
        if validation == 'y': # Jika user menyetujui penghapusan file
            try:
                self.path.unlink()  # Menghapus file
                print(f"File '{self.path}' berhasil dihapus.")
                write_log(f"File '{self.path}' berhasil dihapus.") # Menulis log ke file history.log
            except PermissionError: # Jika user tidak memiliki izin untuk menghapus file
                print(f"Tidak memiliki izin untuk menghapus file '{self.path}'.")
            except Exception as e: # Error handling
                print(f"Terjadi kesalahan saat menghapus file: {e}")
        
        elif validation == 'n': # Jika user membatalkan penghapusan file
            print(f"Penghapusan file '{self.path}' dibatalkan.")
        
        else: # Jika input user tidak valid
            print("Input tidak valid. Harap masukkan 'y' atau 'n'. Penghapusan file dibatalkan.")


