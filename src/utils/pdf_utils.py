from io import BytesIO
from xhtml2pdf import pisa
from datetime import datetime
from utils.formatadores import extrair_secao, limpar_estilo


def gerar_relatorio_pdf(texto_completo, score):
    # Extraímos e limpamos cada seção para o HTML
    resumo = limpar_estilo(extrair_secao(texto_completo, "[RESUMO"))
    fortes = limpar_estilo(extrair_secao(texto_completo, "[PONTOS_FORTES"))
    gaps = limpar_estilo(extrair_secao(texto_completo, "[GAPS"))
    sugestoes = limpar_estilo(extrair_secao(texto_completo, "[SUGESTOES"))
    dicas = limpar_estilo(extrair_secao(texto_completo, "[DICAS_OURO"))

    # Configuração dinâmica de cores baseada na sua nova régua
    if score >= 70:
        cor_score = "#2ecc71"  # Verde
        status_match = "ALTA ADERÊNCIA"
    elif score >= 50:
        cor_score = "#f1c40f"  # Amarelo
        status_match = "MÉDIA ADERÊNCIA"
    else:
        cor_score = "#e74c3c"  # Vermelho
        status_match = "BAIXA ADERÊNCIA"

    html_template = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <meta charset="utf-8">
        <style>
            /* Definição de Frames para repetição em todas as páginas */
            @page {{
                size: A4;
                margin: 1cm;
                margin-bottom: 3cm; /* Espaço para o rodapé não sobrepor o texto */
                
                @frame footer {{
                    -pdf-frame-content: footerContent;
                    bottom: 0.5cm;
                    margin-left: 1cm;
                    margin-right: 1cm;
                    height: 2.5cm;
                }}
            }}

            body {{ font-family: Helvetica, Arial, sans-serif; color: #333; }}
            
            /* Estilo do Rodapé Fixo */
            #footerContent {{
                font-size: 7pt;
                color: #721c24;
                text-align: center;
                border-top: 0.5pt solid #eee;
                padding-top: 8px;
            }}

            .header {{ text-align: center; margin-bottom: 20px; }}
            
            .score-circle {{ 
                background-color: {cor_score}; color: white; padding: 15px; 
                text-align: center; border-radius: 10px; margin-bottom: 20px;
            }}
            
            .card {{ padding: 15px; border-radius: 8px; margin-bottom: 12px; font-size: 11pt; }}
            
            .resumo-box {{ border: 1px solid #eee; background-color: #ffffff; }}
            .diferenciais {{ background-color: #e7f3ff; border-left: 6px solid #4A90E2; color: #1e3a8a; }}
            .gaps {{ background-color: #fff8e1; border-left: 6px solid #f1c40f; color: #856404; }}
            .plano {{ background-color: #e8f5e9; border-left: 6px solid #2ecc71; color: #1b5e20; }}
            .dicas-ouro {{ background-color: #f0f7ff; border: 1px dashed #4A90E2; margin-top: 10px; }}
            
            h3 {{ margin-top: 0; margin-bottom: 8px; font-size: 13pt; text-transform: uppercase; font-weight: bold; }}
            b {{ color: #000; }}
        </style>
    </head>
    <body>
        <div id="footerContent">
            <div style="background-color: #fff4f4; padding: 8px; border: 0.5pt solid #f5c6cb; border-radius: 5px; margin-bottom: 5px;">
                <strong>Nota Legal:</strong> Este documento foi gerado por Inteligência Artificial (Gemini 2.0 Flash) apenas como <b>sugestão</b>. 
                As análises não possuem garantia de acerto total e a decisão final cabe sempre ao usuário.
            </div>
            <div style="color: #aaa; font-size: 8pt;">
                Gerado por <b>Assistente de Currículo</b> | {datetime.now().strftime('%d/%m/%Y %H:%M')}
            </div>
        </div>

        <div class="header">
            <h1 style="color: #4A90E2; margin:0; font-size: 28pt; font-weight: 900;">Assistente de Currículo</h1>
            <p style="color: #666; font-size: 10pt; margin-top: 5px;">Relatório de Análise e Sugestões Profissionais</p>
        </div>

        <div class="score-circle">
            <h2 style="margin:0; font-size: 32pt;">{score}%</h2>
            <div style="font-weight: bold; font-size: 10pt; letter-spacing: 1px;">{status_match}</div>
        </div>

        <div class="card resumo-box">
            <h3>📝 Avaliação Geral</h3>
            <p>{resumo}</p>
        </div>

        <div class="card diferenciais">
            <h3>💪 Sugestões de Diferenciais</h3>
            <p>{fortes}</p>
        </div>

        <div class="card gaps">
            <h3>⚠️ Possíveis Pontos de Atenção</h3>
            <p>{gaps}</p>
        </div>

        <div class="card plano">
            <h3>💡 Plano de Ação Sugerido</h3>
            <p>{sugestoes}</p>
        </div>

        {f'<div class="card dicas-ouro"><h3>✨ Dicas de Ouro</h3><p>{dicas}</p></div>' if dicas else ''}

    </body>
    </html>
    """
    
    result = BytesIO()
    pisa.CreatePDF(
        src=BytesIO(html_template.encode("utf-8")), 
        dest=result,
        encoding='utf-8'
    )
    return result.getvalue()