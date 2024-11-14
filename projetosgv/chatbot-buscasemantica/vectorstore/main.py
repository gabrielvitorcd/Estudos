import os
import redis
from langchain_community.document_loaders import DirectoryLoader, JSONLoader
from langchain.text_splitter import TokenTextSplitter
from langchain.vectorstores import RedisVectorStore
from langchain.embeddings import OpenAIEmbeddings
import asyncio

# Define o caminho para a pasta onde os arquivos JSON estão localizados
loader = DirectoryLoader(
    directory_path=os.path.join(os.path.dirname(__file__), '../tmp'),
    glob='*.json',
    loader_cls=lambda path: JSONLoader(file_path=path, content_path='/transcription')
)

async def load():
    # Carrega os documentos do diretório especificado
    docs = await loader.load()

    # Configura o token splitter para dividir os documentos em chunks
    splitter = TokenTextSplitter(
        encoding_name='cl100k_base',
        chunk_size=600,
        chunk_overlap=0
    )

    # Divide os documentos em chunks
    splitted_documents = splitter.split_documents(docs)
    print(splitted_documents)

    # Conecta ao Redis
    redis_client = redis.Redis(host='127.0.0.1', port=6379, decode_responses=True)

    # Cria o RedisVectorStore e insere os documentos processados com embeddings
    await RedisVectorStore.from_documents(
        splitted_documents,
        embedding=OpenAIEmbeddings(openai_api_key=os.getenv("OPENAI_API_KEY")),
        redis_url="redis://127.0.0.1:6379",
        index_name="videos-embeddings",
        key_prefix="videos:"
    )

    # Fecha a conexão com o Redis
    redis_client.close()

# Executa a função assíncrona
asyncio.run(load())
