import streamlit as st
import pandas as pd

st.set_page_config(page_title="Visão para a Área Brasil", layout="wide")

# CSS personalizado para mesclar e estender as caixas de Responsabilidade
st.markdown("""
<style>
    .stApp {
        background-color: #08111e;
        color: #ffffff;
    }
    
    .main-title {
        color: #00b4d8 !important;
        font-size: 30px !important;
        font-weight: bold !important;
        letter-spacing: 1.5px;
        margin-bottom: 20px;
    }
    
    /* Agrupador da Responsabilidade (Altura exata para bater com 2 linhas + margem) */
    .pillar-box-merged {
        background-color: #0d1e30;
        border-radius: 6px;
        padding: 10px;
        font-weight: bold;
        font-size: 13px;
        text-align: center;
        border: 1px solid #1a334e;
        height: 94px; /* Altura exata: 2x caixas de 44px + 6px de margem */
        display: flex;
        align-items: center;
        justify-content: center;
        line-height: 1.3;
        box-sizing: border-box;
        margin-bottom: 12px; /* Margem entre blocos de responsabilidades */
    }
    
    .p-viver { color: #8bc34a; border-left: 5px solid #8bc34a; }
    .p-cuidar { color: #ffb74d; border-left: 5px solid #ffb74d; }
    .p-convidar { color: #4dd0e1; border-left: 5px solid #4dd0e1; }
    .p-unir { color: #ba68c8; border-left: 5px solid #ba68c8; }
    
    /* Grade de Cabeçalho */
    .grid-header {
        background-color: #0e2238;
        color: #00b4d8;
        font-weight: bold;
        text-align: center;
        padding: 10px;
        border-radius: 4px;
        font-size: 14px;
        letter-spacing: 1px;
    }
    
    /* Linha do Tópico com Altura Fixa */
    .topic-row {
        background-color: #0d1e30;
        padding: 0 15px;
        height: 44px;
        border-radius: 4px;
        font-size: 14px;
        font-weight: 600;
        border: 1px solid #1a334e;
        display: flex;
        align-items: center;
        margin-bottom: 6px;
        box-sizing: border-radius;
    }
    
    /* Caixas de Valores com Altura Fixa */
    .val-box {
        background-color: #122840;
        color: #ffffff;
        text-align: center;
        height: 44px;
        line-height: 44px;
        border-radius: 4px;
        font-size: 17px;
        font-weight: bold;
        border: 1px solid #1e3d60;
        margin-bottom: 6px;
        box-sizing: border-box;
    }
    
    .footer-quote {
        text-align: center;
        color: #8ab4f8;
        font-style: italic;
        margin-top: 30px;
        font-size: 20px;
    }
</style>
""", unsafe_allow_html=True)

@st.cache_data
def carregar_dados():
    return pd.read_excel('DADOS.xlsx', sheet_name='2026')

df = pd.read_excel('DADOS.xlsx', sheet_name='2026')

# --- TOPO: TÍTULO E FILTROS ---
st.markdown("<p class='main-title'>VISÃO PARA A ÁREA BRASIL - ESTACA MACEIÓ BRASIL LITORAL</p>", unsafe_allow_html=True)

c_ano, c_unid = st.columns([1, 4])

with c_ano:
    st.caption("**ANO**")
    anos = sorted(df['ANO'].unique())
    ano_sel = st.segmented_control("Ano", anos, default=anos[0], label_visibility="collapsed")

with c_unid:
    st.caption("**UNIDADE**")
    unidades = sorted(df['UNIDADES'].unique())
    unid_sel = st.segmented_control("Unidade", unidades, default=unidades[0], label_visibility="collapsed")

st.markdown("<br>", unsafe_allow_html=True)

# Filtrar dados
df_filtrado = df[(df['ANO'] == ano_sel) & (df['UNIDADES'] == unid_sel)]

