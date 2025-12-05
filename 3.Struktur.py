#NAMA :Cyntia angreni
#kelas: SISTEM INFORMASI A.

#Struktur adalah tipe data komposit yang memungkinkan Anda menggabungkan beberapa variabel dengan tipe data yang berbeda di bawah satu nama

#konsep struktur(diimplemtasikan dengan kelas)
print("--- konsep struktur kelas (class) ---")
class Karyawan:
    """
    Class ini merepresentasikan struktur data seorang karyawan,
    menggabungkan nama (string), id (integer), dan gaji (float).
    """
    def __init__(self, nama, id_karyawan, gaji):
        self.nama = nama
        self.id_karyawan = id_karyawan
        self.gaji = gaji

    def tampilkan_info(self):
        return f"ID: {self.id_karyawan}, Nama: {self.nama}, Gaji: Rp{self.gaji:,.2f}