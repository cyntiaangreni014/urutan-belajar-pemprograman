

#Variabel Statis: Ukuran dan lokasi memori ditentukan saat program dikompilasi (compile-time). Memori ini dialokasikan sekali dan tetap ada selama program berjalan.
#Variabel Dinamis: Memori dialokasikan saat program berjalan (run-time). Ukurannya bisa berubah sesuai kebutuhan.

#5 Variabel Statis dan Dinamis
print("--- 1.5 Variabel Statis dan Dinamis ---")
# Di Python, alokasi memori dikelola secara otomatis (dinamis).
# Variabel statis (class variable) vs variabel instance (dinamis dalam konteks objek)
class Mobil:
    # Variabel statis (milik class, sama untuk semua objek)
    jumlah_roda = 4

    def __init__(self, warna):
        # Variabel dinamis (instance variable, beda untuk tiap objek)
        self.warna = warna

mobil_merah = Mobil("Merah")
mobil_biru = Mobil("Biru")

print(f"Variabel Statis (semua mobil punya): Roda = {Mobil.jumlah_roda}")
print(f"Variabel Dinamis (spesifik objek): Warna mobil 1 = {mobil_merah.warna}")
print(f"Variabel Dinamis (spesifik objek): Warna mobil 2 = {mobil_biru.warna}")
print("-" * 20 + "\n")

