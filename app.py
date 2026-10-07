import streamlit as st



# ============================================================

# CONFIGURACIÓN

# ============================================================



st.set_page_config(

page_title="Carmen Pastelería · Boda L&D",

page_icon="🍰",

layout="wide",

initial_sidebar_state="expanded",

)



# ============================================================

# PALETA ORIGINAL

# ============================================================



BG = "#f5f0ea"

SURFACE = "#fffdfb"

SOFT = "#f1e9e1"

ESPRESSO = "#3b2f2f"

COCOA = "#795b48"

CARAMEL = "#c3a58c"

LINE = "#e5d9ce"

GREEN = "#667568"

GREEN_SOFT = "#e9eee9"



# ============================================================

# CSS

# ============================================================



st.markdown(

f"""

<style>



/* ========================================================

BASE

======================================================== */



html, body, [data-testid="stAppViewContainer"] {{

background: {BG} !important;

}}



.stApp {{

background: {BG} !important;

}}



[data-testid="stHeader"] {{

background: transparent !important;

}}



#MainMenu,

footer {{

visibility: hidden;

}}



.main .block-container {{

max-width: 1180px;

padding: 42px 45px 70px;

}}



/* ========================================================

TIPOGRAFÍA

======================================================== */



h1, h2, h3, h4 {{

color: {ESPRESSO} !important;

font-family: Georgia, "Times New Roman", serif !important;

font-weight: 400 !important;

}}



p, label {{

color: {ESPRESSO};

}}



/* ========================================================

ENCABEZADO

======================================================== */



.brand {{

text-align: center;

font-family: Georgia, "Times New Roman", serif;

font-size: 40px;

line-height: 1.1;

color: {ESPRESSO};

letter-spacing: -0.7px;

margin-top: 5px;

}}



.subtitle {{

text-align: center;

color: {COCOA};

font-size: 10px;

letter-spacing: 3px;

text-transform: uppercase;

margin-top: 8px;

margin-bottom: 38px;

}}



/* Espacio reservado para el logo futuro */



.logo-placeholder {{

text-align: center;

height: 0;

overflow: hidden;

}}



/* ========================================================

TARJETA PEDIDO

======================================================== */



.order-card {{

background: {SURFACE};

border: 1px solid {LINE};

border-radius: 18px;

padding: 27px 30px;

margin-bottom: 15px;

box-shadow: 0 8px 25px rgba(59,47,47,.035);

}}



.eyebrow {{

color: {COCOA};

font-size: 10px;

letter-spacing: 2px;

text-transform: uppercase;

margin-bottom: 7px;

}}



.order-title {{

font-family: Georgia, "Times New Roman", serif;

color: {ESPRESSO};

font-size: 31px;

line-height: 1.15;

margin-bottom: 13px;

}}



.status {{

display: inline-block;

color: {COCOA};

background: {SOFT};

border: 1px solid {LINE};

border-radius: 30px;

padding: 6px 13px;

font-size: 10px;

}}



/* ========================================================

INFORMACIÓN DEL PEDIDO

======================================================== */



.info-card {{

background: {SOFT};

border: 1px solid {LINE};

border-radius: 13px;

padding: 15px 17px;

min-height: 67px;

}}



.info-label {{

color: {COCOA};

font-size: 9px;

text-transform: uppercase;

letter-spacing: 1.4px;

margin-bottom: 5px;

}}



.info-value {{

color: {ESPRESSO};

font-size: 13px;

}}



/* ========================================================

ETAPAS

======================================================== */



.stages {{

position: relative;

display: flex;

justify-content: space-between;

margin: 28px 8px 38px;

}}



.stages::before {{

content: "";

position: absolute;

left: 5%;

right: 5%;

top: 5px;

height: 1px;

background: {LINE};

z-index: 0;

}}



.stage {{

position: relative;

z-index: 1;

text-align: center;

background: {BG};

padding: 0 8px;

}}



.stage-dot {{

width: 11px;

height: 11px;

border-radius: 50%;

background: {CARAMEL};

margin: 0 auto 8px;

border: 3px solid {BG};

box-shadow: 0 0 0 1px {CARAMEL};

}}



.stage-label {{

color: {COCOA};

font-size: 8px;

letter-spacing: 1.3px;

text-transform: uppercase;

white-space: nowrap;

}}



/* ========================================================

SIDEBAR

======================================================== */



[data-testid="stSidebar"] {{

background: {SOFT} !important;

border-right: 1px solid {LINE};

}}



[data-testid="stSidebar"] > div:first-child {{

padding: 30px 18px;

}}



[data-testid="stSidebar"] h1,

[data-testid="stSidebar"] h2,

[data-testid="stSidebar"] h3 {{

color: {ESPRESSO} !important;

font-family: Georgia, "Times New Roman", serif !important;

}}



.side-heading {{

font-family: Georgia, "Times New Roman", serif;

color: {ESPRESSO};

font-size: 24px;

margin-bottom: 4px;

}}



.side-subheading {{

color: {COCOA};

font-size: 10px;

letter-spacing: 1px;

margin-bottom: 25px;

}}



.side-section {{

background: {SURFACE};

border: 1px solid {LINE};

border-radius: 14px;

padding: 13px 14px 11px;

margin-bottom: 17px;

}}



.side-section-title {{

font-family: Georgia, "Times New Roman", serif;

color: {ESPRESSO};

font-size: 17px;

margin-bottom: 9px;

}}



/* ========================================================

CHECKBOXES

======================================================== */



[data-testid="stCheckbox"] {{

padding-top: 1px;

padding-bottom: 1px;

}}



[data-testid="stCheckbox"] label {{

font-size: 12px !important;

}}



[data-testid="stCheckbox"] label p {{

color: {ESPRESSO} !important;

font-size: 12px !important;

}}



/* ========================================================

TÍTULOS DE SECCIÓN

======================================================== */



.section-kicker {{

color: {COCOA};

font-size: 9px;

letter-spacing: 2px;

text-transform: uppercase;

margin-bottom: 3px;

}}



.section-title {{

color: {ESPRESSO};

font-family: Georgia, "Times New Roman", serif;

font-size: 28px;

margin-bottom: 18px;

}}



/* ========================================================

TARJETAS DE DÍAS

======================================================== */



.day-card-top {{

background: {SURFACE};

border: 1px solid {LINE};

border-bottom: none;

border-radius: 17px 17px 0 0;

padding: 19px 20px 5px;

margin-top: 4px;

}}



.day-card-bottom {{

background: {SURFACE};

border: 1px solid {LINE};

border-top: none;

border-radius: 0 0 17px 17px;

padding: 0 20px 14px;

margin-bottom: 18px;

}}



.day-label {{

color: {CARAMEL};

font-size: 9px;

letter-spacing: 2px;

text-transform: uppercase;

}}



.day-title {{

color: {ESPRESSO};

font-family: Georgia, "Times New Roman", serif;

font-size: 20px;

margin-top: 4px;

}}



/* ========================================================

DIVISORES

======================================================== */



hr {{

border: none !important;

border-top: 1px solid {LINE} !important;

margin: 30px 0 !important;

}}



/* ========================================================

PROGRESO

======================================================== */



.progress-card {{

background: {SURFACE};

border: 1px solid {LINE};

border-radius: 17px;

padding: 21px 24px 17px;

margin-top: 3px;

}}



.progress-label {{

color: {COCOA};

font-size: 9px;

text-transform: uppercase;

letter-spacing: 1.7px;

margin-bottom: 5px;

}}



.progress-number {{

color: {ESPRESSO};

font-family: Georgia, "Times New Roman", serif;

font-size: 27px;

}}



[data-testid="stProgress"] {{

margin-top: -8px;

margin-bottom: 12px;

}}



[data-testid="stProgress"] > div {{

background: {SOFT} !important;

border-radius: 20px !important;

height: 7px !important;

}}



[data-testid="stProgress"] > div > div {{

background: {GREEN} !important;

border-radius: 20px !important;

}}



/* ========================================================

ALERTA FINAL

======================================================== */



.stAlert {{

background: {GREEN_SOFT} !important;

border: 1px solid #d7ded7 !important;

border-radius: 13px !important;

color: {GREEN} !important;

}}



/* ========================================================

RESPONSIVE

======================================================== */



@media (max-width: 800px) {{



.main .block-container {{

padding: 25px 18px 50px;

}}



.brand {{

font-size: 32px;

}}



.subtitle {{

font-size: 8px;

letter-spacing: 2px;

}}



.order-title {{

font-size: 26px;

}}



.stages {{

overflow-x: auto;

justify-content: flex-start;

gap: 20px;

padding-bottom: 5px;

}}



.stage {{

min-width: 85px;

}}



.stage-label {{

font-size: 7px;

}}

}}



</style>

""",

unsafe_allow_html=True,

)



