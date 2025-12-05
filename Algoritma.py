#NAMA :Cyntia angreni 
#kelas:SISTEM INFORMASI A.


# 1. Algoritma Stack (Tumpukan)
print("--- Algoritma Stack ---")
stack = []
# Push: Menambahkan elemen ke puncak
stack.append("Buku A")
stack.append("Buku B")
stack.append("Buku C")
print(f"Isi stack setelah push: {stack}")

# Pop: Mengambil elemen dari puncak
elemen_teratas = stack.pop()
print(f"Elemen yang di-pop: {elemen_teratas}")
print(f"Isi stack setelah pop: {stack}")
print("-" * 20 + "\n")


# 2. Algoritma Searching (Pencarian)
print("--- Algoritma Searching ---")
data_terurut = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
target = 70

def binary_search(arr, target):
    kiri, kanan = 0, len(arr) - 1
    while kiri <= kanan:
        tengah = (kiri + kanan) // 2
        if arr[tengah] == target:
            return f"Target {target} ditemukan di indeks {tengah}."
        elif arr[tengah] < target:
            kiri = tengah + 1
        else:
            kanan = tengah - 1
    return f"Target {target} tidak ditemukan."

print(f"Mencari {target} dalam data: {data_terurut}")
print(binary_search(data_terurut, target))
print(binary_search(data_terurut, 45)) # Contoh target tidak ada
print("-" * 20 + "\n")

# 3. Algoritma Pengurutan Data Dasar
print("--- Algoritma Pengurutan Dasar ---")
data_acak = [64, 34, 25, 12, 22, 11, 90]
print(f"Data sebelum diurutkan: {data_acak}")

def bubble_sort(arr):
    n = len(arr)
    # Salin array agar tidak mengubah array asli
    arr_copy = arr[:]
    for i in range(n):
        for j in range(0, n-i-1):
            if arr_copy[j] > arr_copy[j+1]:
                arr_copy[j], arr_copy[j+1] = arr_copy[j+1], arr_copy[j]
    return arr_copy

print(f"Hasil Bubble Sort: {bubble_sort(data_acak)}")
print("-" * 20 + "\n")


# 4. Algoritma Pengurutan Data Tingkat Lanjut
print("--- Algoritma Pengurutan Lanjut ---")
data_acak_2 = [29, 10, 14, 37, 13, 5, 20, 18]
print(f"Data sebelum diurutkan: {data_acak_2}")

def quick_sort(arr):
    # Salin array agar tidak mengubah array asli
    arr_copy = arr[:]
    if len(arr_copy) <= 1:
        return arr_copy
    else:
        pivot = arr_copy[len(arr_copy) // 2]
        kiri = [x for x in arr_copy if x < pivot]
        tengah = [x for x in arr_copy if x == pivot]
        kanan = [x for x in arr_copy if x > pivot]
        return quick_sort(kiri) + tengah + quick_sort(kanan)

print(f"Hasil Quick Sort: {quick_sort(data_acak_2)}")
print("-" * 20 + "\n")

