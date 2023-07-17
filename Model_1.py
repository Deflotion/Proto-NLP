import PyPDF2

def extract_bab_pasal(filename):
    with open(filename, 'rb') as file:
        pdf_reader = PyPDF2.PdfReader(file)

        bab = ''
        pasal = ''
        bab_pasal_dict = {}

        for page in pdf_reader.pages:
            text = page.extract_text()
            lines = text.split('\n')

            for line in lines:
                if line.lower().startswith('bab '):
                    bab = line.strip()
                    pasal = ''
                elif line.lower().startswith('pasal '):
                    pasal = line.strip()
                    bab_pasal_dict[bab] = pasal

    return bab_pasal_dict

# Menggunakan contoh file "peraturan.pdf"
file_path = r"D:\Lomba BDC\Semifinal BDC\Investasi-V1\1_UU_dan_PERPU\PERATURAN_PEMERINTAH_PENGGANTI_UNDANG-UNDANG_NOMOR_7_TAHUN_1962.pdf"
hasil_ekstraksi = extract_bab_pasal(file_path)

# Menampilkan hasil ekstraksi bab dan pasal
for bab, pasal in hasil_ekstraksi.items():
    print("Bab:", bab)
    print("Pasal:", pasal)
    print()
