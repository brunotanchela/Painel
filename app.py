import time
import streamlit as st

# CONFIGURAÇÕES (edite aqui)
TEMPO_EXIBICAO = 10      # segundos que a página do grupo fica aberta
COLUNAS = 4              # botões por linha na tela inicial

GRUPOS = [
    {
        "tema": "ODS 3.9",
        "integrantes": "BRUNO T, MATHEUS S, CRISTIAN, VITOR G e JOÃO SETTI",
        "subtema": "Saneamento básico e tratamento d'água.",
        "conteudo": "SIGA A LINHA VERDE NO CHÃO.",
        "cor": "#008000"
    },
    {
        "tema": "ODS 3.6",
        "integrantes": "BRUNO P, GIOVANNA R, LETÍCIA e RAFAELA",
        "subtema": "Acidentes e prevenção.",
        "conteudo": "SIGA A LINHA VERDE NO CHÃO.",
        "cor": "#008000",
    },
    {
        "tema": "ODS 3.8",
        "integrantes": "GABRIELA, JOÃO SOUSA, LAURA, CAMILA e REBECA",
        "subtema": "Vacinas e medicamentos. (Laboratório)",
        "conteudo": "SIGA A LINHA ROXA NO CHÃO.",
        "cor": "#800080",
    },
    {
        # ligado com os dois de baixo
        "tema": "ODS 3.7",
        "integrantes": "BEATRIZ F, DANIEL V, EDUARDA T, JOSÉ, LARA e VICENZO",
        "subtema": "Saúde sexual e reprodutiva.",
        "conteudo": "SIGA A LINHA ROSA NO CHÃO.",
        "cor": "#FF007F",
    }, 
   {
        "tema": "ODS 3.4",
        "integrantes": "JOÃO DAVI, MATEUS R, MARIA EDUARDA, MILENA e VINÍCIUS",
        "subtema": "Saúde mental e bem-estar.",
        "conteudo": "SIGA A LINHA ROSA NO CHÃO.",
        "cor": "#FF007F",
    },
    {
        "tema": "ODS 3.1 e 3.2",
        "integrantes": "GIOVANA N, DANIEL C, EDUARDO e MIGUEL",
        "subtema": "Mortalidade materna e infantil.",
        "conteudo": "SIGA A LINHA ROSA NO CHÃO",
        "cor": "#FF007F",
    },
    {
        "tema": "ODS 3.3",
        "integrantes": "BEATRIZ T, BEATRIZ S e ALEXANDRE M",
        "subtema": "Doenças transmissíveis.",
        "conteudo": "SIGA A LINHA LARANJA NO CHÃO.",
        "cor": "#ffa500",
    },
    {
        "tema": "ODS 3.4",
        "integrantes": "GABRIEL SOUZA e MURILO B",
        "subtema": "Doenças não-transmissíveis.",
        "conteudo": "SIGA A LINHA LARANJA NO CHÃO.",
        "cor": "#ffa500",
    },
    {
        "tema": "ODS 3.9",
        "integrantes": "ANA LUIZA, ELLOÁ, ISABELLE e HELOISA",
        "subtema": "Poluição do ar. (Laboratório)",
        "conteudo": "SIGA A LINHA ROXA NO CHÃO.",
        "cor": "#800080",
    },
    {
        "tema": "ODS 3.5",
        "integrantes": "CAMILLA, DAVI, CHRISTIELLY e MANUELA",
        "subtema": "Álcool e drogas.",
        "conteudo": "SIGA A LINHA LARANJA NO CHÃO.",
        "cor": "#ffa500",
    },
    {
        "tema": "ODS 3.0.a",
        "integrantes": "NICOLAS, MELISSA e LUANA",
        "subtema": "Tabagismo.",
        "conteudo": "SIGA A LINHA LARANJA NO CHÃO.",
        "cor": "#ffa500",
    },
    {
        "tema": "ODS 3.4",
        "integrantes": "HENRIQUE e JUAN",
        "subtema": "Alimentação e saúde.",
        "conteudo": "SIGA A LINHA AMARELA NO CHÃO.",
        "cor": "#FFFF00",
    },
    # ainda estão faltando:
    # poluição e saúde (2 gp do lab), tabagismo, uso de drogas e álcool, alimentação e saúde
]

