# buatkan kode hitung matriks
# buatkan kode hitung matriks
import numpy as np

# Fungsi untuk menambahkan dua matriks
def tambah_matriks(A, B):
    return np.add(A, B)

# Fungsi untuk mengurangkan dua matriks
def kurang_matriks(A, B):
    return np.subtract(A, B)

# Fungsi untuk mengalikan dua matriks
def kali_matriks(A, B):
    return np.dot(A, B)

# Fungsi untuk transpose matriks
def transpose_matriks(A):
    return np.transpose(A)

# Contoh penggunaan
A = np.array([[1, 2], [3, 4]])
B = np.array([[5, 6], [7, 8]])

print("Matriks A:")
print(A)
print("Matriks B:")
print(B)

print("Penjumlahan Matriks A dan B:")
print(tambah_matriks(A, B))

print("Pengurangan Matriks A dan B:")
print(kurang_matriks(A, B))

print("Perkalian Matriks A dan B:")
print(kali_matriks(A, B))

print("Transpose Matriks A:")
print(transpose_matriks(A))