# ============================================================

# ENCABEZADO

# ============================================================



st.markdown(

'<div class="brand">Carmen Pastelería</div>',

unsafe_allow_html=True

)



st.markdown(

'<div class="subtitle">Producción · Organización · Detalles</div>',

unsafe_allow_html=True

)



# ============================================================

# PEDIDO

# ============================================================



st.markdown(

"""

<div class="order-card">

<div class="eyebrow">Pedido de esta semana</div>

<div class="order-title">Boda L&D</div>

<span class="status">En planificación</span>

</div>

""",

unsafe_allow_html=True

)



col1, col2, col3 = st.columns(3)



with col1:
   st.markdown(
       """
       <div class="info-card">
           <div class="info-label">Evento</div>
           <div class="info-value">Boda</div>
       </div>
       """,
       unsafe_allow_html=True
   )

with col2:
    st.markdown(
        """
    <div class="info-card">
        <div class="info-label">Producción</div>
        <div class="info-value">Lunes → Sábado</div>
    </div>
    """,
    unsafe_allow_html=True
    )

with col3:
    st.markdown(
        """
    <div class="info-card">
        <div class="info-label">Entrega</div>
        <div class="info-value">Sábado</div>
    </div>
    """,
    unsafe_allow_html=True
    )

# ============================================================

# ETAPAS

# ============================================================



