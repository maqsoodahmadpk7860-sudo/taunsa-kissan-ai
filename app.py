import streamlit as st

st.title("🌾 Taunsa Kissan AI Helper")

user_input = st.text_input("Apna masla likho:")

if st.button("Hal Batao"):
    text = user_input.lower()
    
    # Check karo kapas + peela/peelay/peely hai ya nahi
    if "kapas" in text and ("peel" in text): 
        st.success("**Hal:** Kapas ke peelay patty = Nitrogen ki kami. Urea 1 bag/acre do + Imidacloprid spray.")
    
    # Check karo gandum + rash/zang hai ya nahi  
    elif "gandum" in text and ("rash" in text or "zang" in text):
        st.success("**Hal:** Gandum ka rash = Zang hai. Tilt ya Nativo fungicide ka spray karo.")
    
    else:
        st.info(f"Filhal main sirf Kapas ke peelay patty aur Gandum ka rash janta hun. Aap ne likha: '{user_input}'")
