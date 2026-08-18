import streamlit as st
import pandas as pd
import plotly.express as px

# ============================================================
# CONFIGURACIÓN GENERAL
# ============================================================

st.set_page_config(
    page_title="Minecraft & Emociones",
    page_icon="⛏️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ============================================================
# ESTILOS
# ============================================================

st.markdown("""
<style>

    /* ------------------------------
       FONDO GENERAL
    ------------------------------ */

    .stApp {
        background:
            linear-gradient(
                rgba(224, 242, 216, 0.88),
                rgba(224, 242, 216, 0.88)
            ),
            linear-gradient(
                135deg,
                #87CEEB 0%,
                #dff2d8 35%,
                #c7d8c0 70%,
                #9bb88b 100%
            );
    }

    /* ------------------------------
       CONTENEDOR PRINCIPAL
    ------------------------------ */

    .main .block-container {
        max-width: 1250px;
        padding-top: 2rem;
        padding-bottom: 3rem;
    }

    /* ------------------------------
       TÍTULO PRINCIPAL
    ------------------------------ */

    .main-title {
        background: linear-gradient(
            135deg,
            #245501,
            #3f8f18,
            #6aaa32
        );
        color: white;
        padding: 30px;
        border-radius: 18px;
        text-align: center;
        border: 5px solid #5c3b1e;
        box-shadow:
            0 8px 0 #5c3b1e,
            0 12px 25px rgba(0,0,0,0.25);
        margin-bottom: 25px;
    }

    .main-title h1 {
        font-size: 3rem;
        margin: 0;
        font-weight: 900;
        text-shadow: 3px 3px 0 #234d08;
    }

    .main-title p {
        font-size: 1.15rem;
        margin-top: 10px;
        margin-bottom: 0;
    }

    /* ------------------------------
       TARJETAS
    ------------------------------ */

    .block-card {
        background: rgba(255,255,255,0.94);
        border: 3px solid #5c3b1e;
        border-radius: 15px;
        padding: 22px;
        margin-bottom: 20px;
        box-shadow:
            0 5px 0 #5c3b1e,
            0 10px 20px rgba(0,0,0,0.12);
        transition: transform 0.2s ease;
    }

    .block-card:hover {
        transform: translateY(-3px);
    }

    .grass-card {
        background: linear-gradient(
            135deg,
            #6aaa32,
            #3f8f18
        );
        color: white;
        border: 3px solid #315f10;
        border-radius: 15px;
        padding: 20px;
        box-shadow: 0 5px 0 #234d08;
        margin-bottom: 18px;
    }

    .stone-card {
        background: linear-gradient(
            135deg,
            #e0e0e0,
            #b7b7b7
        );
        border: 3px solid #666666;
        border-radius: 15px;
        padding: 20px;
        box-shadow: 0 5px 0 #555555;
        margin-bottom: 18px;
    }

    .sky-card {
        background: linear-gradient(
            135deg,
            #d9f3ff,
            #9edcff
        );
        border: 3px solid #3984a8;
        border-radius: 15px;
        padding: 20px;
        box-shadow: 0 5px 0 #28647e;
        margin-bottom: 18px;
    }

    /* ------------------------------
       MÉTRICAS
    ------------------------------ */

    div[data-testid="stMetric"] {
        background: rgba(255,255,255,0.95);
        border: 3px solid #5c3b1e;
        border-radius: 14px;
        padding: 18px;
        box-shadow: 0 5px 0 #5c3b1e;
    }

    div[data-testid="stMetricLabel"] {
        font-weight: bold;
    }

    /* ------------------------------
       BOTONES
    ------------------------------ */

    .stButton > button {
        width: 100%;
        min-height: 50px;
        border-radius: 12px;
        border: 3px solid #5c3b1e;
        background: linear-gradient(
            135deg,
            #6aaa32,
            #3f8f18
        );
        color: white;
        font-weight: 800;
        font-size: 1rem;
        box-shadow: 0 4px 0 #5c3b1e;
        transition: all 0.15s ease;
    }

    .stButton > button:hover {
        transform: translateY(-2px);
        box-shadow: 0 6px 0 #5c3b1e;
        color: white;
    }

    /* ------------------------------
       SIDEBAR
    ------------------------------ */

    section[data-testid="stSidebar"] {
        background:
            linear-gradient(
                180deg,
                #315f10 0%,
                #3f8f18 45%,
                #5c3b1e 100%
            );
    }

    section[data-testid="stSidebar"] * {
        color: white;
    }

    /* ------------------------------
       INPUTS
    ------------------------------ */

    div[data-baseweb="input"],
    div[data-baseweb="select"] {
        border-radius: 10px;
    }

    /* ------------------------------
       SEPARADORES
    ------------------------------ */

    .pixel-line {
        height: 8px;
        background:
            repeating-linear-gradient(
                90deg,
                #5c3b1e 0px,
                #5c3b1e 25px,
                #6aaa32 25px,
                #6aaa32 50px
            );
        border-radius: 5px;
        margin: 25px 0;
    }

    /* ------------------------------
       LOGROS
    ------------------------------ */

    .achievement {
        background: rgba(255,255,255,0.96);
        border: 3px solid #5c3b1e;
        border-radius: 15px;
        padding: 18px;
        text-align: center;
        height: 100%;
        box-shadow: 0 5px 0 #5c3b1e;
    }

    .achievement-unlocked {
        background: linear-gradient(
            135deg,
            #fff6b3,
            #ffe47a
        );
    }

    .achievement-icon {
        font-size: 2.7rem;
    }

    /* ------------------------------
       CONTADOR
    ------------------------------ */

    .counter {
        background: #5c3b1e;
        color: white;
        padding: 10px 18px;
        border-radius: 12px;
        text-align: center;
        font-weight: bold;
        margin-top: 15px;
    }

    /* ------------------------------
       RESPONSIVE
    ------------------------------ */

    @media (max-width: 768px) {

        .main .block-container {
            padding: 1rem;
        }

        .main-title {
            padding: 20px 12px;
        }

        .main-title h1 {
            font-size: 2rem;
        }

        .main-title p {
            font-size: 0.95rem;
        }
    }

</style>
""", unsafe_allow_html=True)


# ============================================================
# DATOS DE LA ENCUESTA
# ============================================================

COLUMNAS = [
    "Edad",
    "Juega Minecraft",
    "Frecuencia",
    "Horas al día",
    "Estado emocional",
    "Ayuda a relajarse",
    "Ayuda a distraerse",
    "Juega con amigos",
    "Mejora el estado de ánimo"
]


# ============================================================
# INICIALIZACIÓN DEL ESTADO
# ============================================================

# st.session_state permite conservar información mientras la
# sesión actual de Streamlit permanezca activa.
#
# IMPORTANTE:
# Estos datos son TEMPORALES y pertenecen a la sesión.
# Si se necesita almacenamiento permanente y compartido entre
# diferentes usuarios, posteriormente se puede conectar
# Firebase, Supabase o una base de datos SQL.

if "respuestas" not in st.session_state:
    st.session_state.respuestas = pd.DataFrame(columns=COLUMNAS)

if "confirmar_borrado" not in st.session_state:
    st.session_state.confirmar_borrado = False


# ============================================================
# FUNCIONES
# ============================================================

def obtener_datos():
    """Devuelve una copia segura del DataFrame actual."""
    return st.session_state.respuestas.copy()


def contar_respuestas():
    """Cuenta las respuestas registradas."""
    return len(st.session_state.respuestas)


def porcentaje(parte, total):
    """Calcula un porcentaje evitando divisiones por cero."""
    if total == 0:
        return 0

    return round((parte / total) * 100, 1)


def mostrar_titulo():
    """Muestra el encabezado principal."""

    st.markdown("""
    <div class="main-title">
        <h1>⛏️ Minecraft & Emociones</h1>
        <p>
            Explorando la relación entre Minecraft y nuestro bienestar emocional
        </p>
    </div>
    """, unsafe_allow_html=True)


def mostrar_contador():
    """Muestra el contador de respuestas."""

    total = contar_respuestas()

    st.markdown(
        f"""
        <div class="counter">
            📋 Respuestas registradas: {total}
        </div>
        """,
        unsafe_allow_html=True
    )


def mostrar_logros():
    """Muestra los logros según la cantidad de respuestas."""

    total = contar_respuestas()

    logros = [
        ("⛏️", "Primer pico", 1, "Registra tu primera respuesta."),
        ("🌱", "Constructor", 5, "Registra 5 respuestas."),
        ("💎", "Diamante", 20, "Registra 20 respuestas."),
        ("🏆", "Maestro constructor", 50, "Registra 50 respuestas.")
    ]

    st.subheader("🏆 Logros")

    columnas = st.columns(4)

    for i, (icono, nombre, requisito, descripcion) in enumerate(logros):

        desbloqueado = total >= requisito

        clase = "achievement achievement-unlocked" if desbloqueado else "achievement"

        estado = "✅ Desbloqueado" if desbloqueado else f"🔒 {requisito} respuestas"

        with columnas[i]:
            st.markdown(
                f"""
                <div class="{clase}">
                    <div class="achievement-icon">{icono}</div>
                    <h4>{nombre}</h4>
                    <p>{descripcion}</p>
                    <strong>{estado}</strong>
                </div>
                """,
                unsafe_allow_html=True
            )


def mostrar_inicio():

    mostrar_titulo()

    st.markdown("""
    <div class="grass-card">

    ## 🌎 ¡Bienvenido, explorador!

    Esta aplicación busca conocer cómo las personas perciben
    emocionalmente su experiencia al jugar Minecraft.

    Puedes responder la encuesta, consultar las estadísticas,
    observar las gráficas y conocer los resultados obtenidos.

    </div>
    """, unsafe_allow_html=True)

    mostrar_contador()

    st.markdown('<div class="pixel-line"></div>', unsafe_allow_html=True)

    col1, col2, col3 = st.columns(3)

    with col1:
        st.markdown("""
        <div class="block-card">
            <h2>⛏️ Explora</h2>
            <p>
            Responde algunas preguntas sobre tus hábitos
            relacionados con Minecraft.
            </p>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown("""
        <div class="block-card">
            <h2>📊 Analiza</h2>
            <p>
            Observa automáticamente las respuestas
            mediante estadísticas y gráficas.
            </p>
        </div>
        """, unsafe_allow_html=True)

    with col3:
        st.markdown("""
        <div class="block-card">
            <h2>💚 Descubre</h2>
            <p>
            Conoce qué emociones y percepciones aparecen
            entre las personas encuestadas.
            </p>
        </div>
        """, unsafe_allow_html=True)

    st.markdown('<div class="pixel-line"></div>', unsafe_allow_html=True)

    mostrar_logros()


def mostrar_encuesta():

    mostrar_titulo()

    st.markdown("""
    <div class="sky-card">

    ## 📝 Encuesta

    Responde las siguientes preguntas. No hay respuestas
    correctas o incorrectas: queremos conocer tu experiencia.

    </div>
    """, unsafe_allow_html=True)

    with st.form("formulario_encuesta", clear_on_submit=True):

        col1, col2 = st.columns(2)

        with col1:

            edad = st.number_input(
                "1. 🎂 Edad",
                min_value=5,
                max_value=100,
                value=None,
                step=1,
                placeholder="Escribe tu edad"
            )

            juega = st.radio(
                "2. 🎮 ¿Juegas Minecraft?",
                ["Sí", "No"],
                horizontal=True
            )

            frecuencia = st.selectbox(
                "3. 🕐 ¿Con qué frecuencia juegas?",
                [
                    "Todos los días",
                    "Varias veces por semana",
                    "Una vez por semana",
                    "Rara vez",
                    "No juego"
                ]
            )

            horas = st.number_input(
                "4. ⏱️ ¿Cuántas horas juegas aproximadamente al día?",
                min_value=0.0,
                max_value=24.0,
                value=0.0,
                step=0.5
            )

        with col2:

            emocion = st.selectbox(
                "5. 😊 ¿Cómo te sientes después de jugar Minecraft?",
                [
                    "😀 Muy feliz",
                    "😄 Feliz",
                    "😐 Igual",
                    "😟 Triste",
                    "😡 Molesto"
                ]
            )

            relajarse = st.selectbox(
                "6. 😌 ¿Minecraft te ayuda a relajarte?",
                [
                    "Mucho",
                    "Bastante",
                    "Poco",
                    "Nada"
                ]
            )

            distraerse = st.selectbox(
                "7. 🧠 ¿Minecraft te ayuda a distraerte de situaciones estresantes?",
                [
                    "Sí",
                    "A veces",
                    "No"
                ]
            )

            amigos = st.radio(
                "8. 👫 ¿Jugar Minecraft te permite compartir tiempo con amigos?",
                ["Sí", "No"],
                horizontal=True
            )

            estado_animo = st.radio(
                "9. 💚 ¿Consideras que Minecraft mejora tu estado de ánimo?",
                ["Sí", "A veces", "No"],
                horizontal=True
            )

        st.markdown('<div class="pixel-line"></div>', unsafe_allow_html=True)

        enviar = st.form_submit_button(
            "⛏️ GUARDAR RESPUESTA",
            use_container_width=True
        )

    if enviar:

        # Comprobación para evitar guardar formularios incompletos.
        if edad is None:
            st.error("⚠️ Por favor, introduce tu edad antes de guardar.")
            return

        if juega == "No":
            # No se inventan respuestas.
            # Solamente se conserva exactamente lo seleccionado.
            pass

        nueva_respuesta = {
            "Edad": int(edad),
            "Juega Minecraft": juega,
            "Frecuencia": frecuencia,
            "Horas al día": float(horas),
            "Estado emocional": emocion,
            "Ayuda a relajarse": relajarse,
            "Ayuda a distraerse": distraerse,
            "Juega con amigos": amigos,
            "Mejora el estado de ánimo": estado_animo
        }

        nueva_fila = pd.DataFrame([nueva_respuesta])

        st.session_state.respuestas = pd.concat(
            [
                st.session_state.respuestas,
                nueva_fila
            ],
            ignore_index=True
        )

        st.success("✅ ¡Respuesta guardada correctamente!")
        st.balloons()

    mostrar_contador()


def mostrar_estadisticas():

    mostrar_titulo()

    datos = obtener_datos()

    st.header("📊 Estadísticas")

    if datos.empty:
        st.info(
            "Todavía no hay datos suficientes. "
            "¡Registra la primera respuesta!"
        )
        mostrar_logros()
        return

    total = len(datos)

    juegan = int(
        (datos["Juega Minecraft"] == "Sí").sum()
    )

    no_juegan = int(
        (datos["Juega Minecraft"] == "No").sum()
    )

    felices = int(
        datos["Estado emocional"].isin(
            ["😀 Muy feliz", "😄 Feliz"]
        ).sum()
    )

    relajados = int(
        datos["Ayuda a relajarse"].isin(
            ["Mucho", "Bastante"]
        ).sum()
    )

    amigos = int(
        (datos["Juega con amigos"] == "Sí").sum()
    )

    columnas = st.columns(5)

    with columnas[0]:
        st.metric(
            "👥 Encuestados",
            total
        )

    with columnas[1]:
        st.metric(
            "🎮 Juegan Minecraft",
            juegan,
            f"{porcentaje(juegan, total)}%"
        )

    with columnas[2]:
        st.metric(
            "🚫 No juegan",
            no_juegan,
            f"{porcentaje(no_juegan, total)}%"
        )

    with columnas[3]:
        st.metric(
            "😀 Felices / Muy felices",
            felices,
            f"{porcentaje(felices, total)}%"
        )

    with columnas[4]:
        st.metric(
            "😌 Ayuda a relajarse",
            relajados,
            f"{porcentaje(relajados, total)}%"
        )

    st.markdown("<br>", unsafe_allow_html=True)

    columnas2 = st.columns(2)

    with columnas2[0]:
        st.metric(
            "👫 Juegan con amigos",
            amigos,
            f"{porcentaje(amigos, total)}%"
        )

    with columnas2[1]:
        st.metric(
            "📝 Total de registros",
            total
        )

    st.markdown('<div class="pixel-line"></div>', unsafe_allow_html=True)

    mostrar_logros()


def crear_grafica(datos, columna, titulo):

    conteo = (
        datos[columna]
        .value_counts()
        .rename_axis("Respuesta")
        .reset_index(name="Personas")
    )

    fig = px.bar(
        conteo,
        x="Respuesta",
        y="Personas",
        title=titulo,
        text="Personas"
    )

    fig.update_traces(
        textposition="outside"
    )

    fig.update_layout(
        template="plotly_white",
        title_x=0.5,
        margin=dict(
            l=20,
            r=20,
            t=60,
            b=20
        ),
        xaxis_title="",
        yaxis_title="Número de personas"
    )

    return fig


def mostrar_graficas():

    mostrar_titulo()

    st.header("📈 Gráficas interactivas")

    datos = obtener_datos()

    if datos.empty:
        st.info(
            "Todavía no hay datos suficientes para crear las gráficas. "
            "¡Registra la primera respuesta!"
        )
        return

    st.markdown("""
    <div class="sky-card">

    Las gráficas se actualizan automáticamente cada vez que
    se registra una nueva respuesta.

    </div>
    """, unsafe_allow_html=True)

    # --------------------------------------------------------
    # GRÁFICA 1
    # --------------------------------------------------------

    fig1 = crear_grafica(
        datos,
        "Juega Minecraft",
        "🎮 ¿Cuántas personas juegan Minecraft?"
    )

    st.plotly_chart(
        fig1,
        use_container_width=True
    )

    # --------------------------------------------------------
    # GRÁFICA 2
    # --------------------------------------------------------

    fig2 = crear_grafica(
        datos,
        "Estado emocional",
        "😊 Estado emocional después de jugar"
    )

    st.plotly_chart(
        fig2,
        use_container_width=True
    )

    # --------------------------------------------------------
    # GRÁFICA 3
    # --------------------------------------------------------

    fig3 = crear_grafica(
        datos,
        "Frecuencia",
        "🕐 Frecuencia de juego"
    )

    st.plotly_chart(
        fig3,
        use_container_width=True
    )

    # --------------------------------------------------------
    # GRÁFICA 4
    # --------------------------------------------------------

    fig4 = crear_grafica(
        datos,
        "Ayuda a relajarse",
        "😌 ¿Minecraft ayuda a relajarse?"
    )

    st.plotly_chart(
        fig4,
        use_container_width=True
    )

    # --------------------------------------------------------
    # GRÁFICA 5
    # --------------------------------------------------------

    fig5 = crear_grafica(
        datos,
        "Mejora el estado de ánimo",
        "💚 Minecraft y estado de ánimo"
    )

    st.plotly_chart(
        fig5,
        use_container_width=True
    )


def mostrar_resultados():

    mostrar_titulo()

    st.header("💚 Resultados")

    datos = obtener_datos()

    if datos.empty:
        st.info(
            "Todavía no se puede obtener una conclusión. "
            "Registra algunas respuestas primero."
        )
        return

    total = len(datos)

    juegan = int(
        (datos["Juega Minecraft"] == "Sí").sum()
    )

    porcentaje_juegan = porcentaje(
        juegan,
        total
    )

    jugadores = datos[
        datos["Juega Minecraft"] == "Sí"
    ]

    if len(jugadores) > 0:

        felices_jugadores = int(
            jugadores["Estado emocional"].isin(
                ["😀 Muy feliz", "😄 Feliz"]
            ).sum()
        )

        porcentaje_felices = porcentaje(
            felices_jugadores,
            len(jugadores)
        )

        relajacion_jugadores = int(
            jugadores["Ayuda a relajarse"].isin(
                ["Mucho", "Bastante"]
            ).sum()
        )

        porcentaje_relajacion = porcentaje(
            relajacion_jugadores,
            len(jugadores)
        )

    else:

        felices_jugadores = 0
        porcentaje_felices = 0
        porcentaje_relajacion = 0

    st.markdown(
        f"""
        <div class="grass-card">

        <h2>🔎 ¿Qué muestran los datos?</h2>

        <p>
        Según las respuestas registradas, el
        <strong>{porcentaje_juegan}%</strong> de los participantes
        indicó que juega Minecraft.
        </p>

        </div>
        """,
        unsafe_allow_html=True
    )

    if len(jugadores) > 0:

        st.markdown(
            f"""
            <div class="block-card">

            <h3>😊 Experiencia emocional</h3>

            <p>
            Entre las personas que indicaron jugar Minecraft,
            el <strong>{porcentaje_felices}%</strong> reportó sentirse
            feliz o muy feliz después de jugar.
            </p>

            <p>
            Además, el <strong>{porcentaje_relajacion}%</strong>
            de los jugadores indicó que Minecraft le ayuda
            mucho o bastante a relajarse.
            </p>

            </div>
            """,
            unsafe_allow_html=True
        )

        st.markdown("""
        <div class="sky-card">

        <h3>💡 Conclusión general</h3>

        <p>
        Según los datos de esta encuesta, se observa una posible
        relación entre la experiencia de juego de Minecraft y
        algunas percepciones emocionales reportadas por los
        participantes.
        </p>

        <p>
        Sin embargo, estos resultados corresponden únicamente
        a las personas encuestadas y no permiten afirmar que
        Minecraft cause directamente determinados efectos
        sobre la salud mental o emocional.
        </p>

        </div>
        """, unsafe_allow_html=True)

    else:

        st.warning(
            "Ninguno de los participantes registrados indicó jugar Minecraft, "
            "por lo que no es posible analizar las respuestas emocionales "
            "específicas de los jugadores."
        )

    st.markdown('<div class="pixel-line"></div>', unsafe_allow_html=True)

    st.caption(
        "⚠️ Importante: estos resultados son descriptivos y "
        "corresponden exclusivamente a esta encuesta."
    )


def mostrar_informacion():

    mostrar_titulo()

    st.header("ℹ️ Información")

    st.markdown("""
    <div class="block-card">

    <h2>🎯 Objetivo del proyecto</h2>

    <p>
    Esta aplicación busca conocer, mediante una encuesta,
    cómo las personas perciben emocionalmente su experiencia
    al jugar Minecraft.
    </p>

    <p>
    El proyecto permite recopilar respuestas, organizarlas
    y representarlas mediante estadísticas y gráficas.
    </p>

    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="sky-card">

    <h2>📚 ¿Cómo interpretar los resultados?</h2>

    <p>
    Los resultados dependen de las personas que participaron
    en la encuesta.
    </p>

    <p>
    Por esta razón, los datos obtenidos no representan
    necesariamente a todos los jugadores de Minecraft.
    </p>

    <p>
    Además, una encuesta de este tipo permite observar
    percepciones y tendencias dentro del grupo estudiado,
    pero no demuestra por sí sola una relación científica
    de causa y efecto.
    </p>

    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="grass-card">

    <h2>💾 Almacenamiento</h2>

    <p>
    Esta versión utiliza <strong>st.session_state</strong>
    junto con un DataFrame de Pandas para conservar las
    respuestas durante la sesión actual.
    </p>

    <p>
    Para un proyecto futuro que necesite guardar los datos
    permanentemente y compartirlos entre usuarios,
    se podría conectar Firebase, Supabase o una base
    de datos SQL.
    </p>

    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="block-card">

    <h2>🛡️ Sobre los datos</h2>

    <p>
    Esta aplicación escolar no utiliza APIs externas
    ni recopila información automáticamente.
    Las respuestas se registran únicamente cuando
    el participante presiona el botón
    <strong>GUARDAR RESPUESTA</strong>.
    </p>

    </div>
    """, unsafe_allow_html=True)


def mostrar_administracion():

    st.header("🧹 Administración")

    datos = obtener_datos()

    total = len(datos)

    st.markdown(
        f"""
        <div class="stone-card">

        <h3>📋 Datos actuales</h3>

        <p>
        Actualmente existen <strong>{total}</strong>
        respuestas en esta sesión.
        </p>

        </div>
        """,
        unsafe_allow_html=True
    )

    # --------------------------------------------------------
    # DESCARGAR CSV
    # --------------------------------------------------------

    if not datos.empty:

        csv = datos.to_csv(
            index=False,
            encoding="utf-8-sig"
        )

        st.download_button(
            label="📥 Descargar datos",
            data=csv,
            file_name="minecraft_emociones.csv",
            mime="text/csv",
            use_container_width=True
        )

    else:

        st.info(
            "No hay datos para descargar todavía."
        )

    st.markdown("<br>", unsafe_allow_html=True)

    # --------------------------------------------------------
    # BORRAR DATOS
    # --------------------------------------------------------

    st.markdown("""
    <div class="stone-card">

    <h3>🗑️ Limpiar datos</h3>

    <p>
    Esta acción eliminará todas las respuestas almacenadas
    durante esta sesión.
    </p>

    </div>
    """, unsafe_allow_html=True)

    confirmar = st.checkbox(
        "⚠️ Confirmo que quiero eliminar todos los datos.",
        key="confirmar_borrado"
    )

    if st.button(
        "🗑️ LIMPIAR DATOS",
        use_container_width=True
    ):

        if not confirmar:

            st.warning(
                "⚠️ Debes confirmar la eliminación antes de continuar."
            )

        else:

            st.session_state.respuestas = pd.DataFrame(
                columns=COLUMNAS
            )

            st.session_state.confirmar_borrado = False

            st.success(
                "✅ Los datos de esta sesión fueron eliminados."
            )

            st.rerun()


# ============================================================
# SIDEBAR
# ============================================================

with st.sidebar:

    st.markdown("""
    <div style="
        text-align:center;
        padding:10px;
        font-size:3rem;
    ">
        ⛏️
    </div>
    """, unsafe_allow_html=True)

    st.markdown(
        """
        <h2 style="text-align:center;">
            Minecraft<br>& Emociones
        </h2>
        """,
        unsafe_allow_html=True
    )

    st.markdown("---")

    pagina = st.radio(
        "🧭 Menú",
        [
            "🏠 Inicio",
            "📝 Encuesta",
            "📊 Estadísticas",
            "📈 Gráficas",
            "💚 Resultados",
            "ℹ️ Información"
        ]
    )

    st.markdown("---")

    mostrar_contador()

    st.markdown("---")

    st.caption(
        "🌱 Proyecto escolar\n\n"
        "⛏️ Explora • 📊 Analiza • 💚 Descubre"
    )


# ============================================================
# NAVEGACIÓN PRINCIPAL
# ============================================================

if pagina == "🏠 Inicio":

    mostrar_inicio()

elif pagina == "📝 Encuesta":

    mostrar_encuesta()

elif pagina == "📊 Estadísticas":

    mostrar_estadisticas()

elif pagina == "📈 Gráficas":

    mostrar_graficas()

elif pagina == "💚 Resultados":

    mostrar_resultados()

elif pagina == "ℹ️ Información":

    mostrar_informacion()


# ============================================================
# ADMINISTRACIÓN AL FINAL DE LA BARRA LATERAL
# ============================================================

with st.sidebar:

    st.markdown("---")

    with st.expander("🧹 Administración"):

        mostrar_administracion()