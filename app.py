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

# Complete Vrijdag Line-up op basis van de timetable afbeelding
liquicity_acts = [
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
]

    
    # ZATERDAG
    {"Dag": "Zaterdag", "Datum": "2026-07-18", "Start": "13:00", "Eind": "14:15", "Artiest": "Telomic", "Stage": "Galaxy"},
    {"Dag": "Zaterdag", "Datum": "2026-07-18", "Start": "14:15", "Eind": "15:30", "Artiest": "Monrroe", "Stage": "Galaxy"},
    {"Dag": "Zaterdag", "Datum": "2026-07-18", "Start": "15:30", "Eind": "16:45", "Artiest": "LSB", "Stage": "Galaxy"},
    {"Dag": "Zaterdag", "Datum": "2026-07-18", "Start": "16:45", "Eind": "18:00", "Artiest": "Etherwood", "Stage": "Galaxy"},
    {"Dag": "Zaterdag", "Datum": "2026-07-18", "Start": "18:00", "Eind": "19:15", "Artiest": "Fred V", "Stage": "Galaxy"},
    {"Dag": "Zaterdag", "Datum": "2026-07-18", "Start": "19:15", "Eind": "20:30", "Artiest": "Danny Byrd", "Stage": "Galaxy"},
    {"Dag": "Zaterdag", "Datum": "2026-07-18", "Start": "20:30", "Eind": "21:45", "Artiest": "Grafix", "Stage": "Galaxy"},
    {"Dag": "Zaterdag", "Datum": "2026-07-18", "Start": "21:45", "Eind": "23:00", "Artiest": "Camo & Krooked", "Stage": "Galaxy"},
    {"Dag": "Zaterdag", "Datum": "2026-07-18", "Start": "23:00", "Eind": "00:15", "Artiest": "Wilkinson", "Stage": "Galaxy"},
    {"Dag": "Zaterdag", "Datum": "2026-07-18", "Start": "00:15", "Eind": "01:30", "Artiest": "Matrix & Futurebound", "Stage": "Galaxy"},
    {"Dag": "Zaterdag", "Datum": "2026-07-18", "Start": "01:30", "Eind": "02:45", "Artiest": "ShockOne", "Stage": "Galaxy"},
    {"Dag": "Zaterdag", "Datum": "2026-07-18", "Start": "02:45", "Eind": "04:00", "Artiest": "Murdock", "Stage": "Galaxy"},

    # ZONDAG
    {"Dag": "Zondag", "Datum": "2026-07-19", "Start": "13:00", "Eind": "14:15", "Artiest": "Edlan", "Stage": "Galaxy"},
    {"Dag": "Zondag", "Datum": "2026-07-19", "Start": "14:15", "Eind": "15:30", "Artiest": "Changing Faces", "Stage": "Galaxy"},
    {"Dag": "Zondag", "Datum": "2026-07-19", "Start": "15:30", "Eind": "16:45", "Artiest": "Keeno", "Stage": "Galaxy"},
    {"Dag": "Zondag", "Datum": "2026-07-19", "Start": "16:45", "Eind": "18:00", "Artiest": "Whiney", "Stage": "Galaxy"},
    {"Dag": "Zondag", "Datum": "2026-07-19", "Start": "18:00", "Eind": "19:15", "Artiest": "Bcee", "Stage": "Galaxy"},
    {"Dag": "Zondag", "Datum": "2026-07-19", "Start": "19:15", "Eind": "20:30", "Artiest": "Nu:Tone", "Stage": "Galaxy"},
    {"Dag": "Zondag", "Datum": "2026-07-19", "Start": "20:30", "Eind": "21:45", "Artiest": "Logistics", "Stage": "Galaxy"},
    {"Dag": "Zondag", "Datum": "2026-07-19", "Start": "21:45", "Eind": "23:00", "Artiest": "Lenzman", "Stage": "Galaxy"},
    {"Dag": "Zondag", "Datum": "2026-07-19", "Start": "23:00", "Eind": "00:15", "Artiest": "Calibre", "Stage": "Galaxy"},
    {"Dag": "Zondag", "Datum": "2026-07-19", "Start": "00:15", "Eind": "01:30", "Artiest": "Spectrasoul", "Stage": "Galaxy"},
    {"Dag": "Zondag", "Datum": "2026-07-19", "Start": "01:30", "Eind": "02:45", "Artiest": "Alix Perez", "Stage": "Galaxy"},
    {"Dag": "Zondag", "Datum": "2026-07-19", "Start": "02:45", "Eind": "04:00", "Artiest": "DRS", "Stage": "Galaxy"},
]

