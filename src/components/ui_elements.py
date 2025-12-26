import streamlit as st

def renderizar_cabecalho():
    """
    Renderiza o cabeçalho fixo no topo da aplicação.
    """
    st.markdown("""
    <style>
        /* Header  */
        .fixed-header {
            position: sticky;
            top: 0;
            left: 0;
            width: 100%;
            background-color: white;
            padding: 10px 20px;
            border-bottom: 2px solid #4A90E2;
            z-index: 999;
            text-align: center;
            box-shadow: 0px 2px 5px rgba(0,0,0,0.1);
            margin-bottom: 20px;
        }
        
        .main-content {
            margin-top: 20px;
        }

        /* Estilização da Sidebar */
        [data-testid="stSidebar"] [data-testid="column"] {
            width: 100% !important;
            flex: 1 1 0% !important;
            min-width: 0px !important;
        }

        [data-testid="stSidebar"] .stButton button {
            width: 100% !important;
            display: block !important;
            height: 45px !important;
            border-radius: 8px !important;
            font-weight: bold !important;
            transition: all 0.3s ease !important;
            text-transform: uppercase;
        }

        [data-testid="stSidebar"] [data-testid="column"]:nth-of-type(1) .stButton button {
            background-color: #4A90E2 !important;
            color: white !important;
            border: none !important;
        }

        [data-testid="stSidebar"] [data-testid="column"]:nth-of-type(2) .stButton button {
            background-color: white !important;
            color: #ff4b4b !important;
            border: 1px solid #ff4b4b !important;
        }

        /* Loader Fullscreen */
        .loader-overlay {
            position: fixed;
            top: 0;
            left: 0;
            width: 100vw;
            height: 100vh;
            background-color: rgba(255, 255, 255, 0.9);
            z-index: 10000;
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: center;
        }

        .loader-circle {
            border: 8px solid #f3f3f3;
            border-top: 8px solid #4A90E2;
            border-radius: 50%;
            width: 60px;
            height: 60px;
            animation: spin 1s linear infinite;
            margin-bottom: 20px;
        }

        @keyframes spin {
            0% { transform: rotate(0deg); }
            100% { transform: rotate(360deg); }
        }
    </style>

    <div class="fixed-header">
        <h2 style='margin:0; color: #4A90E2; font-family: sans-serif;'>🤖 Assistente de Currículo</h2>
        <p style='margin:0; color: #666; font-size: 14px;'>🤝 Juntos na Sua Próxima Conquista</p>
    </div>
    <div class="main-content"></div>

    """, unsafe_allow_html=True)

def renderizar_gauge(score):
    """
    Cria o medidor visual de compatibilidade (Match Score).
    """
    # Lógica de cores baseada na régua definida
    if score >= 70:
        color = "#2ecc71"  # Verde
        label = "ALTA ADERÊNCIA"
    elif score >= 50:
        color = "#f1c40f"  # Amarelo
        label = "MÉDIA ADERÊNCIA"
    else:
        color = "#e74c3c"  # Vermelho
        label = "BAIXA ADERÊNCIA"

    st.markdown(f"""
    <div style="display: flex; flex-direction: column; align-items: center; background: white; padding: 15px; border-radius: 15px; border: 1px solid #eee; box-shadow: 0px 4px 10px rgba(0,0,0,0.05);">
        <div style="width: 100px; height: 100px; border-radius: 50%; background: conic-gradient({color} {score * 3.6}deg, #f0f2f6 0deg); display: flex; align-items: center; justify-content: center;">
            <div style="width: 82px; height: 82px; background: white; border-radius: 50%; display: flex; align-items: center; justify-content: center;">
                <span style="font-size: 22px; font-weight: bold; color: {color};">{score}%</span>
            </div>
        </div>
        <div style="margin-top:10px; padding: 2px 10px; background-color: {color}; color: white; border-radius: 12px; font-size: 10px; font-weight: bold;">
            {label}
        </div>
    </div>
    """, unsafe_allow_html=True)

def exibir_manual():
    """
    Exibe as instruções de uso iniciais.
    """
    st.info("### Bem-vindo ao seu Assistente de Currículo! 🌟")
    st.warning("⚠️ **Aviso:** Esta é uma ferramenta baseada em IA. As análises são sugestões e podem conter imprecisões.")
    
    st.markdown("---")
    st.markdown("### 🛠️ Como usar:")
    
    col1, col2, col3, col4 = st.columns(4)
    with col1: st.markdown("**1. Chave API**\nInsira sua chave Gemini.")
    with col2: st.markdown("**2. Vaga**\nCole a descrição alvo.")
    with col3: st.markdown("**3. Currículo**\nSuba seu PDF.")
    with col4: st.markdown("**4. Analisar**\nVeja suas sugestões!")