# --- CABEÇALHO DA TABELA ---
col_pil, col_top, col_met, col_alc = st.columns([1.3, 3.5, 1, 1])

with col_pil:
    st.markdown("<div class='grid-header'>RESPONSABILIDADES</div>", unsafe_allow_html=True)
with col_top:
    st.markdown("<div class='grid-header' style='text-align:left; padding-left:15px;'>INDICADOR / TÓPICO</div>", unsafe_allow_html=True)
with col_met:
    st.markdown("<div class='grid-header'>META</div>", unsafe_allow_html=True)
with col_alc:
    st.markdown("<div class='grid-header'>ALCANÇADO</div>", unsafe_allow_html=True)

st.write("")

# Estrutura agrupada por Responsabilidade
grupos_responsabilidades = [
    {
        "pilar": "VIVER O EVANGELHO DE JESUS CRISTO",
        "classe": "p-viver",
        "topicos": [
            {"nome": "Frequência da Reunião Sacramental", "icone": "⛵"},
            {"nome": "Membros Participantes", "icone": "👥"}
        ]
    },
    {
        "pilar": "CUIDAR DOS NECESSITADOS",
        "classe": "p-cuidar",
        "topicos": [
            {"nome": "Membros Retornando", "icone": "🤝"},
            {"nome": "Membros Jejuando", "icone": "🥖"}
        ]
    },
    {
        "pilar": "CONVIDAR TODOS A RECEBER O EVANGELHO",
        "classe": "p-convidar",
        "topicos": [
            {"nome": "Batismos de Conversos", "icone": "🌊"},
            {"nome": "Missionários Servindo do Brasil", "icone": "🏙️️"}
        ]
    },
    {
        "pilar": "UNIR AS FAMÍLIAS POR TODA A ETERNIDADE",
        "classe": "p-unir",
        "topicos": [
            {"nome": "Recomendações para o Templo - Membros com Investidura", "icone": "🏛️"},
            {"nome": "Recomendações para o Templo - Membros sem Investidura", "icone": "📜"}
        ]
    }
]

# Renderização do Grid Agrupado
for grupo in grupos_responsabilidades:
    c_p, c_t, c_m, c_a = st.columns([1.3, 3.5, 1, 1])
    
    # Coluna 1: Responsabilidade Unificada (Uma única caixa centralizada verticalmente)
    with c_p:
        st.markdown(f"<div class='pillar-box-merged {grupo['classe']}'>{grupo['pilar']}</div>", unsafe_allow_html=True)
        
    # Colunas 2, 3 e 4: Os tópicos e seus valores empilhados
    with c_t:
        for t in grupo["topicos"]:
            st.markdown(f"<div class='topic-row'>{t['icone']}&nbsp;&nbsp;{t['nome']}</div>", unsafe_allow_html=True)
            
    with c_m:
        for t in grupo["topicos"]:
            dado_topico = df_filtrado[df_filtrado['TOPICO'] == t['nome']]
            val_meta = dado_topico['V. META'].values[0] if not dado_topico.empty and pd.notna(dado_topico['V. META'].values[0]) else 0
            st.markdown(f"<div class='val-box'>{int(val_meta):,}</div>".replace(",", "."), unsafe_allow_html=True)
            
    with c_a:
        for t in grupo["topicos"]:
            dado_topico = df_filtrado[df_filtrado['TOPICO'] == t['nome']]
            val_real = dado_topico['V. ALCANÇADO'].values[0] if not dado_topico.empty and pd.notna(dado_topico['V. ALCANÇADO'].values[0]) else 0
            st.markdown(f"<div class='val-box'>{int(val_real):,}</div>".replace(",", "."), unsafe_allow_html=True)

# Rodapé
st.markdown("<div class='footer-quote'>\"Eu plantei; Apolo regou; mas Deus deu o crescimento.\" (1 Coríntios 3:6)</div>", unsafe_allow_html=True)