df_acts = pd.DataFrame(liquicity_acts)

col1, col2 = st.columns(2)

with col1:
    st.subheader("Selecteer jouw Must-Sees")
    
    with st.form(key="form_timetable_local"):
        tijdelijke_vinkjes = {}
        
        for dag in ["Vrijdag", "Zaterdag", "Zondag"]:
            st.markdown(f"### 📅 {dag}")
            dag_acts = df_acts[df_acts["Dag"] == dag]
            
            for _, act in dag_acts.iterrows():
                key = f"{act['Artiest']} ({act['Start']}-{act['Eind']})"
                is_checked = key in st.session_state.mijn_timetable
                tijdelijke_vinkjes[key] = st.checkbox(f"{act['Start']} - {act['Eind']} | **{act['Artiest']}** ({act['Stage']})", value=is_checked)
            
        if st.form_submit_button("💾 Keuzes Opslaan", type="primary"):
            st.session_state.mijn_timetable = [k for k, v in tijdelijke_vinkjes.items() if v]
            st.rerun()

with col2:
    st.subheader("Jouw Persoonlijke Planning")
    
    if not st.session_state.mijn_timetable:
        st.info("Je hebt nog geen artiesten geselecteerd.")
    else:
        st.success(f"Je hebt {len(st.session_state.mijn_timetable)} optredens geselecteerd!")
        
        geselecteerde_acts = []
        for act in liquicity_acts:
            match_key = f"{act['Artiest']} ({act['Start']}-{act['Eind']})"
            if match_key in st.session_state.mijn_timetable:
                geselecteerde_acts.append(act)
        
        df_selectie = pd.DataFrame(geselecteerde_acts)
        st.dataframe(df_selectie[["Dag", "Start", "Eind", "Artiest", "Stage"]], use_container_width=True, hide_index=True)
        
        ics_content = "BEGIN:VCALENDAR\nVERSION:2.0\nPRODID:-//Liquicity Timetable Planner//NL\nCALSCALE:GREGORIAN\nMETHOD:PUBLISH\n"
        
        for act in geselecteerde_acts:
            date_clean = act["Datum"].replace("-", "")
            start_clean = act["Start"].replace(":", "") + "00"
            end_clean = act["Eind"].replace(":", "") + "00"
            
            st_hour = int(act["Start"].split(":")[0])
            act_date = date_clean
            if st_hour < 6:
                if act["Dag"] == "Vrijdag": act_date = "20260718"
                elif act["Dag"] == "Zaterdag": act_date = "20260719"
                elif act["Dag"] == "Zondag": act_date = "20260720"
            
            end_date = act_date
            if int(end_clean) < int(start_clean):
                if act_date == "20260717": end_date = "20260718"
                elif act_date == "20260718": end_date = "20260719"
                elif act_date == "20260719": end_date = "20260720"

            ics_content += "BEGIN:VEVENT\n"
            ics_content += f"SUMMARY:🚀 {act['Artiest']}\n"
            ics_content += f"LOCATION:🏟️ {act['Stage']}\n"
            ics_content += f"DESCRIPTION:Liquicity Weekend 2026\n"
            ics_content += f"DTSTART;TZID=Europe/Amsterdam:{act_date}T{start_clean}\n"
            ics_content += f"DTEND;TZID=Europe/Amsterdam:{end_date}T{end_clean}\n"
            ics_content += "END:VEVENT\n"
            
        ics_content += "END:VCALENDAR"
        
        ics_bytes = io.BytesIO(ics_content.encode("utf-8"))
        st.download_button(label="📅 Download .ics Agenda", data=ics_bytes, file_name="liquicity_timetable.ics", mime="text/calendar", use_container_width=True)
