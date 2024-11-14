import os
import numpy as np
from langchain_community.document_loaders import DirectoryLoader, JSONLoader
from langchain.text_splitter import TokenTextSplitter
from sentence_transformers import SentenceTransformer
import faiss
import asyncio

# Define o caminho para a pasta onde os arquivos JSON estão localizados
loader = DirectoryLoader(
    path='C:/Users/Gabriel/Desktop/vectorstore/tmp',  # Caminho absoluto para os arquivos JSON
    glob='*.json',  # Padrão de busca para arquivos JSON
    loader_cls=lambda path: JSONLoader(file_path=path, jq_schema='.transcription')  # Corrigido o jq_schema
)

async def embed_batch(embeddings, batch):
    """Função assíncrona para processar um lote de embeddings."""
    return await asyncio.to_thread(embeddings.encode, [doc.page_content for doc in batch])

async def load():
    # Carrega os documentos do diretório especificado
    docs = loader.load()

    # Configura o token splitter para dividir os documentos em chunks
    splitter = TokenTextSplitter(
        encoding_name='cl100k_base',
        chunk_size=600,
        chunk_overlap=0
    )

    # Divide os documentos em chunks
    splitted_documents = splitter.split_documents(docs)
    print("Documentos divididos em chunks:", splitted_documents)

    # Inicializa o modelo de embeddings local (usando sentence-transformers)
    embeddings = SentenceTransformer('sentence-transformers/all-MiniLM-L6-v2')

    batch_size = 20  # Tamanho do lote
    document_vectors = []  # Lista para armazenar todos os embeddings

    # Inicializa o FAISS (IndexFlatL2 é o tipo de índice, adequado para buscas exatas)
    dimension = None
    faiss_index = None

    # Lista de tarefas assíncronas para processar os lotes em paralelo
    tasks = []
    for i in range(0, len(splitted_documents), batch_size):
        batch = splitted_documents[i:i + batch_size]  # Cria um lote de documentos
        task = asyncio.create_task(embed_batch(embeddings, batch))  # Cria uma tarefa assíncrona para o lote
        tasks.append((i, task))

    # Processa os resultados das tarefas conforme são completadas
    for i, task in tasks:
        batch_embeddings = await task  # Espera pela conclusão da tarefa

        # Inicializa o índice FAISS com a dimensão correta no primeiro lote
        if faiss_index is None:
            dimension = len(batch_embeddings[0])
            faiss_index = faiss.IndexFlatL2(dimension)

        # Adiciona embeddings do lote ao índice FAISS
        faiss_index.add(np.array(batch_embeddings, dtype=np.float32))

        # Salva o índice FAISS em intervalos
        faiss.write_index(faiss_index, 'faiss_index.index')
        print(f"Índice FAISS atualizado e salvo após o lote {i//batch_size + 1}")

    print(f"Processamento concluído. Total de vetores no índice FAISS: {faiss_index.ntotal}")

# Executa a função assíncrona
asyncio.run(load())
