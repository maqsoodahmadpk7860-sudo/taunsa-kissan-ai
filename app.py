import streamlit as st

st.set_page_config(page_title="Taunsa Kissan AI")
st.title("🌾 Taunsa Kissan AI Helper")
st.write("Kapas ya Gandum ka masla Roman Urdu me likho.")

user_input = st.text_input("Apna masla likho:")

if st.button("Hal Batao"):
    text = user_input.lower()
    
    if not text:
        st.warning("Pehle masla likho bhai")
    
    elif "kapas" in text and ("peela" in text or "peelay" in text):
        st.success("**Hal:** Kapas ke peelay patty = Nitrogen ki kami ya Leaf Curl Virus. 1. Urea 1 bag/acre. 2. Imidacloprid ka spray karein.")
    
    elif "gandum" in text and ("rash" in text or "zang" in text):
        st.success("**Hal:** Gandum ka rash = Zang/Rust hai. Tilt 250 EC ya Nativo ka spray subah karein. Pani kam lagayen.")
    
    else:
        st.info("Filhal main sirf Kapas ke peelay patty aur Gandum ka rash janta hun. Baqi masle jald add karunga.")
