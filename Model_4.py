import PyPDF2
import re
import csv

def extract_bab_pasal(filename):
    with open(filename, 'rb') as file:
        pdf_reader = PyPDF2.PdfReader(file)
        bab_pasal_dict = {}
        current_bab = ''
        current_pasal = ''
        current_isi_pasal = ''
        
        for page in pdf_reader.pages:
            text = page.extract_text()
            lines = text.split('\n')

            for line in lines:
                line = line.strip()
                if line.lower().startswith('bab '):
                    current_bab = line
                elif re.match(r'pasal\s+\d+', line, re.IGNORECASE):
                    if current_pasal and current_isi_pasal:
                        bab_pasal_dict[current_pasal] = current_isi_pasal.strip()
                    current_pasal = line
                    current_isi_pasal = ''
                elif current_pasal:
                    current_isi_pasal += line + '\n'

        if current_pasal and current_isi_pasal:
            bab_pasal_dict[current_pasal] = current_isi_pasal.strip()

    return bab_pasal_dict

def save_to_csv(data, csv_filename):
    with open(csv_filename, 'w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(['Pasal', 'Isi Pasal'])
        for pasal, isi_pasal in data.items():
            writer.writerow([pasal, isi_pasal])

# Menggunakan contoh file "peraturan.pdf"
file_path = r"D:\Lomba BDC\Semifinal BDC\Investasi-V1\1_UU_dan_PERPU\2022perpu002.pdf"
hasil_ekstraksi = extract_bab_pasal(file_path)

# Menyimpan hasil ekstraksi ke file CSV
csv_filename = "hasil_ekstraksi.csv"
save_to_csv(hasil_ekstraksi, csv_filename)

print("Data telah disimpan dalam file CSV:", csv_filename)
