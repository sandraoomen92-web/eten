import streamlit as st
import random


# -----------------------------------------------------------------------------
# KEUZES
# -----------------------------------------------------------------------------

AVG_OPTIES = [
    "AVG - Bloemkool",
    "AVG - Broccoli",
    "AVG - Boontjes",
    "AVG - Witte Bonen/Wortelen"
]

OVERIG_OPTIES = [
    "Rijst",
    "Wraps",
    "Pita"
]


# -----------------------------------------------------------------------------
# MENU MAKEN
# -----------------------------------------------------------------------------

def maak_menu():

    menu = {}

    # Houd bij welke keuzes al gebruikt zijn
    gebruikte_avg = []
    gebruikte_overig = []

    # Dag 4:
    # Precies 2x AVG met sla, 1x Friet en 1x Pizza.
    dag4_opties = [
        "AVG met sla",
        "AVG met sla",
        "Friet",
        "Pizza"
    ]

    # Hussel de volgorde van dag 4
    random.shuffle(dag4_opties)


    # -------------------------------------------------------------------------
    # 4 WEKEN MAKEN
    # -------------------------------------------------------------------------

    for week_nummer in range(1, 5):

        week = {}


        # ---------------------------------------------------------------------
        # DAG 1 - ALTIJD PASTA
        # ---------------------------------------------------------------------

        week["Dag 1"] = "Pasta"


        # ---------------------------------------------------------------------
        # DAG 2 - AVG
        # ---------------------------------------------------------------------

        beschikbare_avg = [
            optie for optie in AVG_OPTIES
            if optie not in gebruikte_avg
        ]

        # Als alle 4 opties gebruikt zijn, beginnen we opnieuw
        if not beschikbare_avg:
            gebruikte_avg = []
            beschikbare_avg = AVG_OPTIES.copy()

        gekozen_avg = random.choice(beschikbare_avg)
        gebruikte_avg.append(gekozen_avg)

        week["Dag 2"] = gekozen_avg


        # ---------------------------------------------------------------------
        # DAG 3 - OVERIG
        # ---------------------------------------------------------------------

        beschikbare_overig = [
            optie for optie in OVERIG_OPTIES
            if optie not in gebruikte_overig
        ]

        # Als alle opties gebruikt zijn, beginnen we opnieuw
        if not beschikbare_overig:
            gebruikte_overig = []
            beschikbare_overig = OVERIG_OPTIES.copy()

        gekozen_overig = random.choice(beschikbare_overig)
        gebruikte_overig.append(gekozen_overig)

        week["Dag 3"] = gekozen_overig


        # ---------------------------------------------------------------------
        # DAG 4
        # ---------------------------------------------------------------------

        week["Dag 4"] = dag4_opties[week_nummer - 1]


        # Week toevoegen aan het menu
        menu[f"Week {week_nummer}"] = week


    return menu


# -----------------------------------------------------------------------------
# STREAMLIT INTERFACE
# -----------------------------------------------------------------------------

st.set_page_config(
    page_title="Wat Eten We Deze Week?",
    page_icon="🍲",
    layout="centered"
)

st.title("🍲 Wat Eten We Deze Week?")

st.write(
    "Genereer een gevarieerd menu voor 4 weken."
)

st.divider()


# -----------------------------------------------------------------------------
# KNOP
# -----------------------------------------------------------------------------

if st.button(
    "🎲 Genereer 4 weken menu",
    type="primary",
    use_container_width=True
):

    menu = maak_menu()

    # Menu bewaren
    st.session_state["menu"] = menu


# -----------------------------------------------------------------------------
# MENU WEERGEVEN
# -----------------------------------------------------------------------------

if "menu" in st.session_state:

    menu = st.session_state["menu"]

    for week_naam, dagen in menu.items():

        st.subheader(f"📅 {week_naam}")

        for dag_naam, gerecht in dagen.items():

            st.markdown(f"**{dag_naam}**")
            st.success(f"🍽️ {gerecht}")

        st.divider()

else:

    st.info(
        "👆 Klik op de knop om jouw menu voor 4 weken te genereren."
    )
