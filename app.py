import streamlit as st

st.set_page_config(page_title="Taunsa Kissan AI Helper")
st.title("🌾 Taunsa Kissan AI Helper")
st.write("Kapas ya Gandum ki bimari pucho Urdu/Roman Urdu me.")

data = {
    "kapas peelay pattay": "Hal: NPK khaad kam hai. 1 bori NPK per acre daalo.",
    "kapas ke keeray": "Hal: Imidacloprid spray karo shaam ke waqt.",
    "gandum ka rash": "Hal: Tilt fungicide ka spray karo.",
    "gandum peela": "Hal: Urea ki kami hai. 1 bori urea daalo."
}

user_input = st.text_input("Apna masla likho:")

if st.button("Hal Batao"):
    found = False
    for key in data:
        if key in user_input.lower():
            st.success(data[key])
            found = True
            break
    if not found:
        st.warning("Try karo: 'kapas peelay pattay' ya 'gandum ka rash'")
