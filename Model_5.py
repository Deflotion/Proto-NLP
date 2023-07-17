import csv
import fitz
import re

def extract_information(pdf_path):
    doc = fitz.open(pdf_path)
    data = []
    
    for page in doc:
        text = page.get_text()
        
        bab_match = re.search(r'BAB ([\d\w\s]+)', text, re.IGNORECASE)
        pasal_match = re.search(r'PASAL ([\d\w\s]+)', text, re.IGNORECASE)
        ayat_match = re.search(r'AYAT ([\d\w\s]+)', text, re.IGNORECASE)
        
        bab = bab_match.group(1).strip() if bab_match else ''
        pasal = pasal_match.group(1).strip() if pasal_match else ''
        ayat = ayat_match.group(1).strip() if ayat_match else ''
        
        if bab and pasal and ayat:
            data.append([bab, pasal, ayat])
    
    doc.close()
    return data

def save_to_csv(data, csv_path):
    with open(csv_path, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Bab', 'Pasal', 'Ayat'])
        writer.writerows(data)
    print(f"Data berhasil disimpan dalam file CSV: {csv_path}")

# Contoh penggunaan
pdf_path = r"D:\Lomba BDC\Semifinal BDC\Investasi-V1\1_UU_dan_PERPU\PERATURAN_PEMERINTAH_PENGGANTI_UNDANG-UNDANG_NOMOR_7_TAHUN_1962.pdf"
csv_path = 'file_baru.csv'

data = extract_information(pdf_path)
save_to_csv(data, csv_path)
