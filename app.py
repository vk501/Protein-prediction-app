import streamlit as st
from predict import predict_structure
import py3Dmol

st.title("Protein Structure Prediction App")

st.write("Enter an amino acid sequence to predict its structure")

sequence = st.text_area("Protein sequence")

if st.button("Predict Structure"):

    if not sequence:
        st.error("Please enter a sequence")
    else:
        st.info("Running prediction...")

        pdb_file = predict_structure(sequence)

        with open(pdb_file) as f:
            pdb_data = f.read()

        # show structure
        view = py3Dmol.view(width=700, height=500)
        view.addModel(pdb_data, "pdb")
        view.setStyle({"cartoon": {"color": "spectrum"}})
        view.zoomTo()

        st.components.v1.html(view._make_html(), height=500)

        # download button
        st.download_button(
            "Download PDB",
            pdb_data,
            file_name="predicted_structure.pdb"
        )

        st.success("Prediction complete!")
