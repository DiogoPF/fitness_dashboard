import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
from supabase import create_client, Client
import io
import pandas as pd


def render():
    # Load secrets
    url = st.secrets["supabase"]["url"]
    key = st.secrets["supabase"]["key"]
    bucket = st.secrets["supabase"]["bucket"]

    supabase: Client = create_client(url, key)

    # Download the CSV file
    file_name = "body_composition_agg.csv"
    response = supabase.storage.from_(bucket).download(file_name)

    # Load into pandas
    csv_bytes = response
    df = pd.read_csv(io.BytesIO(csv_bytes))
    st.dataframe(df)

    # ======= Process your data (example: filter rows where BMI > 25) =======
    df_processed = df[df["skeletal_muscle_mass"] < 30]

    # ======= Upload new CSV back to Supabase =======
    new_file_name = "processed_body_composition.csv"
    csv_buffer = io.StringIO()
    df_processed.to_csv(csv_buffer, index=False)

    # Upload to Supabase
    res = supabase.storage.from_(bucket).upload(
        path=new_file_name,
        file=csv_buffer.getvalue(),
        file_options={"content-type": "text/csv"},
        upsert=True,  # Overwrites file if it already exists
    )

    if res:
        st.success(f"Uploaded file: {new_file_name}")
    else:
        st.error("Upload failed")
