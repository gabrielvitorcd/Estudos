import faiss
from sentence_transformers import SentenceTransformer

# Substitua pelo caminho correto onde o arquivo .index está salvo
index = faiss.read_index("C:/Users/Gabriel/Desktop/vectorstore/faiss_index.index")

# Carregar o modelo de embeddings (use o mesmo modelo usado para criar o índice)
model = SentenceTransformer('all-MiniLM-L6-v2')

def search(query, k=5):
    # Gerar embedding para a consulta
    query_embedding = model.encode(query).reshape(1, -1)

    # Realizar a consulta no índice FAISS
    distances, indices = index.search(query_embedding, k)
    
    # Retornar os índices e distâncias dos resultados
    return indices, distances

# Exemplo de consulta
query = "comida"
indices, distances = search(query)
print("Indices dos documentos mais próximos:", indices)
print("Distâncias correspondentes:", distances)
