import csv
import re
import PyPDF2

# Fungsi untuk membaca teks dari file PDF
def read_pdf(file_path):
    pdf_file = open(file_path, 'rb')
    pdf_reader = PyPDF2.PdfReader(pdf_file)

    text = ''
    for page in pdf_reader.pages:
        text += page.extract_text()

    pdf_file.close()
    return text

# Fungsi untuk mengekstrak informasi dari teks
def extract_information(text, file_name):
    # Pola regex untuk mencocokkan nomor peraturan dan tahun
    nomor_tahun_pattern = r'Nomor\sPeraturan:\s(\d+).*Tahun\s(\d{4})'

    # Pola regex untuk mencocokkan bab, pasal, dan ayat
    bab_pasal_ayat_pattern = r'(Bab\s[IVX]+)[\s\n]*((Pasal\s\d+)[\s\n]*((Ayat\s\d+\.)+\s?.*)*)'

    # Ekstraksi nomor peraturan dan tahun
    nomor_tahun_match = re.search(nomor_tahun_pattern, text)
    nomor_peraturan = nomor_tahun_match.group(1) if nomor_tahun_match else ''
    tahun_peraturan = nomor_tahun_match.group(2) if nomor_tahun_match else ''

    # Ekstraksi bab, pasal, dan ayat
    bab_pasal_ayat_matches = re.findall(bab_pasal_ayat_pattern, text)
    bab_pasal_ayat_list = []
    for match in bab_pasal_ayat_matches:
        bab = match[0]
        pasal = match[2]
        ayat = match[3]
        bab_pasal_ayat_list.append((bab, pasal, ayat))

    return nomor_peraturan, tahun_peraturan, bab_pasal_ayat_list

# Fungsi untuk menulis data ke file CSV
def write_to_csv(data, output_file):
    with open(output_file, 'w', newline='', encoding='utf-8') as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow(['Nomor Peraturan', 'Tahun', 'Tentang', 'Mengingat', 'Nama File', 'Bab', 'Pasal', 'Ayat'])
        writer.writerows(data)

# Main program
def main():
    pdf_file_path = r'D:\Lomba BDC\Semifinal BDC\Investasi-V1\1_UU_dan_PERPU\PERATURAN_PEMERINTAH_PENGGANTI_UNDANG-UNDANG_NOMOR_7_TAHUN_1962.pdf'  # Ganti dengan path file PDF yang ingin Anda baca
    output_csv_file = 'output.csv'  # Ganti dengan nama file CSV output

    # Membaca teks dari file PDF
    pdf_text = read_pdf(pdf_file_path)

    # Ekstraksi informasi dari teks
    nomor_peraturan, tahun_peraturan, bab_pasal_ayat_list = extract_information(pdf_text, pdf_file_path)

    # Menggabungkan hasil ekstraksi menjadi baris data tunggal
    extracted_data = []
    for bab, pasal, ayat in bab_pasal_ayat_list:
        extracted_data.append([
            nomor_peraturan,
            tahun_peraturan,
            '',
            '',
            pdf_file_path,
            bab,
            pasal,
            ayat
        ])

    # Menulis data ke dalam file CSV
    write_to_csv(extracted_data, output_csv_file)

    print("Data berhasil diekstraksi dan ditulis ke dalam file CSV.")

if __name__ == '__main__':
    main()
