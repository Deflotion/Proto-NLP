import csv
import re

# Fungsi untuk melakukan ekstraksi dengan menggunakan regex
def extract_pasal(text):
    pasal = re.findall(r"Pasal\s+(\d+)", text, re.IGNORECASE)

    return ';'.join(pasal) if pasal else ''

# Nama file input dan output
input_file = 'output_model_8_v1.csv'
output_file = 'output3.csv'

# Buka file input dan buat file output
with open(input_file, 'r') as file_in, open(output_file, 'w', newline='') as file_out:
    reader = csv.reader(file_in)
    writer = csv.writer(file_out)

    # Menulis header untuk file output
    writer.writerow(['Pasal'])

    # Membaca baris-baris dari file input
    for row in reader:
        text = row[0]  # Asumsikan teks berada di kolom pertama

        # Mengekstrak informasi pasal menggunakan fungsi extract_pasal
        extracted_pasal = extract_pasal(text)

        # Menulis baris dengan informasi pasal yang diekstraksi ke dalam file output
        writer.writerow([extracted_pasal])

print("Ekstraksi pasal selesai. File output.csv telah dibuat.")
