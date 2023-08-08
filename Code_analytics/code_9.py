import torch
import torch.nn as nn
import pandas as pd
from transformers import BertTokenizer, BertModel

class TextSimilarityTransformer(nn.Module):
    def __init__(self, model_name="bert-base-uncased"):
        super(TextSimilarityTransformer, self).__init__()
        self.tokenizer = BertTokenizer.from_pretrained(model_name)
        self.model = BertModel.from_pretrained(model_name)
        self.cosine_similarity = nn.CosineSimilarity(dim=1)

    def forward(self, text_a, text_b):
        inputs_a = self.tokenizer.encode_plus(text_a, add_special_tokens=True, return_tensors="pt", max_length=128)
        inputs_b = self.tokenizer.encode_plus(text_b, add_special_tokens=True, return_tensors="pt", max_length=128)

        with torch.no_grad():
            outputs_a = self.model(**inputs_a)
            embeddings_a = outputs_a.pooler_output

            outputs_b = self.model(**inputs_b)
            embeddings_b = outputs_b.pooler_output

        similarity_score = self.cosine_similarity(embeddings_a, embeddings_b)

        return similarity_score.item()

# Membaca data dari file CSV dengan encoding yang sesuai (contoh: 'utf-8', 'latin1', 'iso-8859-1', dll.)
data = pd.read_csv("D:\Lomba BDC\Semifinal BDC\Code_analytics\Data\DataBaru_1.csv")

# Mengambil nilai dari kolom "Tentang:" (tanpa tanda titik dua)
texts = data["Tentang:"].tolist()

# Inisialisasi dan gunakan model TextSimilarityTransformer
model = TextSimilarityTransformer()

# Hitung similarity antara setiap pasangan dokumen dan simpan hasilnya dalam list
similarity_scores = []
for i, text_a in enumerate(texts):
    scores = [model(text_a, text_b) for j, text_b in enumerate(texts) if i != j]
    similarity_scores.append(scores)

# Pastikan semua baris memiliki jumlah elemen yang sama dengan menambahkan nilai NaN jika diperlukan
max_length = max(len(scores) for scores in similarity_scores)
similarity_scores = [scores + [float('nan')] * (max_length - len(scores)) for scores in similarity_scores]

# Buat DataFrame untuk menyimpan hasil similarity
result_df = pd.DataFrame(similarity_scores, columns=[f"Dokumen {i + 1}" for i in range(max_length)])

# Simpan hasil similarity ke dalam file CSV
result_df.to_csv("hasil_similarity_01.csv", index=False)
