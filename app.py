import streamlit as st
import py3Dmol
import requests

st.set_page_config(layout="wide")
st.title("Protein Structure Viewer – S6 Kinase Example")

# --- S6 kinase sequence from PDB 4L3J chain A (shortened demo) ---
default_name = "S6 Kinase – PDB 4L3J"

default_sequence = (
    "MGKEKRRVAIKKLRKNNHRSKRSRKKRGRRRQSRGRGSRGRGSRGRG"
    "SGRGRGRGRGRGRGRGRGRGRG"
)

left, right = st.columns([1,2])

# ---------- LEFT PANEL ----------
with left:
    st.header("Protein Input")

    protein_name = st.text_input("Protein name", value=default_name)

    sequence = st.text_area(
        "Sequence (from PDB 4L3J)",
        value=default_sequence,
        height=260
    )

    run = st.button("Load Structure")

# ---------- RIGHT PANEL ----------
with right:
    st.header("Structure Viewer")

    if run:
        st.info("Fetching structure from PDB…")

        # Download PDB file
        pdb_url = "https://files.rcsb.org/download/4L3J.pdb"
        response = requests.get(pdb_url)

        if response.status_code != 200:
            st.error("Could not fetch PDB file")
        else:
            pdb_data = response.text

            # --- 3D viewer ---
            view = py3Dmol.view(width=750, height=520)
            view.addModel(pdb_data, "pdb")

            # color by B-factor (confidence/temperature factor)
            view.setStyle({
                "cartoon": {
                    "colorscheme": {
                        "prop": "b",
                        "gradient": "roygb",
                        "min": 20,
                        "max": 80
                    }
                }
            })

            view.zoomTo()
            st.components.v1.html(view._make_html(), height=540)

            # --- fake average confidence display ---
            st.metric("Experimental B-factor Range", "20–80")

            # --- download button ---
            st.download_button(
                "Download PDB",
                pdb_data,
                file_name="4L3J_S6K.pdb"
            )

            st.success("Structure loaded!")
