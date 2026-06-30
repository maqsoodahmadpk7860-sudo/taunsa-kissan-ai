import streamlit as st
import pandas as pd

st.set_page_config(page_title="Kissan AI v2.1", layout="centered")
st.title("🌾 Kissan AI ULTIMATE v2.1 - Smart Search")

@st.cache_data
def load_data():
    df = pd.read_csv('fasal_masle.csv')
    return df

df = load_data()

user_input = st.text_input("Fasal + masla likho: kapas patta peela, piaz thrips...")

if st.button("Hal Batao"):
    if user_input:
        text = user_input.lower()
        user_words = text.split() # User ke sab words list me tod do
        
        # 1. Fasal ka naam pakro
        faslen = df['fasal'].unique()
        found_fasal = None
        for f in faslen:
            if f in text:
                found_fasal = f
                break
        
        if found_fasal:
            fasal_df = df[df['fasal'] == found_fasal]
            
            # 2. SMART SEARCH SHURU - Score System
            best_match = None
            best_score = 0

            for index, row in fasal_df.iterrows():
                db_words = row['pehchan_words'].split(',')
                score = 0
                for db_word in db_words:
                    if db_word.strip() in user_words: # Agar 1 word match hua
                        score += 1
                
                if score > best_score: # Jis ka score sabse zyada
                    best_score = score
                    best_match = row
            
            # 3. Result dikhao
            if best_score > 0: # Matlab kam se kam 1 word match hua
                st.error(f"**[{found_fasal.upper()}{best_match['masla_id']}] {best_match['naam']} - {best_score} Match**")
                st.success(f"**Hal:** {best_match['hal']}")
            else:
                st.info(f"**{found_fasal}** ke {len(fasal_df)} masle database me hain. Thora detail likho. Ex: `kapas whitefly` ya `kapas gulabi`")
        else:
            st.warning(f"Fasal nahi mili. Ye faslen hain: {', '.join(faslen)}")
    else:
        st.warning("Masla likho bhai g.")
