import torch
import torch.nn as nn
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

# Sample texts
texts = [
    "Bentuk Negara Indonesia: Negara Indonesia adalah negara kesatuan yang berbentuk Republik. Artinya, Indonesia merupakan negara yang terdiri dari berbagai wilayah yang bersatu menjadi satu kesatuan yang berbentuk republik.",
    "Kedaulatan Rakyat: Kedaulatan berada di tangan rakyat, yang berarti kekuasaan tertinggi berada pada rakyat Indonesia. Kedaulatan ini dilaksanakan sepenuhnya oleh Majelis Permusyawaratan Rakyat (MPR). MPR merupakan lembaga tertinggi dalam negara yang mewakili rakyat dan memiliki peran penting dalam mengambil keputusan-keputusan strategis untuk negara.",
    "Komposisi Majelis Permusyawaratan Rakyat: MPR terdiri atas anggota Dewan Perwakilan Rakyat (DPR), ditambah dengan utusan-utusan dari daerah-daerah dan golongan-golongan tertentu, sesuai dengan aturan yang ditetapkan melalui undang-undang. Artinya, MPR merupakan gabungan anggota DPR dan wakil-wakil dari daerah dan golongan tertentu.",
    "Jangka Waktu Sidang MPR: MPR wajib mengadakan sidang sekurang-kurangnya sekali dalam lima tahun di ibukota negara. Ini berarti MPR harus mengadakan pertemuan setidaknya sekali dalam lima tahun."
]

# Initialize and use the TextSimilarityTransformer model
model = TextSimilarityTransformer()

# Calculate similarity between each pair of documents and display the results
for i, text_a in enumerate(texts):
    print(f"Similarity Document {i + 1} with other texts:")
    for j, text_b in enumerate(texts):
        if i != j:
            similarity_score = model(text_a, text_b)
            print(f"  Text {j + 1}: Similarity Score = {similarity_score:.4f}")
    print("-" * 50)
