import streamlit as st
import pandas as pd

# Configuração da Página
st.set_page_config(
    page_title="Visão para a Área Brasil",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Estilização CSS Customizada
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
    
    /* Agrupador da Responsabilidade */
    .pillar-box-merged {
        background-color: #0d1e30;
        border-radius: 6px;
        padding: 10px;
        font-weight: bold;
        font-size: 13px;
        text-align: center;
        border: 1px solid #1a334e;
        height: 94px;
        display: flex;
        align-items: center;
        justify-content: center;
        line-height: 1.3;
        box-sizing: border-box;
        margin-bottom: 12px;
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
    
    /* Linha do Tópico */
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
        box-sizing: border-box;
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

    /* Destaque para a coluna Falta */
    .val-box-falta {
        background-color: #1a2332;
        color: #ff8a80;
        text-align: center;
        height: 44px;
        line-height: 44px;
        border-radius: 4px;
        font-size: 17px;
        font-weight: bold;
        border: 1px solid #3c242e;
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

# Função para carregar os dados do Excel
@st.cache_data
def carregar_dados():
    try:
        # Lê todas as abas caso haja mais de um ano
        xls = pd.ExcelFile("DADOS.xlsx")
        dfs = []
        for sheet_name in xls.sheet_names:
            dfs.append(pd.read_excel(xls, sheet_name=sheet_name))
        df = pd.concat(dfs, ignore_index=True)
        return df
    except Exception as e:
        st.error(f"Erro ao carregar o arquivo DADOS.xlsx: {e}")
        return pd.DataFrame()

df = carregar_dados()

# Título Principal
st.markdown("<p class='main-title'>VISÃO PARA A ÁREA BRASIL - ESTACA MACEIÓ BRASIL LITORAL</p>", unsafe_allow_html=True)

if not df.empty:
    # Filtros de Seleção (Ano e Unidade)
    col_f1, col_f2 = st.columns([1, 4])
    
    with col_f1:
        st.caption("ANO")
        anos_disponiveis = sorted(df['ANO'].dropna().unique().astype(int))
        ano_sel = st.radio("Selecione o Ano", anos_disponiveis, horizontal=True, label_visibility="collapsed")
        
    with col_f2:
        st.caption("UNIDADE")
        unidades_disponiveis = df['UNIDADES'].dropna().unique().tolist()
        unid_sel = st.radio("Selecione a Unidade", unidades_disponiveis, horizontal=True, label_visibility="collapsed")
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    # Filtrar dados
    df_filtrado = df[(df['ANO'] == ano_sel) & (df['UNIDADES'] == unid_sel)]
    
    # Definição dos Grupos e Tópicos
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
                {"nome": "Missionários Servindo do Brasil", "icone": "🏙"}
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

    # Cabeçalho da Tabela (Agrupado com a nova coluna FALTA)
    col1, col2, col3, col4, col5 = st.columns([2.5, 5, 2, 2, 2])
    with col1:
        st.markdown("<div class='grid-header'>RESPONSABILIDADES</div>", unsafe_allow_html=True)
    with col2:
        st.markdown("<div class='grid-header'>INDICADOR / TÓPICO</div>", unsafe_allow_html=True)
    with col3:
        st.markdown("<div class='grid-header'>META</div>", unsafe_allow_html=True)
    with col4:
        st.markdown("<div class='grid-header'>ALCANÇADO</div>", unsafe_allow_html=True)
    with col5:
        st.markdown("<div class='grid-header'>FALTA</div>", unsafe_allow_html=True)
        
    st.markdown("<div style='margin-bottom: 10px;'></div>", unsafe_allow_html=True)

    # Renderização dos Blocos
    for grupo in grupos_responsabilidades:
        col1, col2, col3, col4, col5 = st.columns([2.5, 5, 2, 2, 2])
        
        # Coluna 1: Responsabilidade (Mesclada visualmente)
        with col1:
            st.markdown(
                f"<div class='pillar-box-merged {grupo['classe']}'>{grupo['pilar']}</div>", 
                unsafe_allow_html=True
            )
            
        # Colunas 2, 3, 4 e 5: Tópicos, Metas, Alcançados e Falta
        with col2:
            for t in grupo["topicos"]:
                st.markdown(
                    f"<div class='topic-row'>{t['icone']}&nbsp;&nbsp;{t['nome']}</div>", 
                    unsafe_allow_html=True
                )
                
        with col3:
            for t in grupo["topicos"]:
                dado_topico = df_filtrado[df_filtrado['TOPICO'].str.strip().str.lower() == t['nome'].strip().lower()]
                val_meta = int(dado_topico['V. META'].values[0]) if not dado_topico.empty and pd.notna(dado_topico['V. META'].values[0]) else 0
                st.markdown(f"<div class='val-box'>{val_meta}</div>", unsafe_allow_html=True)
                
        with col4:
            for t in grupo["topicos"]:
                dado_topico = df_filtrado[df_filtrado['TOPICO'].str.strip().str.lower() == t['nome'].strip().lower()]
                val_alc = int(dado_topico['V. ALCANÇADO'].values[0]) if not dado_topico.empty and pd.notna(dado_topico['V. ALCANÇADO'].values[0]) else 0
                st.markdown(f"<div class='val-box'>{val_alc}</div>", unsafe_allow_html=True)

        with col5:
            for t in grupo["topicos"]:
                dado_topico = df_filtrado[df_filtrado['TOPICO'].str.strip().str.lower() == t['nome'].strip().lower()]
                val_falta = int(dado_topico['FALTA'].values[0]) if not dado_topico.empty and pd.notna(dado_topico['FALTA'].values[0]) else 0
                st.markdown(f"<div class='val-box-falta'>{val_falta}</div>", unsafe_allow_html=True)

# Rodapé com citação
st.markdown("<p class='footer-quote'>\"Eu plantei; Apolo regou; mas Deus deu o crescimento.\" (1 Coríntios 3:6)</p>", unsafe_allow_html=True)