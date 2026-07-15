import streamlit as st
import pandas as pd
import io

# App configuratie
st.set_page_config(page_title="Liquicity Timetable Planner 2026", page_icon="🎵", layout="wide")

# Initialiseer lokale opslag voor geselecteerde artiesten
if "mijn_timetable" not in st.session_state:
    st.session_state.mijn_timetable = []

st.title("🪐 Liquicity Weekend 2026 Timetable Planner")
st.write("Vink je favoriete artiesten aan, sla ze op en download je persoonlijke `.ics`-agendabestand.")

# Complete Weekend Line-up Data
liquicity_acts = [
    # ==================== VRIJDAG ====================
    # === GALAXY STAGE ===
    {"Dag": "Vrijdag", "Datum": "2026-07-17", "Start": "11:00", "Eind": "12:30", "Artiest": "Midaze", "Stage": "Galaxy"},
    {"Dag": "Vrijdag", "Datum": "2026-07-17", "Start": "12:30", "Eind": "13:45", "Artiest": "Ketsune", "Stage": "Galaxy"},
    {"Dag": "Vrijdag", "Datum": "2026-07-17", "Start": "13:45", "Eind": "15:00", "Artiest": "Hiraeth", "Stage": "Galaxy"},
    {"Dag": "Vrijdag", "Datum": "2026-07-17", "Start": "15:00", "Eind": "16:00", "Artiest": "Yue (ft. Daxta)", "Stage": "Galaxy"},
    {"Dag": "Vrijdag", "Datum": "2026-07-17", "Start": "16:00", "Eind": "17:15", "Artiest": "Artino (ft. Wolf Pax)", "Stage": "Galaxy"},
    {"Dag": "Vrijdag", "Datum": "2026-07-17", "Start": "17:15", "Eind": "18:45", "Artiest": "Hybrid Minds (ft. Tempza)", "Stage": "Galaxy"},
    {"Dag": "Vrijdag", "Datum": "2026-07-17", "Start": "18:45", "Eind": "20:00", "Artiest": "Shy FX (ft. Rage MC)", "Stage": "Galaxy"},
    {"Dag": "Vrijdag", "Datum": "2026-07-17", "Start": "20:00", "Eind": "21:15", "Artiest": "Maduk (ft. Mota)", "Stage": "Galaxy"},
    {"Dag": "Vrijdag", "Datum": "2026-07-17", "Start": "21:15", "Eind": "22:30", "Artiest": "Kanine (ft. Rage MC)", "Stage": "Galaxy"},
    {"Dag": "Vrijdag", "Datum": "2026-07-17", "Start": "22:30", "Eind": "00:00", "Artiest": "Andy C (ft. Tonn Piper)", "Stage": "Galaxy"},

    # === SOLAR STAGE ===
    {"Dag": "Vrijdag", "Datum": "2026-07-17", "Start": "11:00", "Eind": "12:15", "Artiest": "Astronymous", "Stage": "Solar"},
    {"Dag": "Vrijdag", "Datum": "2026-07-17", "Start": "12:15", "Eind": "13:30", "Artiest": "48Past", "Stage": "Solar"},
    {"Dag": "Vrijdag", "Datum": "2026-07-17", "Start": "13:30", "Eind": "14:45", "Artiest": "Mod", "Stage": "Solar"},
    {"Dag": "Vrijdag", "Datum": "2026-07-17", "Start": "14:45", "Eind": "15:45", "Artiest": "Voxi", "Stage": "Solar"},
    {"Dag": "Vrijdag", "Datum": "2026-07-17", "Start": "15:45", "Eind": "16:45", "Artiest": "Bcee", "Stage": "Solar"},
    {"Dag": "Vrijdag", "Datum": "2026-07-17", "Start": "16:45", "Eind": "18:00", "Artiest": "Sless & Loboski (ft. Mota)", "Stage": "Solar"},
    {"Dag": "Vrijdag", "Datum": "2026-07-17", "Start": "18:00", "Eind": "19:00", "Artiest": "Natty Lou (ft. Wolf Pax)", "Stage": "Solar"},
    {"Dag": "Vrijdag", "Datum": "2026-07-17", "Start": "19:00", "Eind": "20:00", "Artiest": "Eskei83 (ft. Daxta)", "Stage": "Solar"},
    {"Dag": "Vrijdag", "Datum": "2026-07-17", "Start": "20:00", "Eind": "21:00", "Artiest": "Voicians (ft. Wolf Pax)", "Stage": "Solar"},
    {"Dag": "Vrijdag", "Datum": "2026-07-17", "Start": "21:00", "Eind": "22:00", "Artiest": "Tantrum Desire (ft. Fava)", "Stage": "Solar"},
    {"Dag": "Vrijdag", "Datum": "2026-07-17", "Start": "22:00", "Eind": "23:00", "Artiest": "Pirapus (ft. Fava)", "Stage": "Solar"},
    {"Dag": "Vrijdag", "Datum": "2026-07-17", "Start": "23:00", "Eind": "00:00", "Artiest": "Lexurus (ft. Mota)", "Stage": "Solar"},

    # === LUNAR STAGE ===
    {"Dag": "Vrijdag", "Datum": "2026-07-17", "Start": "11:00", "Eind": "13:00", "Artiest": "Botone", "Stage": "Lunar"},
    {"Dag": "Vrijdag", "Datum": "2026-07-17", "Start": "13:00", "Eind": "14:15", "Artiest": "Noppo", "Stage": "Lunar"},
    {"Dag": "Vrijdag", "Datum": "2026-07-17", "Start": "14:15", "Eind": "15:30", "Artiest": "Imo-Lu", "Stage": "Lunar"},
    {"Dag": "Vrijdag", "Datum": "2026-07-17", "Start": "15:30", "Eind": "16:45", "Artiest": "Edlan", "Stage": "Lunar"},
    {"Dag": "Vrijdag", "Datum": "2026-07-17", "Start": "16:45", "Eind": "18:15", "Artiest": "Monrroe (Liquid Set)", "Stage": "Lunar"},
    {"Dag": "Vrijdag", "Datum": "2026-07-17", "Start": "18:15", "Eind": "19:30", "Artiest": "4AM Kru", "Stage": "Lunar"},
    {"Dag": "Vrijdag", "Datum": "2026-07-17", "Start": "19:30", "Eind": "21:00", "Artiest": "Pola & Bryson", "Stage": "Lunar"},
    {"Dag": "Vrijdag", "Datum": "2026-07-17", "Start": "21:00", "Eind": "22:30", "Artiest": "S.P.Y", "Stage": "Lunar"},
    {"Dag": "Vrijdag", "Datum": "2026-07-17", "Start": "22:30", "Eind": "00:00", "Artiest": "Imanu", "Stage": "Lunar"},

    # === NEBULA STAGE ===
    {"Dag": "Vrijdag", "Datum": "2026-07-17", "Start": "11:00", "Eind": "13:00", "Artiest": "Kubalo", "Stage": "Nebula"},
    {"Dag": "Vrijdag", "Datum": "2026-07-17", "Start": "13:00", "Eind": "14:00", "Artiest": "As:She", "Stage": "Nebula"},
    {"Dag": "Vrijdag", "Datum": "2026-07-17", "Start": "14:00", "Eind": "15:00", "Artiest": "Drum 'n Babes", "Stage": "Nebula"},
    {"Dag": "Vrijdag", "Datum": "2026-07-17", "Start": "15:00", "Eind": "16:30", "Artiest": "Dnbstep Workshop", "Stage": "Nebula"},
    {"Dag": "Vrijdag", "Datum": "2026-07-17", "Start": "16:30", "Eind": "17:30", "Artiest": "Sebass", "Stage": "Nebula"},
    {"Dag": "Vrijdag", "Datum": "2026-07-17", "Start": "17:30", "Eind": "18:30", "Artiest": "Sub Flow & Top Tier", "Stage": "Nebula"},
    {"Dag": "Vrijdag", "Datum": "2026-07-17", "Start": "18:30", "Eind": "19:30", "Artiest": "Amber Jay", "Stage": "Nebula"},
    {"Dag": "Vrijdag", "Datum": "2026-07-17", "Start": "19:30", "Eind": "20:30", "Artiest": "Curious Mind", "Stage": "Nebula"},
    {"Dag": "Vrijdag", "Datum": "2026-07-17", "Start": "20:30", "Eind": "21:30", "Artiest": "Hot Cues", "Stage": "Nebula"},
    {"Dag": "Vrijdag", "Datum": "2026-07-17", "Start": "21:30", "Eind": "22:30", "Artiest": "Something Else with Fox & Yue", "Stage": "Nebula"},
    {"Dag": "Vrijdag", "Datum": "2026-07-17", "Start": "22:30", "Eind": "23:30", "Artiest": "Blackout Baddies", "Stage": "Nebula"},
    # ==================== ZATERDAG ====================
    # === GALAXY STAGE ===
    {"Dag": "Zaterdag", "Datum": "2026-07-18", "Start": "11:00", "Eind": "12:30", "Artiest": "Midaze", "Stage": "Galaxy"},
    {"Dag": "Zaterdag", "Datum": "2026-07-18", "Start": "12:30", "Eind": "14:00", "Artiest": "Operator21", "Stage": "Galaxy"},
    {"Dag": "Zaterdag", "Datum": "2026-07-18", "Start": "14:00", "Eind": "15:15", "Artiest": "Matt View & Hannelotta", "Stage": "Galaxy"},
    {"Dag": "Zaterdag", "Datum": "2026-07-18", "Start": "15:15", "Eind": "16:30", "Artiest": "Dossa (ft. Daxta)", "Stage": "Galaxy"},
    {"Dag": "Zaterdag", "Datum": "2026-07-18", "Start": "16:30", "Eind": "17:45", "Artiest": "Jon Void (ft. Wolf Pax)", "Stage": "Galaxy"},
    {"Dag": "Zaterdag", "Datum": "2026-07-18", "Start": "17:45", "Eind": "19:00", "Artiest": "Fox Stevenson Live", "Stage": "Galaxy"},
    {"Dag": "Zaterdag", "Datum": "2026-07-18", "Start": "19:00", "Eind": "20:15", "Artiest": "Sigma (ft. Fava)", "Stage": "Galaxy"},
    {"Dag": "Zaterdag", "Datum": "2026-07-18", "Start": "20:15", "Eind": "21:30", "Artiest": "Æon:Mode (ft. Wolf Pax)", "Stage": "Galaxy"},
    {"Dag": "Zaterdag", "Datum": "2026-07-18", "Start": "21:30", "Eind": "22:45", "Artiest": "Delta Heavy (ft. Daxta)", "Stage": "Galaxy"},
    {"Dag": "Zaterdag", "Datum": "2026-07-18", "Start": "22:45", "Eind": "00:00", "Artiest": "Andromedik", "Stage": "Galaxy"},

    # === SOLAR STAGE ===
    {"Dag": "Zaterdag", "Datum": "2026-07-18", "Start": "11:00", "Eind": "12:15", "Artiest": "Astronymous", "Stage": "Solar"},
    {"Dag": "Zaterdag", "Datum": "2026-07-18", "Start": "12:15", "Eind": "13:15", "Artiest": "Zazu", "Stage": "Solar"},
    {"Dag": "Zaterdag", "Datum": "2026-07-18", "Start": "13:15", "Eind": "14:15", "Artiest": "L.A.O.S", "Stage": "Solar"},
    {"Dag": "Zaterdag", "Datum": "2026-07-18", "Start": "14:15", "Eind": "15:15", "Artiest": "Rameses B", "Stage": "Solar"},
    {"Dag": "Zaterdag", "Datum": "2026-07-18", "Start": "15:15", "Eind": "16:15", "Artiest": "Boxplot (ft. Mota)", "Stage": "Solar"},
    {"Dag": "Zaterdag", "Datum": "2026-07-18", "Start": "16:15", "Eind": "17:15", "Artiest": "Cartoon", "Stage": "Solar"},
    {"Dag": "Zaterdag", "Datum": "2026-07-18", "Start": "17:15", "Eind": "18:30", "Artiest": "NCT & Dualistic (ft. Fava)", "Stage": "Solar"},
    {"Dag": "Zaterdag", "Datum": "2026-07-18", "Start": "18:30", "Eind": "19:30", "Artiest": "Matrix & Futurebound Live (ft. Mota)", "Stage": "Solar"},
    {"Dag": "Zaterdag", "Datum": "2026-07-18", "Start": "19:30", "Eind": "20:30", "Artiest": "Koven", "Stage": "Solar"},
    {"Dag": "Zaterdag", "Datum": "2026-07-18", "Start": "20:30", "Eind": "21:45", "Artiest": "Maduk Anniversary Set (ft. Mota)", "Stage": "Solar"},
    {"Dag": "Zaterdag", "Datum": "2026-07-18", "Start": "21:45", "Eind": "23:00", "Artiest": "T & Sugah", "Stage": "Solar"},
    {"Dag": "Zaterdag", "Datum": "2026-07-18", "Start": "23:00", "Eind": "00:00", "Artiest": "Feint (ft. Fava)", "Stage": "Solar"},

    # === LUNAR STAGE ===
    {"Dag": "Zaterdag", "Datum": "2026-07-18", "Start": "11:00", "Eind": "12:45", "Artiest": "Botone", "Stage": "Lunar"},
    {"Dag": "Zaterdag", "Datum": "2026-07-18", "Start": "12:45", "Eind": "14:00", "Artiest": "Miesfm", "Stage": "Lunar"},
    {"Dag": "Zaterdag", "Datum": "2026-07-18", "Start": "14:00", "Eind": "15:00", "Artiest": "Styke", "Stage": "Lunar"},
    {"Dag": "Zaterdag", "Datum": "2026-07-18", "Start": "15:00", "Eind": "16:15", "Artiest": "Glxy", "Stage": "Lunar"},
    {"Dag": "Zaterdag", "Datum": "2026-07-18", "Start": "16:15", "Eind": "17:30", "Artiest": "Telomic", "Stage": "Lunar"},
    {"Dag": "Zaterdag", "Datum": "2026-07-18", "Start": "17:30", "Eind": "19:00", "Artiest": "FD & Submorphics (Lenzman Dedication Set)", "Stage": "Lunar"},
    {"Dag": "Zaterdag", "Datum": "2026-07-18", "Start": "19:00", "Eind": "21:00", "Artiest": "Calibre", "Stage": "Lunar"},
    {"Dag": "Zaterdag", "Datum": "2026-07-18", "Start": "21:00", "Eind": "22:30", "Artiest": "Etherwood", "Stage": "Lunar"},
    {"Dag": "Zaterdag", "Datum": "2026-07-18", "Start": "22:30", "Eind": "00:00", "Artiest": "Technimatic", "Stage": "Lunar"},

    # === NEBULA STAGE ===
    {"Dag": "Zaterdag", "Datum": "2026-07-18", "Start": "11:00", "Eind": "12:00", "Artiest": "Kubalo", "Stage": "Nebula"},
    {"Dag": "Zaterdag", "Datum": "2026-07-18", "Start": "12:00", "Eind": "13:00", "Artiest": "Giant Musical Chairs", "Stage": "Nebula"},
    {"Dag": "Zaterdag", "Datum": "2026-07-18", "Start": "13:00", "Eind": "14:00", "Artiest": "Waves & Nebulaheights", "Stage": "Nebula"},
    {"Dag": "Zaterdag", "Datum": "2026-07-18", "Start": "14:00", "Eind": "15:00", "Artiest": "Enter The Rift", "Stage": "Nebula"},
    {"Dag": "Zaterdag", "Datum": "2026-07-18", "Start": "15:00", "Eind": "16:00", "Artiest": "Wet Socks Beach Party", "Stage": "Nebula"},
    {"Dag": "Zaterdag", "Datum": "2026-07-18", "Start": "16:00", "Eind": "17:00", "Artiest": "Next Horizon", "Stage": "Nebula"},
    {"Dag": "Zaterdag", "Datum": "2026-07-18", "Start": "17:00", "Eind": "18:00", "Artiest": "Fryett", "Stage": "Nebula"},
    {"Dag": "Zaterdag", "Datum": "2026-07-18", "Start": "18:00", "Eind": "19:00", "Artiest": "Fiber Family Takeover", "Stage": "Nebula"},
    {"Dag": "Zaterdag", "Datum": "2026-07-18", "Start": "19:00", "Eind": "20:00", "Artiest": "Time Travelomic 2.0", "Stage": "Nebula"},
    {"Dag": "Zaterdag", "Datum": "2026-07-18", "Start": "20:00", "Eind": "21:00", "Artiest": "Rex Hooligan", "Stage": "Nebula"},
    {"Dag": "Zaterdag", "Datum": "2026-07-18", "Start": "21:00", "Eind": "22:00", "Artiest": "Eetlaste Kaksnurk", "Stage": "Nebula"},
    {"Dag": "Zaterdag", "Datum": "2026-07-18", "Start": "22:00", "Eind": "23:30", "Artiest": "Thrasher", "Stage": "Nebula"},
    # ==================== ZONDAG ====================
    # === GALAXY STAGE ===
    {"Dag": "Zondag", "Datum": "2026-07-19", "Start": "11:00", "Eind": "12:30", "Artiest": "Midaze", "Stage": "Galaxy"},
    {"Dag": "Zondag", "Datum": "2026-07-19", "Start": "12:30", "Eind": "14:30", "Artiest": "Auris & Friends", "Stage": "Galaxy"},
    {"Dag": "Zondag", "Datum": "2026-07-19", "Start": "14:30", "Eind": "15:45", "Artiest": "Nymfo", "Stage": "Galaxy"},
    {"Dag": "Zondag", "Datum": "2026-07-19", "Start": "15:45", "Eind": "17:00", "Artiest": "Goddard (ft. Fava)", "Stage": "Galaxy"},
    {"Dag": "Zondag", "Datum": "2026-07-19", "Start": "17:00", "Eind": "18:00", "Artiest": "Catching Cairo", "Stage": "Galaxy"},
    {"Dag": "Zondag", "Datum": "2026-07-19", "Start": "18:00", "Eind": "19:00", "Artiest": "Aktive (ft. Fava)", "Stage": "Galaxy"},
    {"Dag": "Zondag", "Datum": "2026-07-19", "Start": "19:00", "Eind": "20:15", "Artiest": "Culture Shock", "Stage": "Galaxy"},
    {"Dag": "Zondag", "Datum": "2026-07-19", "Start": "20:15", "Eind": "21:30", "Artiest": "Wilkinson", "Stage": "Galaxy"},
    {"Dag": "Zondag", "Datum": "2026-07-19", "Start": "21:30", "Eind": "23:00", "Artiest": "Netsky", "Stage": "Galaxy"},

    # === SOLAR STAGE ===
    {"Dag": "Zondag", "Datum": "2026-07-19", "Start": "11:00", "Eind": "12:00", "Artiest": "Astronymous", "Stage": "Solar"},
    {"Dag": "Zondag", "Datum": "2026-07-19", "Start": "12:00", "Eind": "13:00", "Artiest": "Lirios", "Stage": "Solar"},
    {"Dag": "Zondag", "Datum": "2026-07-19", "Start": "13:00", "Eind": "14:30", "Artiest": "Flint & Figure", "Stage": "Solar"},
    {"Dag": "Zondag", "Datum": "2026-07-19", "Start": "14:30", "Eind": "15:45", "Artiest": "Aperio", "Stage": "Solar"},
    {"Dag": "Zondag", "Datum": "2026-07-19", "Start": "15:45", "Eind": "16:45", "Artiest": "Genetics (ft. Wolf Pax)", "Stage": "Solar"},
    {"Dag": "Zondag", "Datum": "2026-07-19", "Start": "16:45", "Eind": "18:00", "Artiest": "Ekko & Sidetrack (ft. Mota)", "Stage": "Solar"},
    {"Dag": "Zondag", "Datum": "2026-07-19", "Start": "18:00", "Eind": "19:15", "Artiest": "Disrupta (ft. Wolf Pax)", "Stage": "Solar"},
    {"Dag": "Zondag", "Datum": "2026-07-19", "Start": "19:15", "Eind": "20:30", "Artiest": "Subsonic (ft. Mota)", "Stage": "Solar"},
    {"Dag": "Zondag", "Datum": "2026-07-19", "Start": "20:30", "Eind": "21:45", "Artiest": "A.M.C (ft. Phantom)", "Stage": "Solar"},
    {"Dag": "Zondag", "Datum": "2026-07-19", "Start": "21:45", "Eind": "23:00", "Artiest": "Mandidextrous (ft. Mota)", "Stage": "Solar"},

    # === LUNAR STAGE ===
    {"Dag": "Zondag", "Datum": "2026-07-19", "Start": "11:00", "Eind": "12:45", "Artiest": "Botone", "Stage": "Lunar"},
    {"Dag": "Zondag", "Datum": "2026-07-19", "Start": "12:45", "Eind": "13:45", "Artiest": "Ipkiss", "Stage": "Lunar"},
    {"Dag": "Zondag", "Datum": "2026-07-19", "Start": "13:45", "Eind": "14:45", "Artiest": "Creek", "Stage": "Lunar"},
    {"Dag": "Zondag", "Datum": "2026-07-19", "Start": "14:45", "Eind": "16:00", "Artiest": "Alb", "Stage": "Lunar"},
    {"Dag": "Zondag", "Datum": "2026-07-19", "Start": "16:00", "Eind": "17:15", "Artiest": "Alibi", "Stage": "Lunar"},
    {"Dag": "Zondag", "Datum": "2026-07-19", "Start": "17:15", "Eind": "18:30", "Artiest": "Low:r", "Stage": "Lunar"},
    {"Dag": "Zondag", "Datum": "2026-07-19", "Start": "18:30", "Eind": "19:45", "Artiest": "Anaïs", "Stage": "Lunar"},
    {"Dag": "Zondag", "Datum": "2026-07-19", "Start": "19:45", "Eind": "21:00", "Artiest": "Skantia", "Stage": "Lunar"},
    {"Dag": "Zondag", "Datum": "2026-07-19", "Start": "21:00", "Eind": "22:00", "Artiest": "Basstripper", "Stage": "Lunar"},
    {"Dag": "Zondag", "Datum": "2026-07-19", "Start": "22:00", "Eind": "23:00", "Artiest": "Pythius", "Stage": "Lunar"},

    # === NEBULA STAGE ===
    {"Dag": "Zondag", "Datum": "2026-07-19", "Start": "11:00", "Eind": "13:00", "Artiest": "Kubalo", "Stage": "Nebula"},
    {"Dag": "Zondag", "Datum": "2026-07-19", "Start": "13:00", "Eind": "14:00", "Artiest": "Maud & Mika Morning Workout", "Stage": "Nebula"},
    {"Dag": "Zondag", "Datum": "2026-07-19", "Start": "14:00", "Eind": "15:00", "Artiest": "Dossa's Disco Drive", "Stage": "Nebula"},
    {"Dag": "Zondag", "Datum": "2026-07-19", "Start": "15:00", "Eind": "16:00", "Artiest": "Lasyen & Lennart Hoffmann", "Stage": "Nebula"},
    {"Dag": "Zondag", "Datum": "2026-07-19", "Start": "16:00", "Eind": "17:00", "Artiest": "Liquicity Office Party", "Stage": "Nebula"},
    {"Dag": "Zondag", "Datum": "2026-07-19", "Start": "17:00", "Eind": "18:00", "Artiest": "Prodace & Niek", "Stage": "Nebula"},
    {"Dag": "Zondag", "Datum": "2026-07-19", "Start": "18:00", "Eind": "19:00", "Artiest": "Reese Roelvink & Wobble Ockles", "Stage": "Nebula"},
    {"Dag": "Zondag", "Datum": "2026-07-19", "Start": "19:00", "Eind": "20:00", "Artiest": "Polygon", "Stage": "Nebula"},
    {"Dag": "Zondag", "Datum": "2026-07-19", "Start": "20:00", "Eind": "21:00", "Artiest": "Mxtr", "Stage": "Nebula"},
    {"Dag": "Zondag", "Datum": "2026-07-19", "Start": "21:00", "Eind": "22:00", "Artiest": "Rameses B Psytrance Power Hour", "Stage": "Nebula"},
]

