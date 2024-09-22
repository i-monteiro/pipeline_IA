import streamlit as st
import time
from openai import OpenAI
from elevenlabs import ElevenLabs
import os
from dotenv import load_dotenv
from datetime import datetime
import re  # Importação adicional

load_dotenv()

# Configuração das chaves de API
OPENAI_API_KEY = os.getenv("API_KEY")
ELEVEN_API_KEY = os.getenv("ELEVEN_API_KEY")

# Verifique se as chaves estão carregadas corretamente
if not OPENAI_API_KEY or not ELEVEN_API_KEY:
    raise ValueError("As chaves de API não foram carregadas corretamente. Verifique o arquivo .env.")

# Instanciar os clientes OpenAI e Eleven Labs
openai_client = OpenAI(api_key=OPENAI_API_KEY)
eleven_client = ElevenLabs(api_key=ELEVEN_API_KEY)

# ID do Assistente
ASSISTANT_ID = os.getenv("ASSISTANT_ID")

# Função para converter texto em fala usando Eleven Labs
def text_to_speech(text):
    """Converte texto em áudio usando a API da Eleven Labs e retorna o áudio."""
    # Gera o áudio usando o modelo multilíngue
    audio_generator = eleven_client.generate(
        text=text,
        voice="nsQAxyXwUKBvqtEK9MfK",  # Use um ID de voz que suporte português
        model="eleven_multilingual_v2"  # Usa o modelo multilíngue para suportar português
    )
    
    # Converte o gerador em bytes
    audio_bytes = b''.join(list(audio_generator))  # Transforma o gerador em bytes
    
    return audio_bytes

# Função para enviar a pergunta ao assistente e obter a resposta
def responder_pergunta(pergunta):
    # Cria um novo thread com a mensagem do usuário
    thread = openai_client.beta.threads.create(
        messages=[
            {
                "role": "user",
                "content": f"hoje é dia {datetime.now()} {pergunta}",
            }
        ]
    )

    # Envia o thread para o assistente (como uma nova execução)
    run = openai_client.beta.threads.runs.create(thread_id=thread.id, assistant_id=ASSISTANT_ID)
    st.write(f"👉 Conversa id: {run.id}")

    # Aguarda a conclusão da execução
    while run.status != "completed":
        run = openai_client.beta.threads.runs.retrieve(thread_id=thread.id, run_id=run.id)
        st.write(f"🏃 Status da execução: {run.status}")
        time.sleep(1)

    st.write("🏁 Execução concluída!")

    # Obtém a última mensagem do thread
    message_response = openai_client.beta.threads.messages.list(thread_id=thread.id)
    messages = message_response.data

    # Extrai e retorna a resposta mais recente
    latest_message = messages[0]
    resposta_texto = latest_message.content[0].text.value.strip()
    
    # Remove as citações do texto
    resposta_texto = re.sub(r'【.*?】', '', resposta_texto)  # Linha adicionada
    
    # Converte a resposta em áudio
    resposta_audio = text_to_speech(resposta_texto)
    
    return resposta_texto, resposta_audio

# Interface do Streamlit
st.title("Agente de Atendimento - Pergunte ao Assistente")

# Caixa de entrada para perguntas
pergunta = st.text_input("Digite sua pergunta:")

# Quando uma pergunta é feita, envia para o assistente e exibe a resposta
if pergunta:
    resposta_texto, resposta_audio = responder_pergunta(pergunta)
    st.write(f"💬 Resposta: {resposta_texto}")
    
    # Reproduz o áudio da resposta
    st.audio(resposta_audio, format='audio/mp3')
