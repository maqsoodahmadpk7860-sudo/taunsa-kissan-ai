import streamlit as st
import pandas as pd

st.set_page_config(page_title="Kissan AI v2.0", layout="centered")
st.title("🌾 Kissan AI ULTIMATE v2.0 - 176+ Masle")
st.write("Ab Database System. Nayi fasal 1 minute me add karo.")

# 1. CSV Load karo. Cache se app tez ho jayegi
@st.cache_data
def load_data():
    df = pd.read_csv('fasal_masle.csv')
    return df

df = load_data()

user_input = st.text_input("Fasal + masla likho: kapas, gandum, rice, piaz, tamatar...")

if st.button("Hal Batao"):
    if user_input:
        text = user_input.lower()
        
        # 2. Fasal ka naam pakro
        faslen = df['fasal'].unique()
        found_fasal = None
        for f in faslen:
            if f in text:
                found_fasal = f
                break
        
        if found_fasal:
            # 3. Us fasal ke sab masle nikalo
            fasal_df = df[df['fasal'] == found_fasal]
            
            # 4. Pehchan_words me search karo
            result_found = False
            for index, row in fasal_df.iterrows():
                words = row['pehchan_words'].split(',')
                if any(word.strip() in text for word in words):
                    st.error(f"**[{found_fasal.upper()}{row['masla_id']}] {row['naam']}**")
                    st.success(f"**Hal:** {row['hal']}")
                    result_found = True
                    break # 1 masla mil gaya bas
            
            if not result_found:
                st.info(f"**{found_fasal}** ke {len(fasal_df)} masle database me hain. Keyword change karo.")
        else:
            st.warning(f"Fasal nahi mili. Ye faslen hain: {', '.join(faslen)}")
    else:
        st.warning("Masla likho bhai g.")
