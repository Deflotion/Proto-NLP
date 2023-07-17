import csv
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

# Fungsi untuk memproses teks dan mengekstrak informasi yang dibutuhkan
def extract_information(text, file_name):
    # List kosong untuk menyimpan hasil ekstraksi
    extracted_data = []

    # Proses ekstraksi data sesuai format peraturan yang ada dalam teks
    # Misalnya, jika format teks yang mengandung nomor peraturan selalu diawali dengan 'Nomor Peraturan:' diikuti oleh nomor peraturan, 
    # Anda dapat menggunakan regular expression atau metode string seperti 'split' untuk mendapatkan nomor peraturan.
    # Setelah Anda mendapatkan semua informasi yang diperlukan, tambahkan ke dalam extracted_data sebagai list.
    # Misalnya, extracted_data.append([nomor_peraturan, tahun, tentang, peraturan_terkait, file_name, bab, pasal, isi_ayat])

    return extracted_data

# Fungsi untuk menulis data ke file CSV
def write_to_csv(data, output_file):
    with open(output_file, 'w', newline='', encoding='utf-8') as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow(['Nomor Peraturan', 'Tahun', 'Tentang', 'Peraturan Terkait', 'Nama File', 'Bab', 'Pasal', 'Isi Ayat'])
        writer.writerows(data)

# Main program
def main():
    pdf_file_path = r'D:\Lomba BDC\Semifinal BDC\Investasi-V1\1_UU_dan_PERPU\PERATURAN_PEMERINTAH_PENGGANTI_UNDANG-UNDANG_NOMOR_7_TAHUN_1962.pdf'  # Ganti dengan path file PDF yang ingin Anda baca
    output_csv_file = 'output.csv'  # Ganti dengan nama file CSV output

    # Membaca teks dari file PDF
    pdf_text = read_pdf(pdf_file_path)

    # Ekstraksi informasi dari teks
    extracted_data = extract_information(pdf_text, pdf_file_path)

    # Menulis data ke dalam file CSV
    write_to_csv(extracted_data, output_csv_file)

    print("Data berhasil diekstraksi dan ditulis ke dalam file CSV.")

if __name__ == '__main__':
    main()
