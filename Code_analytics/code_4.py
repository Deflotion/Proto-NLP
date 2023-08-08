import pandas as pd
import torch
from transformers import AutoTokenizer, AutoModel
from sklearn.metrics.pairwise import cosine_similarity

def read_data(file_path):
    df = pd.read_csv(file_path)
    return df

def calculate_similarity(model, tokenizer, sentence1, sentence2):
    encoded_input = tokenizer(sentence1, sentence2, return_tensors='pt', padding=True, truncation=True, max_length=128)  # Sesuaikan max_length sesuai kebutuhan Anda
    with torch.no_grad():
        model_output = model(**encoded_input)
    sentence_embeddings = model_output.pooler_output
    if sentence_embeddings.size(0) < 2:
        # Jika panjang token kurang dari 2, mengembalikan similarity 0 (tidak diolah)
        return 0.0
    similarity_score = cosine_similarity(sentence_embeddings[0].unsqueeze(0), sentence_embeddings[1].unsqueeze(0))
    return similarity_score

def main():
    file_path = r'D:\Lomba BDC\Semifinal BDC\Code_analytics\Data\DataUU.csv'
    model_name = "indolem/indobert-base-uncased"
    model = AutoModel.from_pretrained(model_name)
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    
    data = read_data(file_path)
    similarity_results = []
    
    for i, row1 in data.iterrows():
        if pd.notna(row1['keypoint:']):  # Memeriksa apakah keypoint tidak kosong
            for j, row2 in data.iterrows():
                if i != j and pd.notna(row2['keypoint:']):  # Memeriksa apakah keypoint tidak kosong
                    doc1 = row1['keypoint:']
                    doc2 = row2['keypoint:']
                    similarity_score = calculate_similarity(model, tokenizer, doc1, doc2)
                    similarity_results.append((row1['name_docs:'], row2['name_docs:'], row1['bab index:'], row2['bab index:'], similarity_score))
    
    # Menyimpan hasil ke dalam DataFrame dan menghitung akurasi
    result_df = pd.DataFrame(similarity_results, columns=['Document 1', 'Document 2', 'Bab Index 1', 'Bab Index 2', 'Similarity Score'])
    result_df.to_csv('similarity_results.csv', index=False)
    
    # Menghitung akurasi model berdasarkan threshold tertentu (misalnya 0.8)
    threshold = 0.8
    accuracy = (result_df['Similarity Score'] >= threshold).mean()
    print("Model Accuracy:", accuracy)

if __name__ == "__main__":
    main()
