import re

def limpar_estilo(texto):
    """
    Remove o markdown da IA e prepara para o formato aceito pelo PDF (xhtml2pdf).
    Substitui negritos e ajusta quebras de linha.
    """
    if not texto: return ""
    # Transforma **bold** em negrito HTML
    texto = re.sub(r'\*\*(.*?)\*\*', r'<b>\1</b>', texto)
    # Troca asteriscos de lista por uma bolinha limpa
    texto = texto.replace('*', ' • ')
    # Ajusta quebras de linha
    texto = texto.replace('\n', '<br>')
    return texto

def extrair_secao(texto, tag):
    try:
        # Adicionei o caractere [ de escape e melhorei a busca pelo final da string
        padrao = f"\\{tag}\\](.*?)(?=\\[|$)"
        match = re.search(padrao, texto, re.DOTALL | re.IGNORECASE)
        if match:
            # Limpa espaços, asteriscos e quebras de linha extras
            return match.group(1).strip().strip(':').strip('*').strip()
        return ""
    except: return ""

def limpar_sessao():
    st.session_state.messages = []
    st.session_state.cv_content = ""