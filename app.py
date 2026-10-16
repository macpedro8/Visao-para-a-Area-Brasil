import streamlit as st
import pandas as pd

# Configuração da Página
st.set_page_config(
    page_title="Visão para a Área Brasil",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Estilização CSS Customizada (Preservando 100% do layout aprovado)
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

    /* ESTILIZAÇÃO DO ST.SEGMENTED_CONTROL */
    div[data-testid="stSegmentedControl"] {
        background-color: #0d1e30 !important;
        padding: 3px !important;
        border-radius: 6px !important;
        border: 1px solid #1a334e !important;
    }

    div[data-testid="stSegmentedControl"] button {
        background-color: transparent !important;
        color: #a0aec0 !important;
        border: none !important;
        border-right: 1px solid #1a334e !important;
        border-radius: 0px !important;
        font-size: 13px !important;
        font-weight: 600 !important;
        padding: 6px 14px !important;
    }

    div[data-testid="stSegmentedControl"] button:last-child {
        border-right: none !important;
    }

    div[data-testid="stSegmentedControl"] button[aria-selected="true"] {
        background-color: #2a1b28 !important;
        color: #ff5252 !important;
        border: 1px solid #ff5252 !important;
        border-radius: 4px !important;
        font-weight: bold !important;
    }
    
    /* ESCONDE 100% DAS BOLINHAS DO ST.RADIO (FALLBACK) */
    div[data-testid="stRadio"] [role="radiogroup"] label {
        background-color: transparent !important;
        color: #a0aec0 !important;
        padding: 6px 14px !important;
        margin: 0px !important;
        border-right: 1px solid #1a334e !important;
        font-size: 13px !important;
        font-weight: 600 !important;
    }

    div[data-testid="stRadio"] [role="radiogroup"] label > div:first-child {
        display: none !important;
        width: 0 !important;
        height: 0 !important;
        margin: 0 !important;
        padding: 0 !important;
    }

    div[data-testid="stRadio"] [role="radiogroup"] {
        background-color: #0d1e30;
        padding: 3px;
        border-radius: 6px;
        border: 1px solid #1a334e;
        display: flex;
        flex-direction: row;
        width: fit-content;
    }

    div[data-testid="stRadio"] [role="radiogroup"] label:has(input:checked) {
        background-color: #2a1b28 !important;
        color: #ff5252 !important;
        border: 1px solid #ff5252 !important;
        border-radius: 4px !important;
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
        gap: 10px;
    }

    .icon-container {
        display: inline-flex;
        align-items: center;
        justify-content: center;
        width: 24px;
        height: 24px;
    }
    
    /* Caixas de Valores */
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

# Definição dos Ícones Vetoriais SVG Customizados
ICONS = {
    "igreja": """<svg class="icon-container" viewBox="0 0 24 24" fill="none" stroke="#00b4d8" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M12 2v6m-3-3h6"/><path d="M4 22V10l8-5 8 5v12H4z"/><path d="M10 22v-5a2 2 0 0 1 4 0v5"/></svg>""",
    "membros": """<svg class="icon-container" viewBox="0 0 24 24" fill="none" stroke="#8bc34a" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M17 21v-2a4 4 0 0 0-4-4H5a4 4 0 0 0-4 4v2"/><circle cx="9" cy="7" r="4"/><path d="M23 21v-2a4 4 0 0 0-3-3.87"/><path d="M16 3.13a4 4 0 0 1 0 7.75"/></svg>""",
    "retornando": """<svg class="icon-container" viewBox="0 0 24 24" fill="none" stroke="#ffb74d" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M11 15h2a2 2 0 1 0 0-4h-3c-.6 0-1.1.2-1.4.6L3 17"/><path d="m7 21 1.6-1.4c.4-.4.4-1 0-1.4l-2.2-2.2"/><path d="M13 9h2a2 2 0 1 0 0-4h-3c-.6 0-1.1.2-1.4.6L7 9"/><path d="m21 15-3-3m0 0 3-3m-3 3h8"/></svg>""",
    "jejum": """<svg class="icon-container" viewBox="0 0 24 24" fill="none" stroke="#ffb74d" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M6 14c-2.5 0-4 1.5-4 3.5S3.5 21 6 21s4-1.5 4-3.5S8.5 14 6 14z"/><path d="M15 5h5l1 12a3 3 0 0 1-3 3h-1a3 3 0 0 1-3-3L15 5z"/><path d="M15 9h6"/></svg>""",
    "batismo": """<svg class="icon-container" viewBox="0 0 24 24" fill="none" stroke="#4dd0e1" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="5" r="2.5"/><path d="M12 9v6"/><path d="M9 12h6"/><path d="M2 18c2 0 3 1 5 1s3-1 5-1 3 1 5 1 3-1 5-1"/><path d="M2 21c2 0 3 1 5 1s3-1 5-1 3 1 5 1 3-1 5-1"/></svg>""",
    "missionarios": """<svg class="icon-container" viewBox="0 0 24 24" fill="#ffffff" stroke="#4dd0e1" stroke-width="1.5"><rect x="3" y="8" width="8" height="12" rx="1" fill="#ffffff" stroke="#4dd0e1"/><rect x="13" y="8" width="8" height="12" rx="1" fill="#ffffff" stroke="#4dd0e1"/><circle cx="7" cy="4" r="2" fill="#4dd0e1"/><circle cx="17" cy="4" r="2" fill="#4dd0e1"/><rect x="4.5" y="10" width="3.5" height="2" rx="0.5" fill="#000000"/><rect x="14.5" y="10" width="3.5" height="2" rx="0.5" fill="#000000"/><path d="M7 12v6M17 12v6" stroke="#000000" stroke-width="1"/></svg>""",
    "templo_azul": """<svg class="icon-container" viewBox="0 0 24 24" fill="none" stroke="#00b4d8" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M12 2v4"/><path d="M12 6l-3 3h6l-3-3z"/><path d="M5 22V11l7-4 7 4v11H5z"/><path d="M9 22v-4a3 3 0 0 1 6 0v4"/><circle cx="12" cy="2" r="1" fill="#00b4d8"/></svg>""",
    "templo_cinza": """<svg class="icon-container" viewBox="0 0 24 24" fill="none" stroke="#8a9ba8" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M12 2v4"/><path d="M12 6l-3 3h6l-3-3z"/><path d="M5 22V11l7-4 7 4v11H5z"/><path d="M9 22v-4a3 3 0 0 1 6 0v4"/><circle cx="12" cy="2" r="1" fill="#8a9ba8"/></svg>"""
}

# Função para carregar os dados do Excel
@st.cache_data(ttl=60)
def carregar_dados():
    try:
        xls = pd.ExcelFile("DADOS.xlsx")
        dfs = []
        for sheet_name in xls.sheet_names:
            temp_df = pd.read_excel(xls, sheet_name=sheet_name)
            temp_df.columns = temp_df.columns.astype(str).str.strip().str.upper()
            dfs.append(temp_df)
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
        if hasattr(st, "segmented_control"):
            ano_sel = st.segmented_control("ANO", anos_disponiveis, default=anos_disponiveis[0], label_visibility="collapsed")
        else:
            ano_sel = st.radio("ANO", anos_disponiveis, horizontal=True, label_visibility="collapsed")
        
    with col_f2:
        st.caption("UNIDADE")
        unidades_disponiveis = df['UNIDADES'].dropna().unique().tolist()
        if hasattr(st, "segmented_control"):
            unid_sel = st.segmented_control("UNIDADE", unidades_disponiveis, default=unidades_disponiveis[0], label_visibility="collapsed")
        else:
            unid_sel = st.radio("UNIDADE", unidades_disponiveis, horizontal=True, label_visibility="collapsed")
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    if ano_sel is None and len(anos_disponiveis) > 0:
        ano_sel = anos_disponiveis[0]
    if unid_sel is None and len(unidades_disponiveis) > 0:
        unid_sel = unidades_disponiveis[0]
    
    # Filtrar dados
    df_filtrado = df[(df['ANO'] == ano_sel) & (df['UNIDADES'] == unid_sel)]
    
    # Definição dos Grupos e Tópicos com SVG Vetorial
    grupos_responsabilidades = [
        {
            "pilar": "VIVER O EVANGELHO DE JESUS CRISTO",
            "classe": "p-viver",
            "topicos": [
                {"nome": "Frequência da Reunião Sacramental", "icone": ICONS["igreja"]},
                {"nome": "Membros Participantes", "icone": ICONS["membros"]}
            ]
        },
        {
            "pilar": "CUIDAR DOS NECESSITADOS",
            "classe": "p-cuidar",
            "topicos": [
                {"nome": "Membros Retornando", "icone": ICONS["retornando"]},
                {"nome": "Membros Jejuando", "icone": ICONS["jejum"]}
            ]
        },
        {
            "pilar": "CONVIDAR TODOS A RECEBER O EVANGELHO",
            "classe": "p-convidar",
            "topicos": [
                {"nome": "Batismos de Conversos", "icone": ICONS["batismo"]},
                {"nome": "Missionários Servindo do Brasil", "icone": ICONS["missionarios"]}
            ]
        },
        {
            "pilar": "UNIR AS FAMÍLIAS POR TODA A ETERNIDADE",
            "classe": "p-unir",
            "topicos": [
                {"nome": "Recomendações para o Templo - Membros com Investidura", "icone": ICONS["templo_azul"]},
                {"nome": "Recomendações para o Templo - Membros sem Investidura", "icone": ICONS["templo_cinza"]}
            ]
        }
    ]

    # Cabeçalho da Tabela
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
        
        # Coluna 1: Responsabilidade
        with col1:
            st.markdown(
                f"<div class='pillar-box-merged {grupo['classe']}'>{grupo['pilar']}</div>", 
                unsafe_allow_html=True
            )
            
        # Coluna 2: Tópicos com Ícones SVG
        with col2:
            for t in grupo["topicos"]:
                st.markdown(
                    f"<div class='topic-row'>{t['icone']}<span>{t['nome']}</span></div>", 
                    unsafe_allow_html=True
                )
                
        # Coluna 3: Meta
        with col3:
            for t in grupo["topicos"]:
                dado_topico = df_filtrado[df_filtrado['TOPICO'].astype(str).str.strip().str.lower() == t['nome'].strip().lower()]
                val_meta = int(dado_topico['V. META'].values[0]) if not dado_topico.empty and 'V. META' in dado_topico and pd.notna(dado_topico['V. META'].values[0]) else 0
                st.markdown(f"<div class='val-box'>{val_meta}</div>", unsafe_allow_html=True)
                
        # Coluna 4: Alcançado
        with col4:
            for t in grupo["topicos"]:
                dado_topico = df_filtrado[df_filtrado['TOPICO'].astype(str).str.strip().str.lower() == t['nome'].strip().lower()]
                val_alc = int(dado_topico['V. ALCANÇADO'].values[0]) if not dado_topico.empty and 'V. ALCANÇADO' in dado_topico and pd.notna(dado_topico['V. ALCANÇADO'].values[0]) else 0
                st.markdown(f"<div class='val-box'>{val_alc}</div>", unsafe_allow_html=True)

        # Coluna 5: Falta
        with col5:
            for t in grupo["topicos"]:
                dado_topico = df_filtrado[df_filtrado['TOPICO'].astype(str).str.strip().str.lower() == t['nome'].strip().lower()]
                
                val_meta = int(dado_topico['V. META'].values[0]) if not dado_topico.empty and 'V. META' in dado_topico and pd.notna(dado_topico['V. META'].values[0]) else 0
                val_alc = int(dado_topico['V. ALCANÇADO'].values[0]) if not dado_topico.empty and 'V. ALCANÇADO' in dado_topico and pd.notna(dado_topico['V. ALCANÇADO'].values[0]) else 0
                
                if not dado_topico.empty and 'FALTA' in dado_topico and pd.notna(dado_topico['FALTA'].values[0]):
                    val_falta = int(dado_topico['FALTA'].values[0])
                else:
                    val_falta = val_meta - val_alc
                    
                st.markdown(f"<div class='val-box-falta'>{val_falta}</div>", unsafe_allow_html=True)

# Rodapé
st.markdown("<p class='footer-quote'>\"Eu plantei; Apolo regou; mas Deus deu o crescimento.\" (1 Coríntios 3:6)</p>", unsafe_allow_html=True)