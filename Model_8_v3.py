import PyPDF2
import os

# Fungsi untuk membaca teks dari file PDF
def read_pdf(file_path):
    pdf_file = open(file_path, 'rb')
    pdf_reader = PyPDF2.PdfReader(pdf_file)

    text = ''
    for page in pdf_reader.pages:
        text += page.extract_text()

    pdf_file.close()
    return text

# Fungsi untuk menulis teks ke file TXT
def write_to_txt(text, output_file):
    with open(output_file, 'w', encoding='utf-8') as txt_file:
        txt_file.write(text)

# Fungsi untuk membuat direktori jika belum ada
def create_directory(directory):
    if not os.path.exists(directory):
        os.makedirs(directory)

# Main program
def main():
    pdf_file_path = r'D:/Lomba BDC/Semifinal BDC/Investasi-V1/3_PERPRES/'
    file = input("Masukkan nama file PDF (tanpa ekstensi): ")
    name_files = f'{file}.pdf'
    output_path = r'D:/Lomba BDC/Semifinal BDC/hasil/3_PERPRES/'
    name_output = f'{file}.txt'
    output_txt_file = output_path + name_output

    # Membaca teks dari file PDF
    pdf_text = read_pdf(pdf_file_path + name_files)

    # Mengecek dan membuat direktori jika belum ada
    create_directory(output_path)

    # Menulis teks ke dalam file TXT
    write_to_txt(pdf_text, output_txt_file)

    print(f"Teks dari file '{name_files}' berhasil ditulis ke dalam '{name_output}.'")

if __name__ == '__main__':
    while True:
        try:
            main()
        except KeyboardInterrupt:
            break
