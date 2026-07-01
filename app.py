import streamlit as st
import pandas as pd
import os
from PIL import Image
import google.generativeai as genai

# ====== CONFIG ======
st.set_page_config(page_title="Kissan AI ULTIMATE v3.0", page_icon="🌾", layout="wide")

# ====== GEMINI AI SETUP - Photo Ke Liye ======
try:
    API_KEY = st.secrets["GEMINI_API_KEY"]
    genai.configure(api_key=API_KEY)
    model_vision = genai.GenerativeModel('gemini-1.5-flash') # Ye photo dekhta hai
    AI_ENABLED = True
except Exception:
    AI_ENABLED = False

# ====== DATA LOAD ======
@st.cache_data
def load_data():
    try:
        df = pd.read_csv("fasal-masle.csv", encoding="utf-8")
        return df
    except Exception as e:
        st.error(f"CSV Load Error: {e}")
        return pd.DataFrame()

df = load_data()

# ====== UI HEADER ======
st.title("🌾 Kissan AI ULTIMATE v3.0")
st.subheader("Photo Se Beemari Pehchano ya Naam Se Talash Karo")

tab1, tab2 = st.tabs(["📸 Photo Se Pehchano", "🔍 Naam Se Talash Karo"])

# ====== TAB 1: PHOTO WALA AI ======
with tab1:
    st.write("**Patte ya Phal ki Photo Upload Karo**")
    uploaded_file = st.file_uploader("Photo yahan drag karo...", type=["jpg", "png", "jpeg"])

    if uploaded_file is not None and AI_ENABLED:
        image = Image.open(uploaded_file)
        st.image(image, caption="Aap ki Upload ki hui Photo", use_column_width=True)
        
        if st.button("AI Se Beemari Pocho 🧠"):
            with st.spinner("AI photo check kar raha hai... 10 second ruko"):
                prompt = """
                Tum Pakistan ke Kissan Ustad ho. Is fasal ke patte/phal ki photo dekho. 
                1. Fasal ka naam btao Urdu me.
                2. Beemari ka naam btao Urdu me.
                3. 2 Line me aasan Hal btao Urdu me.
                4. 1 Dawai ka naam btao.
                Jawab sirf Urdu me do, list ki shakal me.
                """
                response = model_vision.generate_content([prompt, image])
                st.success("**AI ka Jawab:**")
                st.markdown(response.text)

    elif not AI_ENABLED:
        st.warning("AI Feature band hai. `GEMINI_API_KEY` Streamlit Secrets me add karo.")

# ====== TAB 2: NAAM SE TALASH ======
with tab2:
    st.write("**Fasal + masla likho, foran hal pao**")
    query = st.text_input("Misaal: kapas patta peela, aam hopper, kino greening")

    if query and not df.empty:
        query = query.lower()
        results = df[df['Keywords'].str.lower().str.contains(query, na=False)]
        
        if not results.empty:
            st.success(f"**{len(results)} Hal Mil Gaye:**")
            for _, row in results.iterrows():
                with st.expander(f"**{row['Fasal']} : {row['Masla']}**"):
                    st.write(f"**Hal:** {row['Hal']}")
                    st.write(f"**Dawai:** {row['Dawai']}")
        else:
            st.warning("Is naam se koi beemari nahi mili. Photo wala tab try karo.")

elif df.empty:
    st.error("Database khali hai. `fasal-masle.csv` check karo.")
