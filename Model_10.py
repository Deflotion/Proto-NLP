import csv
import pdfplumber

# Fungsi untuk membaca teks dari file PDF
def read_pdf(file_path):
    with pdfplumber.open(file_path) as pdf:
        text = ""
        for page in pdf.pages:
            text += page.extract_text()
    return text

# Fungsi untuk menulis data ke file CSV
def write_to_csv(data, output_file):
    with open(output_file, 'w', newline='', encoding='utf-8') as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow(['Nomor Peraturan', 'Tahun', 'Tentang', 'Mengingat', 'Nama File', 'Bab', 'Pasal', 'Ayat'])
        writer.writerows(data)

# Fungsi untuk mengekstrak informasi dari teks
def extract_information(text, file_name):
    # Implementasikan logika ekstraksi informasi sesuai format teks dalam file PDF
    # Misalnya, gunakan regex atau metode pemrosesan string untuk mengekstrak nomor peraturan, tahun, tentang, mengingat, bab, pasal, dan ayat

    nomor_peraturan = ''
    tahun_peraturan = ''
    tentang = ''
    mengingat = ''
    bab = ''
    pasal = ''
    ayat = ''

    # Ekstraksi informasi yang diinginkan dari teks

    return nomor_peraturan, tahun_peraturan, tentang, mengingat, bab, pasal, ayat

# Main program
def main():
    pdf_file_path = r'D:\Lomba BDC\Semifinal BDC\Investasi-V1\1_UU_dan_PERPU\PERATURAN_PEMERINTAH_PENGGANTI_UNDANG-UNDANG_NOMOR_7_TAHUN_1962.pdf'  # Ganti dengan path file PDF yang ingin Anda baca
    output_csv_file = 'output.csv'  # Ganti dengan nama file CSV output

    # Membaca teks dari file PDF
    pdf_text = read_pdf(pdf_file_path)

    # Ekstraksi informasi dari teks
    nomor_peraturan, tahun_peraturan, tentang, mengingat, bab, pasal, ayat = extract_information(pdf_text, pdf_file_path)

    # Menyusun data ekstraksi menjadi baris data tunggal
    extracted_data = [[nomor_peraturan, tahun_peraturan, tentang, mengingat, pdf_file_path, bab, pasal, ayat]]

    # Menulis data ke dalam file CSV
    write_to_csv(extracted_data, output_csv_file)

    print("Data berhasil diekstraksi dan ditulis ke dalam file CSV.")

if __name__ == '__main__':
    main()
