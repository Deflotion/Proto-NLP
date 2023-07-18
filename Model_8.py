# import csv
# import PyPDF2

# # Fungsi untuk membaca teks dari file PDF
# def read_pdf(file_path):
#     pdf_file = open(file_path, 'rb')
#     pdf_reader = PyPDF2.PdfReader(pdf_file)

#     text = ''
#     for page in pdf_reader.pages:
#         text += page.extract_text()

#     pdf_file.close()
#     return text

# # Fungsi untuk menulis teks ke file CSV
# def write_to_csv(text, output_file):
#     with open(output_file, 'w', newline='', encoding='utf-8') as csv_file:
#         writer = csv.writer(csv_file)
#         writer.writerow(['Teks'])
#         writer.writerow([text])

# # Main program
# def main():
#     pdf_file_path = r'D:\Lomba BDC\Semifinal BDC\Investasi-V1\1_UU_dan_PERPU\PERATURAN_PEMERINTAH_PENGGANTI_UNDANG-UNDANG_NOMOR_7_TAHUN_1962.pdf'   # Ganti dengan path file PDF yang ingin Anda baca
#     output_csv_file = 'output.csv'  # Ganti dengan nama file CSV output

#     # Membaca teks dari file PDF
#     pdf_text = read_pdf(pdf_file_path)

#     # Menulis teks ke dalam file CSV
#     write_to_csv(pdf_text, output_csv_file)

#     print("Teks dari file PDF berhasil ditulis ke dalam file CSV.")

# if __name__ == '__main__':
#     main()


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
    pdf_file_path = r'D:/Lomba BDC/Semifinal BDC/Investasi-V1/1_UU_dan_PERPU/'
    file = '2022perpu002'
    name_files = f'{file}.pdf'# Ganti dengan path file PDF yang ingin Anda baca
    output_path = r'D:/Lomba BDC/Semifinal BDC/hasil/1_UU_dan_PERPU/'
    output_txt_file = output_path + f'{file}.txt'  # Ganti dengan nama file TXT output

    # Membaca teks dari file PDF
    pdf_text = read_pdf(pdf_file_path+name_files)

    # Menulis teks ke dalam file TXT
    write_to_txt(pdf_text, output_txt_file)

    print("Teks dari file PDF berhasil ditulis ke dalam file TXT.")

if __name__ == '__main__':
    main()
