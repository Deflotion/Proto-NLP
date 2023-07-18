import csv
import re

def extract_pasal(text):
    pasal = re.findall(r"Pasal\s+(\d+)\.\s+(.*?)(?=\n\n[A-Za-z]|\Z)", text, re.IGNORECASE | re.DOTALL)
    pasal_data = [(p[0], p[1]) for p in pasal] if pasal else []

    poin = []
    for p in pasal_data:
        poin_list = re.findall(r"(?<!\w)(?:[a-z]\.|[ivx]+\.)\s*(.*?)(?=(?:\n\n[A-Za-z]\.|[a-z]\.|[ivx]+\.)|\Z)", p[1], re.IGNORECASE | re.DOTALL)
        poin.extend([(p[0], po) for po in poin_list])

    return pasal_data, poin

input_file = 'output_model_8_v1.csv'
output_file = 'output15.csv'

with open(input_file, 'r') as file_in, open(output_file, 'w', newline='') as file_out:
    reader = csv.reader(file_in)
    writer = csv.writer(file_out)

    writer.writerow(['Pasal', 'Isi Pasal'])

    pasal_data_all = []
    poin_all = []

    for row in reader:
        text = row[0]

        pasal_data, poin = extract_pasal(text)

        pasal_data_all.extend(pasal_data)
        poin_all.extend(poin)

    for pasal in pasal_data_all:
        pasal_text = f"Pasal {pasal[0]}"
        for po in poin_all:
            if po[0] == pasal[0]:
                writer.writerow([pasal_text, po[1]])

print("Ekstraksi informasi pasal selesai. File output.csv telah dibuat.")
