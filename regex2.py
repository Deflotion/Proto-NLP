import csv
import re

# Fungsi untuk melakukan ekstraksi dengan menggunakan regex
def extract_mengingat(text):
    kalimat = re.findall(r"(?<=Mengingat:)(.*?)(?=(?:\.\s*?[A-Z]\.|$))", text, re.IGNORECASE | re.DOTALL)

    return [kal.strip() for kal in kalimat] if kalimat else []

# Nama file input dan output
input_file = 'output_model_8_v1.csv'
output_file = 'output6.csv'

# Buka file input dan buat file output
with open(input_file, 'r') as file_in, open(output_file, 'w', newline='') as file_out:
    reader = csv.reader(file_in)
    writer = csv.writer(file_out)

    # Menulis header untuk file output
    writer.writerow(['Mengingat'])

    # Membaca baris-baris dari file input
    for row in reader:
        text = row[0]  # Asumsikan teks berada di kolom pertama

        # Mengekstrak informasi Mengingat menggunakan fungsi extract_mengingat
        extracted_mengingat = extract_mengingat(text)

        # Menulis setiap baris dengan informasi Mengingat yang diekstraksi ke dalam file output
        for item in extracted_mengingat:
            writer.writerow([item])

print("Ekstraksi Mengingat selesai. File output.csv telah dibuat.")
