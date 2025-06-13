import streamlit as st
import pandas as pd
import io

def export_to_excel(df):
    buffer = io.BytesIO()
    df.to_excel(buffer, index=False)
    buffer.seek(0)
    st.download_button(
        label="📥 Scarica Excel",
        data=buffer,
        file_name="mna_company_list.xlsx",
        mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
    )
