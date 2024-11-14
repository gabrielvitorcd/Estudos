import openai
import os

from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")
print("Chave de API carregada:", api_key)


openai.api_key = os.getenv("OPENAI_API_KEY")

try:
    # Teste de criação de embedding usando o modelo atualizado
    response = openai.embeddings.create(
        input="This is a test",
        model="text-embedding-ada-002"  # Certifique-se de que o modelo é válido
    )
    print("Permissões verificadas: Embedding criado com sucesso.")
except openai.OpenAIError as e:
    print("Erro de permissão ao criar embedding:", e)