# PÁGINA E ESTILO
st.set_page_config(page_title="EXPOCAMP 2A e 2B", layout="wide")

# ---------- TELA LIMPA: esconde barra superior, menu, Deploy e rodapé ----------
ESTILO_LIMPO = """
<style>
header[data-testid="stHeader"],
[data-testid="stToolbar"],
[data-testid="stDecoration"],
[data-testid="stStatusWidget"],
[data-testid="stAppDeployButton"],
.stDeployButton,
#MainMenu,
footer,
[class*="viewerBadge"],
[class*="ProfileContainer"],
[class*="profileContainer"] {
    display: none !important;
    visibility: hidden !important;
}
/* Sem a barra superior, reduz o espaço vazio no topo da página */
[data-testid="stMainBlockContainer"],
.block-container {
    padding-top: 2rem !important;
}
</style>
"""
st.markdown(ESTILO_LIMPO, unsafe_allow_html=True)


st.markdown(
    """
    <style>
    /* Botões grandes da tela inicial */
    div[class*="st-key-grupo_"] button {
        min-height: 230px;
        width: 100%;
        padding: 1.2rem;
        border-radius: 18px;
        text-align: center;
    }
    /* Empilha as 3 linhas (o Streamlit as coloca lado a lado por padrão) */
    div[class*="st-key-grupo_"] button div[data-testid="stMarkdownContainer"] {
        display: flex !important;
        flex-direction: column !important;
        align-items: center !important;
        justify-content: center !important;
        width: 100% !important;
        text-align: center;
    }
    div[class*="st-key-grupo_"] button p {
        display: block !important;
        width: 100% !important;
        white-space: normal !important;   /* permite quebrar linha em textos longos */
        overflow: visible !important;
        text-overflow: clip !important;
        text-align: center !important;
    }
    /* 1ª linha do botão: TEMA (maior) */
    div[class*="st-key-grupo_"] button p:nth-of-type(1) {
        font-size: 2.4rem;
        font-weight: 800;
        line-height: 1.2;
        margin-bottom: 0.6rem;
    }
    /* 2ª linha: INTEGRANTES */
    div[class*="st-key-grupo_"] button p:nth-of-type(2) {
        font-size: 1.5rem;
        line-height: 1.3;
        margin-bottom: 0.6rem;
    }
    /* 3ª linha: SUBTEMA */
    div[class*="st-key-grupo_"] button p:nth-of-type(3) {
        font-size: 1.5rem;
        font-style: italic;
        line-height: 1.3;
        margin-bottom: 0;
    }
    /* Página do grupo */
    .grupo-tema { font-size: 4rem; font-weight: 800; text-align: center; }
    .grupo-integrantes { font-size: 2.2rem; text-align: center; margin-top: 1rem; }
    .grupo-subtema { font-size: 2.2rem; font-style: italic; text-align: center; margin-top: 1rem; }
    .grupo-conteudo { font-size: 4rem; text-align: center; margin-top: 2rem; }
    </style>
    """,
    unsafe_allow_html=True,
)

# ESTADO
if "pagina" not in st.session_state:
    st.session_state.pagina = "home"
if "entrada" not in st.session_state:
    st.session_state.entrada = 0.0


def abrir_grupo(indice: int) -> None:
    st.session_state.pagina = indice
    st.session_state.entrada = time.time()


def voltar_home() -> None:
    st.session_state.pagina = "home"


def abrir_slides() -> None:
    st.session_state.pagina = "slides"
    st.session_state.slide = 0
    st.session_state.entrada = time.time()


