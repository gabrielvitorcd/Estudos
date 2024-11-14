import whisper
import json
import os

def transcribe_audio_to_text(mp3_file, output_json):
    # Carrega o modelo Whisper
    model = whisper.load_model("base")  # Pode ser 'tiny', 'base', 'small', 'medium', 'large'
    
    # Realiza a transcrição
    print("Transcrevendo áudio...")
    transcription = model.transcribe(mp3_file)
    
    # Extrai o texto da transcrição
    text = transcription['text']
    
    # Salva o texto transcrito em um arquivo JSON
    data = {"transcription": text}
    
    with open(output_json, 'w', encoding='utf-8') as json_file:
        json.dump(data, json_file, ensure_ascii=False, indent=4)
    
    print(f"Transcrição salva em {output_json}")

# Exemplo de uso
mp3_file = "aula1.mp3"  # Substitua pelo nome do seu arquivo MP3
output_json = "transcricao.json"  # Nome do arquivo de saída JSON

transcribe_audio_to_text(mp3_file, output_json)
