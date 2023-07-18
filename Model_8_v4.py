import PyPDF2
import os
import docx2txt

# Fungsi untuk membaca teks dari file PDF
def read_pdf(file_path):
    pdf_file = open(file_path, 'rb')
    pdf_reader = PyPDF2.PdfReader(pdf_file)

    text = ''
    for page in pdf_reader.pages:
        text += page.extract_text()

    pdf_file.close()
    return text

# Fungsi untuk membaca teks dari file DOC
def read_doc(file_path):
    text = docx2txt.process(file_path)
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
    pdf_file_path = r'D:/Lomba BDC/Semifinal BDC/Investasi-V1/4_PERMEN/BKPM/'
    doc_file_path = r'D:/Lomba BDC/Semifinal BDC/Investasi-V1/4_PERMEN/BKPM/DOC/'
    file = 'KEPMGK_INVBKPM_12SK1999_1999'
    name_files = f'{file}.pdf'
    output_path = r'D:/Lomba BDC/Semifinal BDC/hasil/4_PERMEN/BKPM/'
    name_output = f'{file}.txt'
    output_txt_file = output_path + name_output

    # Mengecek dan membuat direktori jika belum ada
    create_directory(output_path)

    if os.path.exists(pdf_file_path + name_files):
        # Membaca teks dari file PDF
        pdf_text = read_pdf(pdf_file_path + name_files)
        # Menulis teks ke dalam file TXT
        write_to_txt(pdf_text, output_txt_file)
        print(f"Teks dari file '{name_files}' berhasil ditulis ke dalam '{name_output}'.")
    elif os.path.exists(doc_file_path + f'{file}.doc'):
        # Membaca teks dari file DOC
        doc_text = read_doc(doc_file_path + f'{file}.doc')
        # Menulis teks ke dalam file TXT
        write_to_txt(doc_text, output_txt_file)
        print(f"Teks dari file '{file}.doc' berhasil ditulis ke dalam '{name_output}'.")
    else:
        print("File tidak ditemukan.")

if __name__ == '__main__':
    main()
