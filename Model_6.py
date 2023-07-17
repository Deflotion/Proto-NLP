import csv
import PyPDF2

# Fungsi untuk mendapatkan teks dari halaman PDF
def extract_text_from_pdf(file_path):
    pdf_file = open(file_path, 'rb')
    pdf_reader = PyPDF2.PdfReader(pdf_file)
    
    text = ''
    for page_num in range(len(pdf_reader.pages)):
        page = pdf_reader.pages[page_num]
        text += page.extract_text()
    
    pdf_file.close()
    return text

# Fungsi untuk menulis data ke file CSV
def write_to_csv(data, output_file):
    with open(output_file, 'w', newline='', encoding='utf-8') as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow(['Nomor Peraturan', 'Tahun', 'Tentang', 'Peraturan Terkait', 'Nama File', 'Bab', 'Pasal', 'Isi Ayat'])
        writer.writerows(data)

# Fungsi utama
def main():
    pdf_file_path = r'D:\Lomba BDC\Semifinal BDC\Investasi-V1\1_UU_dan_PERPU\PERATURAN_PEMERINTAH_PENGGANTI_UNDANG-UNDANG_NOMOR_7_TAHUN_1962.pdf'
    output_csv_file = 'output.csv'
    
    pdf_text = extract_text_from_pdf(pdf_file_path)
    
    # Proses parsing teks untuk mendapatkan data yang dibutuhkan
    data = []
    # Contoh parsing data, sesuaikan dengan format teks pada file PDF yang Anda miliki
    # Misalnya, jika informasi yang Anda cari selalu diawali dengan 'Nomor Peraturan:' diikuti oleh nomor peraturan, 
    # Anda dapat menggunakan regular expression atau metode string seperti 'split' untuk mendapatkan nomor peraturan.
    # Setelah Anda mendapatkan semua informasi yang diperlukan, tambahkan ke dalam data sebagai list.
    # Misalnya, data.append([nomor_peraturan, tahun, tentang, peraturan_terkait, nama_file, bab, pasal, isi_ayat])
    
    write_to_csv(data, output_csv_file)
    print("Output berhasil ditulis ke file CSV.")

if __name__ == '__main__':
    main()
