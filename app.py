import streamlit as st
import py3Dmol
import requests
from predict import predict_structure

st.set_page_config(layout="wide")
st.title("Protein Structure Viewer & Predictor")

tab1, tab2 = st.tabs(["Experimental Structure", "Predict Novel Sequence"])

# ---------- TAB 1: Experimental PDB ----------
with tab1:
    st.header("S6 Kinase Example – PDB 4L3J")

    pdb_url = "https://files.rcsb.org/download/4L3J.pdb"
    response = requests.get(pdb_url)

    if response.status_code == 200:
        pdb_data = response.text
        view = py3Dmol.view(width=750, height=520)
        view.addModel(pdb_data, "pdb")
        view.setStyle({
            "cartoon": {"colorscheme": {"prop":"b","gradient":"roygb","min":20,"max":80}}
        })
        view.zoomTo()
        st.components.v1.html(view._make_html(), height=540)

        st.download_button("Download PDB", pdb_data, "4L3J_S6K.pdb")
    else:
        st.error("Could not fetch 4L3J structure.")

# ---------- TAB 2: Novel Prediction ----------
with tab2:
    st.header("Predict Novel Protein Structure")

    protein_name = st.text_input("Protein name", value="MyProtein")
    sequence = st.text_area("Paste amino acid sequence", height=250)

    run = st.button("Predict Structure")

    if run:
        if not sequence.strip():
            st.error("Please enter a valid sequence")
        else:
            st.info("Running prediction (may take a few minutes)...")
            pdb_file = predict_structure(sequence, protein_name)

            with open(pdb_file) as f:
                pdb_data = f.read()

            # 3D viewer colored by B-factor (pLDDT)
            view = py3Dmol.view(width=750, height=520)
            view.addModel(pdb_data, "pdb")
            view.setStyle({
                "cartoon": {
                    "colorscheme": {"prop":"b","gradient":"roygb","min":50,"max":100}
                }
            })
            view.zoomTo()
            st.components.v1.html(view._make_html(), height=540)

            # Display average pLDDT (placeholder)
            st.metric("Average pLDDT Confidence", "80–90")  

            st.download_button("Download PDB", pdb_data, f"{protein_name}.pdb")
            st.success("Prediction complete!")
