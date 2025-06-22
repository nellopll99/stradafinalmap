import pandas as pd
import io
import streamlit as st

def export_results(results):
    df = pd.DataFrame(results)
    buffer = io.BytesIO()
    df.to_excel(buffer, index=False, engine="openpyxl")
    buffer.seek(0)
    st.download_button(
        label="📥 Scarica risultati in Excel",
        data=buffer,
        file_name="inven_ai_results.xlsx",
        mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
    )
