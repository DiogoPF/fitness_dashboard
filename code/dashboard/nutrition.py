import streamlit as st
import io
import pandas as pd
from supabase import create_client, Client


def render():
    # Load secrets from Streamlit
    url = st.secrets["supabase"]["url"]
    key = st.secrets["supabase"]["key"]
    bucket = st.secrets["supabase"]["bucket"]

    supabase: Client = create_client(url, key)

    # Download CSV file from bucket
    file_name = "body_composition_agg.csv"
    response = supabase.storage.from_(bucket).download(file_name)
    csv_bytes = response
    df = pd.read_csv(io.BytesIO(csv_bytes))

    st.dataframe(df)

    # Process: filter rows where BMI > 25 (example)
    df_processed = df[df["skeletal_muscle_mass"] < 30]

    # Convert processed DataFrame to CSV bytes
    csv_buffer = io.StringIO()
    df_processed.to_csv(csv_buffer, index=False)
    csv_bytes_processed = csv_buffer.getvalue().encode(
        "utf-8"
    )  # convert string to bytes

    # Upload processed CSV back to Supabase storage bucket
    new_file_name = "processed_body_composition.csv"
    res = supabase.storage.from_(bucket).upload(
        path=new_file_name,
        file=csv_bytes_processed,
        file_options={"content-type": "text/csv"},
        upsert=True,  # overwrite if exists
    )

    if res:
        st.success(f"Uploaded processed file: {new_file_name}")
    else:
        st.error("Failed to upload processed file")
