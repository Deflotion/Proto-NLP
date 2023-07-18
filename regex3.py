import re
import csv

file_input = 'output.txt'
file_output = 'perundang-undangan.csv'

# Membaca isi file teks
with open(file_input, 'r') as file:
    teks = file.read()

# Pola regex untuk mengekstrak informasi
pola_regex = r'(?:(Bab\s+(\d+))?\s+)?Pasal\s+(\d+)\s*(?::\s*Ayat\s+(\d+))?\s*([^.]+)'

# Mencocokkan pola regex dalam teks dan mengekstrak informasi
hasil_ekstraksi = re.findall(pola_regex, teks)

# Menyimpan hasil ekstraksi ke dalam file CSV
with open(file_output, 'w', newline='') as file_csv:
    penulis_csv = csv.writer(file_csv)
    penulis_csv.writerow(['Bab', 'Pasal', 'Ayat', 'Teks'])
    penulis_csv.writerows(hasil_ekstraksi)

print(f"Hasil ekstraksi telah disimpan dalam file: {file_output}")
