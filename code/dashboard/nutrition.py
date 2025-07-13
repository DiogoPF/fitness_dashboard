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
    file_name = "body_composition_agg.csv"  # Change to your filename
    response = supabase.storage.from_(bucket).download(file_name)

    # Load into pandas
    csv_bytes = response
    df = pd.read_csv(io.BytesIO(csv_bytes))

    st.dataframe(df)