df_acts = pd.DataFrame(liquicity_acts)

col1, col2 = st.columns(2)

with col1:
    st.subheader("Selecteer jouw Must-Sees")
    
    # === FILTER SECTIE (Nu BUITEN de form geplaatst voor instant resultaat) ===
    st.markdown("##### 🔍 Live Filters")
    f_col1, f_col2 = st.columns(2)
    
    with f_col1:
        filter_dag = st.multiselect(
            "Kies Dag(en):", 
            options=["Vrijdag", "Zaterdag", "Zondag"], 
            default=["Vrijdag", "Zaterdag", "Zondag"]
        )
        
    with f_col2:
        filter_stage = st.multiselect(
            "Kies Stage(s):", 
            options=["Galaxy", "Solar", "Lunar", "Nebula"], 
            default=["Galaxy", "Solar", "Lunar", "Nebula"]
        )
        
    st.write("---")
    
    # Het formulier bevat nu alleen nog de checkboxes en de opslaan-knop
    with st.form(key="form_timetable_local"):
        tijdelijke_vinkjes = {}
        
        # Loop door alle dagen
        for dag in ["Vrijdag", "Zaterdag", "Zondag"]:
            # Toon de dag alleen als deze is aangevinkt in de live filter
            if dag in filter_dag:
                # Filter de acts direct op basis van de gekozen stages
                dag_acts = df_acts[(df_acts["Dag"] == dag) & (df_acts["Stage"].isin(filter_stage))]
                
                if not dag_acts.empty:
                    st.markdown(f"### 📅 {dag}")
                    
                    for _, act in dag_acts.iterrows():
                        key = f"{act['Dag']} | {act['Artiest']} ({act['Start']}-{act['Eind']}) [{act['Stage']}]"
                        is_checked = key in st.session_state.mijn_timetable
                        
                        tijdelijke_vinkjes[key] = st.checkbox(
                            f"{act['Start']} - {act['Eind']} | **{act['Artiest']}** ({act['Stage']})", 
                            value=is_checked,
                            key=f"cb_{act['Dag']}_{act['Artiest'].replace(' ', '_')}_{act['Start'].replace(':', '')}"
                        )
            
        if st.form_submit_button("💾 Keuzes Opslaan", type="primary"):
            nieuwe_selectie = [k for k, v in tijdelijke_vinkjes.items() if v]
            
            # Behoud de selectie van artiesten die op dit moment verborgen zijn door actieve filters
            for oude_key in st.session_state.mijn_timetable:
                if oude_key not in tijdelijke_vinkjes:
                    nieuwe_selectie.append(oude_key)
                    
            st.session_state.mijn_timetable = nieuwe_selectie
            st.rerun()

