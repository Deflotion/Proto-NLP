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

# Fungsi untuk menulis teks ke file TXT
def write_to_txt(text, output_file):
    with open(output_file, 'w', encoding='utf-8') as txt_file:
        txt_file.write(text)

# Main program
def main():
    pdf_file_path = r'D:/Lomba BDC/Semifinal BDC/Investasi-V1/4_PERMEN/MENPERIN/'
    file = 'PERMEN_PERIN_64MINDPER72016_2016'
    name_files = f'{file}.pdf'# Ganti dengan path file PDF yang ingin Anda baca
    output_path = r'D:/Lomba BDC/Semifinal BDC/hasil/4_PERMEN/MENPERIN/'
    name_output = f'{file}.txt'
    output_txt_file = output_path + name_output  # Ganti dengan nama file TXT output

    # Membaca teks dari file PDF
    pdf_text = read_pdf(pdf_file_path+name_files)

    # Menulis teks ke dalam file TXT
    write_to_txt(pdf_text, output_txt_file)

    print(f"Teks dari file '{name_files}' berhasil ditulis ke dalam '{name_output}.'")

if __name__ == '__main__':
    main()

