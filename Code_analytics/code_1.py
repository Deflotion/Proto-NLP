import spacy

# Load the spaCy language model
nlp = spacy.load('en_core_web_trf')

# Dokumen yang akan dianalisis
dokumen = "KEBIJAKAN KEUANGAN NEGARA DAN STABILITAS SISTEM KEUANGAN UNTUK PENANGANAN PANDEMI CORONA VIRUS DISEASE 2019 (COVID-19) DAN/ATAU DALAM RANGKA MENGHADAPI ANCAMAN YANG MEMBAHAYAKAN PEREKONOMIAN NASIONAL DAN/ATAU STABILITAS SISTEM KEUANGAN"

# Tokenisasi dokumen
dokumen_tokens = nlp(dokumen)

# Kata target
kata_target = "investasi"

# Similaritas kosinus antara kata target dan kata dalam dokumen
def hitung_similaritas(kata):
    return dokumen_tokens.similarity(nlp(kata))

# Ambil kata-kata dengan similaritas tinggi
kata_mendekati = [token.text for token in dokumen_tokens if hitung_similaritas(token.text) > 0.6 and token.text.lower() != kata_target]

# Tampilkan kata-kata yang mendekati
print("Kata yang mendekati 'investasi':", kata_mendekati)