with col2:
    st.subheader("Jouw Persoonlijke Planning")
    
    if not st.session_state.mijn_timetable:
        st.info("Je hebt nog geen artiesten geselecteerd. Vink je favorieten aan de linkerkant aan en druk op Opslaan.")
    else:
        st.success(f"Je hebt {len(st.session_state.mijn_timetable)} optredens geselecteerd!")
        
        geselecteerde_acts = []
        for act in liquicity_acts:
            match_key = f"{act['Dag']} | {act['Artiest']} ({act['Start']}-{act['Eind']}) [{act['Stage']}]"
            if match_key in st.session_state.mijn_timetable:
                geselecteerde_acts.append(act)
        
        df_selectie = pd.DataFrame(geselecteerde_acts)
        st.dataframe(df_selectie[["Dag", "Start", "Eind", "Artiest", "Stage"]], use_container_width=True, hide_index=True)
        
        # === VEILIGE ICS GENERATOR ===
        ics_content = "BEGIN:VCALENDAR\nVERSION:2.0\nPRODID:-//Liquicity Timetable Planner//NL\nCALSCALE:GREGORIAN\nMETHOD:PUBLISH\n"
        
        for act in geselecteerde_acts:
            date_clean = act["Datum"].replace("-", "")
            start_clean = act["Start"].replace(":", "") + "00"
            end_clean = act["Eind"].replace(":", "") + "00"
            
            end_date = date_clean
            if int(end_clean) <= int(start_clean):
                if date_clean == "20260717": end_date = "20260718"
                elif date_clean == "20260718": end_date = "20260719"
                elif date_clean == "20260719": end_date = "20260720"

            ics_content += "BEGIN:VEVENT\n"
            ics_content += f"SUMMARY:🚀 {act['Artiest']}\n"
            ics_content += f"LOCATION:🏟️ {act['Stage']}\n"
            ics_content += f"DESCRIPTION:Liquicity Weekend 2026 - live op de {act['Stage']} stage.\n"
            ics_content += f"DTSTART;TZID=Europe/Amsterdam:{date_clean}T{start_clean}\n"
            ics_content += f"DTEND;TZID=Europe/Amsterdam:{end_date}T{end_clean}\n"
            ics_content += "END:VEVENT\n"
            
        ics_content += "END:VCALENDAR"
        
        ics_bytes = io.BytesIO(ics_content.encode("utf-8"))
        st.download_button(
            label="📅 Download .ics Agenda", 
            data=ics_bytes, 
            file_name="liquicity_timetable.ics", 
            mime="text/calendar", 
            use_container_width=True
        )
