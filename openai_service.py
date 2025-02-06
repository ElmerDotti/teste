import os
import openai

openai.api_key = os.getenv("sua_chave_aqui")

def analyze_conversation(messages):
    conversation = "\n".join(
        [f"Cliente: {msg['content']}" if msg['remote'] else f"Assistente: {msg['content']}" for msg in messages]
    )

    prompt = f"""
    A seguir está uma conversa entre um cliente e um assistente. Analise e extraia os seguintes pontos:
    - Nota de satisfação do cliente (0 a 10)
    - Resumo da conversa
    - Como a conversa poderia ter sido melhorada

    Conversa:
    {conversation}

    Responda no seguinte formato JSON:
    {{
        "satisfaction": <nota>,
        "summary": "<resumo>",
        "improvement": "<melhoria>"
    }}
    """

    response = openai.ChatCompletion.create(
        model="gpt-4o-mini",
        messages=[{"role": "system", "content": prompt}]
    )

    try:
        analysis = eval(response["choices"][0]["message"]["content"])
        return analysis
    except:
        return None
