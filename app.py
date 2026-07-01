import streamlit as st
import pandas as pd

st.set_page_config(page_title="Kissan AI v2.1", layout="centered")
st.title("🌾 Kissan AI ULTIMATE v2.1 - Smart Search")

@st.cache_data
def load_data():
    try:
        df = pd.read_csv('fasal-masle.csv', encoding='utf-8')
    except UnicodeDecodeError:
        df = pd.read_csv('fasal-masle.csv', encoding='latin1')
    return df

df = load_data()

user_input = st.text_input("Fasal + masla likho: kapas patta peela, piaz thrips...")

if user_input:
    search_terms = user_input.lower().split()
    results = df[df['Keywords'].str.lower().str.contains('|'.join(search_terms), na=False)]
    
    if not results.empty:
        for index, row in results.iterrows():
            st.success(f"**Masla Mila: {row['Fasal']} - {row['Masla']}**")
            st.write(f"**Hal:** {row['Hal']}")
            st.write(f"**Dawai:** {row['Dawai']}")
            st.markdown("---")
    else:
        st.warning("Ustad, is masle ka record abhi database me nahi hai.")
