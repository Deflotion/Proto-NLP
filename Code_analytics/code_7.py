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

# Membaca data dari file CSV
data = pd.read_csv("D:\Lomba BDC\Semifinal BDC\Code_analytics\Data\Dataset_v3.csv")

# Mengambil nilai dari kolom "keypoint" (tanpa tanda titik dua)
texts = data["keypoint:"].tolist()

# Inisialisasi dan gunakan model TextSimilarityTransformer
model = TextSimilarityTransformer()

# Hitung similarity antara setiap pasangan dokumen dan tampilkan hasilnya
for i, text_a in enumerate(texts):
    print(f"Similarity Dokumen {i + 1} dengan dokumen lain:")
    for j, text_b in enumerate(texts):
        if i != j:
            similarity_score = model(text_a, text_b)
            print(f"  Dokumen {j + 1}: Skor Similarity = {similarity_score:.4f}")
    print("-" * 50)