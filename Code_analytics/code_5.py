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
        # Tokenize input texts
        inputs_a = self.tokenizer.encode_plus(text_a, add_special_tokens=True, return_tensors="pt", max_length=128)
        inputs_b = self.tokenizer.encode_plus(text_b, add_special_tokens=True, return_tensors="pt", max_length=128)

        # Get embeddings using BERT
        with torch.no_grad():
            outputs_a = self.model(**inputs_a)
            embeddings_a = outputs_a.pooler_output

            outputs_b = self.model(**inputs_b)
            embeddings_b = outputs_b.pooler_output

        # Calculate cosine similarity between embeddings
        similarity_score = self.cosine_similarity(embeddings_a, embeddings_b)

        return similarity_score.item()

# Sample texts
text1 = "Bentuk Negara Indonesia: Negara Indonesia adalah negara kesatuan yang berbentuk Republik. Artinya, Indonesia merupakan negara yang terdiri dari berbagai wilayah yang bersatu menjadi satu kesatuan yang berbentuk republik."
text2 = "Kedaulatan Rakyat: Kedaulatan berada di tangan rakyat, yang berarti kekuasaan tertinggi berada pada rakyat Indonesia. Kedaulatan ini dilaksanakan sepenuhnya oleh Majelis Permusyawaratan Rakyat (MPR). MPR merupakan lembaga tertinggi dalam negara yang mewakili rakyat dan memiliki peran penting dalam mengambil keputusan-keputusan strategis untuk negara."

# Initialize and use the TextSimilarityTransformer model
model = TextSimilarityTransformer()
similarity_score = model(text1, text2)

print(f"Similarity Score: {similarity_score:.4f}")
