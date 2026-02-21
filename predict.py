import streamlit as st
from urllib.parse import quote

st.title("Predict Novel Protein Structure with ColabFold")

sequence = st.text_area("Paste your sequence here")

if st.button("Run in ColabFold"):
    if not sequence.strip():
        st.error("Enter a sequence first")
    else:
        # Encode sequence for URL
        encoded_seq = quote(sequence)
        colab_url = f"https://colab.research.google.com/github/sokrypton/ColabFold/blob/main/AlphaFold2_mmseqs2.ipynb#scrollTo=0&sequence={encoded_seq}"
        st.markdown(f"[Click here to run in ColabFold]({colab_url})", unsafe_allow_html=True)
