import csv
from PyPDF2 import PdfReader
import re

def extract_pdf_info(file_path):
    pdf = PdfReader(file_path)
    
    extracted_info = []
    for page_num in range(len(pdf.pages)):
        page = pdf.pages[page_num]
        content = page.extract_text()
        
        # Mencari bab, pasal, dan ayat dalam teks menggunakan regular expression
        bab_match = re.search(r'Bab\s*(\d+)', content)
        pasal_match = re.search(r'Pasal\s*(\d+)', content)
        ayat_match = re.search(r'Ayat\s*(\d+)', content)
        
        # Memeriksa keberadaan dan mengekstrak nilai bab, pasal, dan ayat jika cocok
        bab = bab_match.group(1) if bab_match else ''
        pasal = pasal_match.group(1) if pasal_match else ''
        ayat = ayat_match.group(1) if ayat_match else ''
        
        # Menambahkan hasil ke dalam list
        extracted_info.append([bab, pasal, ayat])
    
    return extracted_info

def save_to_csv(data, output_file):
    with open(output_file, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['Bab', 'Pasal', 'Ayat'])  # Menulis header
        writer.writerows(data)  # Menulis data baris per baris

# Menjalankan model dan menyimpan hasil ke dalam file CSV
pdf_file_path = r"D:\Lomba BDC\Semifinal BDC\Investasi-V1\1_UU_dan_PERPU\PERATURAN_PEMERINTAH_PENGGANTI_UNDANG-UNDANG_NOMOR_7_TAHUN_1962.pdf"  # Ubah dengan path file PDF yang ingin Anda ekstrak
output_csv_file = 'output.csv'  # Nama file CSV output

extracted_data = extract_pdf_info(pdf_file_path)
save_to_csv(extracted_data, output_csv_file)

print('Ekstraksi selesai. Hasil disimpan dalam file CSV:', output_csv_file)
