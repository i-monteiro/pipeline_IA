from elevenlabs import ElevenLabs
from openai import OpenAI
import os
from dotenv import load_dotenv

# Carregar variáveis de ambiente
load_dotenv()

# Suas chaves de API
OPENAI_API_KEY = os.getenv("API_KEY")
ELEVEN_API_KEY = os.getenv("ELEVEN_API_KEY")

# Verifique se as chaves estão carregadas corretamente
if not OPENAI_API_KEY or not ELEVEN_API_KEY:
    raise ValueError("As chaves de API não foram carregadas corretamente. Verifique o arquivo .env.")

# Instanciar o cliente OpenAI
openai_client = OpenAI(api_key=OPENAI_API_KEY)

# Instanciar o cliente Eleven Labs
eleven_client = ElevenLabs(api_key=ELEVEN_API_KEY)

# Função para classificar comentário
def classify_comment(comment):
    """Envia um comentário para a API e retorna a classificação como 'elogio' ou 'reclamação'."""
    response = openai_client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "Você é um assistente que classifica comentários."},
            {"role": "user", "content": f"Classifique o seguinte comentário como 'elogio' ou 'reclamação': {comment}"}
        ]
    )
    return response.choices[0].message.content.strip()

# Função para converter texto em fala usando Eleven Labs
def text_to_speech(text):
    """Converte texto em áudio usando a API da Eleven Labs e salva o arquivo."""
    # Gera o áudio usando o modelo multilíngue
    audio_generator = eleven_client.generate(
        text=text,
        voice="nsQAxyXwUKBvqtEK9MfK",  # Use um ID de voz que suporte português
        model="eleven_multilingual_v2"  # Usa o modelo multilíngue para suportar português
    )
    
    # Converte o gerador em bytes
    audio_bytes = b''.join(list(audio_generator))  # Transforma o gerador em bytes

    # Salva o áudio em um arquivo
    audio_file = "output.mp3"
    with open(audio_file, "wb") as f:
        f.write(audio_bytes)  # Escreve os bytes no arquivo
    print(f"Áudio salvo em: {audio_file}")

# Exemplo de uso
if __name__ == "__main__":
    comentario = input("Digite o comentário para classificar: ")
    
    try:
        # Obter a classificação do comentário via ChatGPT
        classificacao = classify_comment(comentario)
        print("Classificação:", classificacao)
        
        # Converte a classificação em áudio usando Eleven Labs
        text_to_speech(f"A classificação do comentário é: {classificacao}")
    except Exception as e:
        print(f"Ocorreu um erro: {e}")
