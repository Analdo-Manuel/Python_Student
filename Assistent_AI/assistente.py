# Assistente AI de programação em Python
# Este assistente é capaz de responder perguntas sobre programação em Python,
# fornecer exemplos de código, explicar conceitos e ajudar na depuração de código.

# Importa módulo para interagir com os sistemas operacionais
import os

# Importa a biblioteca Streamlit para criar a interface do usuário web
import streamlit as st

# Importa a class Groq para se concetar à API da Groq
from groq import Groq

st.set_page_config(
    page_title="Python",
    page_icon="🤖", 
    layout="wide",
    initial_sidebar_state="expanded")


SYSTEM_PROMPT = """
Você é um assistente de IA especializado em programação, com foco em Python. Seu objetivo é fornecer explicações claras e concisas sobre conceitos de programação, responder perguntas, fornecer exemplos de código e ajudar na depuração de código.
Responda em português.
Explique os conceitos de forma simples e dê exemplos em Python.

REGRAS DE OPERAÇÃO:
1. Sempre forneça exemplos de código em Python quando apropriado.
2. Se o usuário fizer uma pergunta sobre um erro de código, forneça uma explicação detalhada do erro e sugira possíveis soluções.
3. Se o usuário pedir para explicar um conceito, forneça uma explicação clara e concisa, seguida de um exemplo em Python.
4. Se o usuário pedir para escrever um código, forneça o código completo em Python, com comentários explicativos.
5. Se o usuário pedir para revisar um código, forneça feedback detalhado sobre o código, incluindo sugestões de melhorias e melhores práticas.
6. Sempre responda em português, mesmo que a pergunta seja feita em outro idioma.
7. Se o usuário fizer uma pergunta fora do escopo de programação em Python, informe educadamente que você só pode responder perguntas relacionadas a esse tópico.
8. Mantenha um tom amigável e profissional em todas as respostas.
9. Documentação: Sempre forneça documentação ou links para documentação oficial quando possível, para que o usuário possa aprender mais sobre o tópico discutido.
"""

with st.sidebar:
    st.header("Configurações do Assistente AI")
    st.markdown("Aqui você pode ajustar as configurações do assistente AI.")    
    # Campo para o usuário inserir sua chave de API da Groq
    groq_api_key = st.text_input("Digite sua chave de API da Groq:", 
                            type="password",
                            help="Insira sua chave de API da Groq para se conectar ao modelo de linguagem. Você pode obter uma chave de API em https://groq.com/.")
    # Campo para o usuário inserir o modelo que deseja usar
    modelo = st.text_input("Digite o modelo que deseja usar:", 
                            value="gpt-oss-120b", 
                            help="Insira o modelo que deseja usar para gerar respostas. Por exemplo, 'gpt-4o' ou 'gpt-oss-120b'.")
    # Adicionar linha divisória
    st.markdown("---")
    st.markdown("### Sobre o Assistente AI")
    st.markdown("Este assistente é capaz de responder perguntas sobre programação em Python, fornecer exemplos de código, explicar conceitos e ajudar na depuração de código.")
    st.markdown("---")
    st.markdown("Desenvolvido por [Analdo Manuel](https://www.seusite.com) - 2024")
    st.link_button("Visite meu site", "https://www.seusite.com", icon="🌐")

with st.container():
    st.title("Assistente AI de programação em Python 🤖")
    st.markdown("Bem-vindo ao Assistente AI de programação em Python!")
    st.caption("Este assistente é capaz de responder perguntas sobre programação em Python, fornecer exemplos de código, explicar conceitos e ajudar na depuração de código.")
    # Inicializa a lista de mensagens na sessão do Streamlit, se ainda não estiver inicializada
    if "messages" not in st.session_state:
        st.session_state.messages = []
    # Exibe todas as mensagens armazenadas na sessão do Streamlit
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message['content'])
    client = None
    if groq_api_key:
        try:
            # Cria uma instância do cliente Groq com a chave de API fornecida
            client = Groq(api_key=groq_api_key)
        except Exception as e:
            st.sidebar.error(f"Erro ao criar o cliente Groq: {e}")
            st.stop()
    elif st.session_state.messages:
        st.sidebar.warning("Por favor, insira sua chave de API da Groq para continuar.")
        st.stop()

st.markdown("""
<style>
div[data-testid="stChatInput"] textarea {
    font-size: 16px;
    color: white;
}

div[data-testid="stChatInput"] textarea::placeholder {
    color: #AAAAAA;
}
</style>
""", unsafe_allow_html=True)

prompt = st.chat_input(
    "💻 Envie seu código ou faça uma pergunta sobre Python 🐍", 
    accept_file=True
) 
# Capta a entrada do usuário no chat
if prompt:
    # Verifica se o cliente Groq foi criado com sucesso
    if not client:
        st.warning("Por favor, insira sua chave de API da Groq para continuar.")
        st.stop()
    # Adiciona a mensagem do usuário à lista de mensagens na sessão do Streamlit
    st.session_state.messages.append({"role": "user", "content": prompt.text})
    # Exibe a mensagem do usuário no chat
    with st.chat_message("user"):
        st.markdown(prompt.text)
    
    # Verifica se o cliente Groq está disponível
    if client:
        messages_for_api = [{"role": "system", "content": SYSTEM_PROMPT}]
        for msg in st.session_state.messages:
            messages_for_api.append(msg)
    # Envia a solicitação para a API da Groq e obtém a resposta
    with st.chat_message("assistant"):
        with st.spinner("Gerando resposta..."):
            try:
                completion = client.chat.completions.create(
                    model=modelo,
                    messages=messages_for_api,
                    temperature=1,
                    max_completion_tokens=2048,
                    top_p=1,
                    reasoning_effort="medium",
                    stream=True,
                    stop=None
                )
                response = ""
                for chunk in completion:
                    if chunk.choices[0].delta.content:
                        response += chunk.choices[0].delta.content
                st.markdown(response)
            except Exception as e:
                st.error(f"Erro ao gerar resposta: {e}")
st.markdown(
    """
    <div style="text-align: center; color: gray;">
    <hr>
    <p style="text-align: center; color: gray;">Desenvolvido por <a href="https://www.seusite.com" target="_blank">Analdo Manuel</a> - 2024</p>
    </div>
    """,
    unsafe_allow_html=True
)