def proximo_slide() -> None:
    # Avança para o próximo grupo e, depois do último, recomeça do primeiro.
    st.session_state.slide = (st.session_state.slide + 1) % len(GRUPOS)
    st.session_state.entrada = time.time()


# TELA INICIAL
def tela_inicial() -> None:
    st.markdown(
        "<h1 style='text-align:center;'>Onde gostaria de ir?</h1>",
        unsafe_allow_html=True,
    )

    for inicio in range(0, len(GRUPOS), COLUNAS):
        colunas = st.columns(COLUNAS)
        for coluna, indice in zip(colunas, range(inicio, inicio + COLUNAS)):
            if indice >= len(GRUPOS):
                break
            g = GRUPOS[indice]
            integrantes = g["integrantes"] or "—"
            # Três linhas (parágrafos) empilhadas dentro do mesmo botão.
            rotulo = f"{g['tema']}\n\n{integrantes}\n\n{g['subtema']}"
            with coluna:
                st.button(
                    rotulo,
                    key=f"grupo_{indice}",
                    use_container_width=True,
                    on_click=abrir_grupo,
                    args=(indice,),
                )

    # Botão "Slide view" no fim da página (só aparece depois de rolar tudo).
    st.markdown("<div style='height:120px'></div>", unsafe_allow_html=True)
    st.divider()
    _, centro, _ = st.columns([2, 1, 2])
    with centro:
        st.button(
            "Slide view",
            key="slide_view",
            use_container_width=True,
            on_click=abrir_slides,
        )


# PÁGINA DO GRUPO (volta sozinha após TEMPO_EXIBICAO segundos)
@st.fragment(run_every=1)
def contagem_regressiva(slides: bool = False) -> None:
    restante = TEMPO_EXIBICAO - (time.time() - st.session_state.entrada)
    if restante <= 0:
        if slides:
            proximo_slide()   # slide view: passa para o próximo grupo
        else:
            voltar_home()     # página de um grupo: volta à tela inicial
        st.rerun()  # recarrega o app inteiro
    if slides:
        texto = (
            f"Próximo slide em {int(restante) + 1}s…  "
            f"({st.session_state.slide + 1}/{len(GRUPOS)})"
        )
    else:
        texto = f"Voltando à página inicial em {int(restante) + 1}s…"
    st.progress(min(max(restante / TEMPO_EXIBICAO, 0.0), 1.0), text=texto)


def pagina_grupo(indice: int, slides: bool = False) -> None:
    g = GRUPOS[indice]
    cor = g.get("cor", "inherit")

    # Pinta a barra de contagem regressiva com a cor do grupo.
    st.markdown(
        f"""<style>
        div[data-testid="stProgress"] [data-testid="stProgressBarTrack"] > div {{
            background-color: {cor} !important;
        }}
        </style>""",
        unsafe_allow_html=True,
    )
    integrantes = g["integrantes"] or "—"
    # Cor do conteúdo deste grupo; sem "cor" definida, usa a cor padrão do texto.
    cor = g.get("cor", "inherit")

    st.markdown(f"<div class='grupo-tema'>{g['tema']}</div>", unsafe_allow_html=True)
    st.markdown(
        f"<div class='grupo-integrantes'>{integrantes}</div>", unsafe_allow_html=True
    )
    st.markdown(f"<div class='grupo-subtema'>{g['subtema']}</div>", unsafe_allow_html=True)
    st.markdown(
        f"<div class='grupo-conteudo' style='color:{cor}'>{g['conteudo']}</div>",
        unsafe_allow_html=True
    )

    st.write("")
    contagem_regressiva(slides)
    if slides:
        st.button("Voltar", key="voltar_slides", on_click=voltar_home)
    else:
        st.button("Voltar agora", on_click=voltar_home)


# ROTEAMENTO
if st.session_state.pagina == "home":
    tela_inicial()
elif st.session_state.pagina == "slides":
    pagina_grupo(st.session_state.slide, slides=True)
else:
    pagina_grupo(st.session_state.pagina)