st.markdown(

"""

<div class="stages">



<div class="stage">

<div class="stage-dot"></div>

<div class="stage-label">Planificación</div>

</div>



<div class="stage">

<div class="stage-dot"></div>

<div class="stage-label">Producción</div>

</div>



<div class="stage">

<div class="stage-dot"></div>

<div class="stage-label">Terminaciones</div>

</div>



<div class="stage">

<div class="stage-dot"></div>

<div class="stage-label">Armado</div>

</div>



<div class="stage">

<div class="stage-dot"></div>

<div class="stage-label">Listo</div>

</div>



</div>

""",

unsafe_allow_html=True

)

# ============================================================
# SIDEBAR
# ============================================================

with st.sidebar:

    st.markdown(
        '<div class="side-heading">Compras</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="side-subheading">Ingredientes y materiales</div>',
        unsafe_allow_html=True
    )

    # -------------------------
    # STOCK
    # -------------------------
    with st.container(border=True):
        st.markdown("**Ya tengo**")
        
        ya_tengo = [
            "Dulce de leche",
            "Chocolate semiamargo",
            "Cacao",
            "Queso crema",
            "Chocolinas",
            "Bases de torta",
            "Bases rectangulares petit",
            "Caja rectangular",
            "Harina leudante / 000",
            "Azúcar",
            "Toppers",
            "Huevos",
            "Manteca",
            "Duraznos en lata",
        ]

        for item in ya_tengo:
            st.checkbox(
                item,
                value=True,
                disabled=True,
                key=f"yt_{item}"
            )

    st.markdown("")

    # -------------------------
    # FALTANTES
    # -------------------------
    with st.container(border=True):
        st.markdown("**Falta comprar**")
        
        falta_comprar = [
            "Dulce de batata",
            "Crema de leche",
            "Frutos rojos",
            "Queso cremoso",
            "Jamón crudo",
            "Salame",
            "Queso en barra",
            "Flores",
            "Limón",
            "Naranjas",
        ]

        for item in falta_comprar:
            st.checkbox(
                item,
                key=f"fc_{item}"
            )

# ============================================================

# PLANIFICACIÓN

# ============================================================



st.markdown(

'<div class="section-kicker">Esta semana</div>',

unsafe_allow_html=True

)



st.markdown(

'<div class="section-title">Planificación</div>',

unsafe_allow_html=True

)



dias_tareas = {

"Lunes": {

"tipo": "Organizar",

"tareas": [

"Revisar pedido de la boda",

"Controlar stock",

"Hacer lista de compras",

"Comprar ingredientes faltantes",

"Organizar ingredientes y materiales",

"Dejar preparado el packaging",

],

},



"Martes": {

"tipo": "Preparar",

"tareas": [

"Armar cajas",

"Preparar packaging",

"Preparar la chocotorta",

"Llevar la chocotorta al freezer",

"Organizar materiales para producción",

],

},



"Miércoles": {

"tipo": "Hornear",

"tareas": [

"Hornear bizcochos",

"Hornear tarteletitas",

"Preparar bases",

"Organizar preparaciones horneadas",

],

},



"Jueves": {

"tipo": "Tortas",

"tareas": [

"Preparar rellenos de torta",

"Preparar almíbar",

"Cortar y rellenar tortas",

"Armar las tortas",

"Llevar a frío",

"Preparar rellenos de petit fours",

],

},



"Viernes": {

"tipo": "Terminar",

"tareas": [

"Armar brownies",

"Decorar petit fours",

"Preparar mesa dulce",

"Armar la parte salada",

"Organizar todo lo terminado",

],

},



"Sábado": {

"tipo": "Listo",

"tareas": [

"Revisar todo el pedido",

"Envolver y proteger",

"Colocar todo en sus cajas",

"Control final",

"Fotografiar el pedido terminado",

],

},

}

# ============================================================
# TAREAS
# ============================================================

total_tasks = sum(
    len(data["tareas"])
    for data in dias_tareas.values()
)

completed_tasks = 0

col_left, col_right = st.columns(2)

for i, (dia, data) in enumerate(dias_tareas.items()):

    column = col_left if i % 2 == 0 else col_right

    with column:
        # Contenedor nativo con borde para cada día
        with st.container(border=True):
            st.caption(dia.upper())
            st.markdown(f"### {data['tipo']}")
            
            st.markdown("---")

            for tarea in data["tareas"]:
                if st.checkbox(
                    tarea,
                    key=f"task_{dia}_{tarea}"
                ):
                    completed_tasks += 1
        
# ============================================================

# PROGRESO

# ============================================================

progress_percentage = (
    int((completed_tasks / total_tasks) * 100)
    if total_tasks > 0
    else 0
)

st.markdown(
    f"""
    <div class="progress-card">
        <div class="progress-label">
            Progreso general de producción
        </div>
        <div class="progress-number">
             {progress_percentage}%
        </div>
    </div>
    """,
    unsafe_allow_html=True
)

st.progress(progress_percentage / 100)

# ============================================================

# FINAL

# ============================================================

if progress_percentage == 100:
    
    st.success(
        "Pedido listo para entregar."
    )
    
    st.balloons() 