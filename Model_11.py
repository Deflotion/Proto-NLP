import csv
import re
import PyPDF2

def read_pdf(file_path):
    pdf_file = open(file_path, 'rb')
    pdf_reader = PyPDF2.PdfReader(pdf_file)

    text = ''
    for page in pdf_reader.pages:
        text += page.extract_text()

    pdf_file.close()
    return text

def extract_information(text, file_name):
    nomor_tahun_pattern = r'Nomor\sPeraturan:\s(\d+).*Tahun\s(\d{4})'
    tentang_pattern = r'Tentang:\s(.+?)(?=\n\n|$)'
    mengingat_pattern = r'Mengingat:\s(.+?)(?=\n\n|$)'
    bab_pasal_ayat_pattern = r'(Bab\s[IVX]+)[\s\n]*((Pasal\s\d+)[\s\n]*((Ayat\s\d+\.)+\s?.*)*)'

    nomor_peraturan = ''
    tahun_peraturan = ''
    tentang = ''
    mengingat = ''
    bab = ''
    pasal = ''
    ayat = ''
    
    nomor_tahun_match = re.search(nomor_tahun_pattern, text)
    if nomor_tahun_match:
        nomor_peraturan = nomor_tahun_match.group(1)
        tahun_peraturan = nomor_tahun_match.group(2)

    tentang_match = re.search(tentang_pattern, text)
    if tentang_match:
        tentang = tentang_match.group(1).strip()

    mengingat_match = re.search(mengingat_pattern, text)
    if mengingat_match:
        mengingat = mengingat_match.group(1).strip()

    bab_pasal_ayat_matches = re.findall(bab_pasal_ayat_pattern, text)
    bab_pasal_ayat_list = []
    for match in bab_pasal_ayat_matches:
        bab = match[0]
        pasal = match[2]
        ayat = match[3]
        bab_pasal_ayat_list.append((bab, pasal, ayat))

    return nomor_peraturan, tahun_peraturan, tentang, mengingat, bab_pasal_ayat_list

def write_to_csv(data, output_file):
    with open(output_file, 'w', newline='', encoding='utf-8') as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow(['Nomor Peraturan', 'Tahun', 'Tentang', 'Mengingat', 'Bab', 'Pasal', 'Ayat'])
        for nomor, tahun, tentang, mengingat, bab, pasal, ayat in data:
            for i in range(len(bab)):
                writer.writerow([nomor, tahun, tentang, mengingat, bab[i], pasal[i], ayat[i]])

def main():
    pdf_file_path = r'D:\Lomba BDC\Semifinal BDC\Investasi-V1\1_UU_dan_PERPU\PERATURAN_PEMERINTAH_PENGGANTI_UNDANG-UNDANG_NOMOR_7_TAHUN_1962.pdf'  # Ganti dengan path file PDF yang ingin Anda baca
    output_csv_file = 'output.csv'  # Ganti dengan nama file CSV output

    pdf_text = read_pdf(pdf_file_path)
    nomor_peraturan, tahun_peraturan, tentang, mengingat, bab_pasal_ayat_list = extract_information(pdf_text, pdf_file_path)

    extracted_data = []
    for bab, pasal, ayat in bab_pasal_ayat_list:
        extracted_data.append((nomor_peraturan, tahun_peraturan, tentang, mengingat, bab, pasal, ayat))

    write_to_csv(extracted_data, output_csv_file)

    print("Data berhasil diekstraksi dan ditulis ke dalam file CSV.")

if __name__ == '__main__':
    main()
