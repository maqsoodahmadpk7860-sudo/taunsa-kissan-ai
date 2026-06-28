import streamlit as st

st.title("🌾 Taunsa Kissan AI Helper")
st.write("Kapas ya Gandum ki bimari pucho Urdu/Roman Urdu me.")

user_input = st.text_input("Apna masla likho:")

if st.button("Hal Batao"):
    if not user_input:
        st.warning("Pehle masla likho bhai")
    elif "kapas" in user_input.lower() and ("peela" in user_input.lower() or "peelay" in user_input.lower()):
        st.success("Hal: Kapas ke peelay patty = Nitrogen ki kami ya fungus ho sakta hai. Urea 1 bag/acre do, aur copper fungicide ka spray karo.")
  elif "gandum" in user_input.lower() and ("rash" in user_input.lower() or "zang" in user_input.lower()):
        st.success("Hal: Gandum ka rash = Zang/Rust bimari hai. Tilt ya Nativo fungicide ka spray karo subah ke waqt.")
    else:
        st.info("Filhal main sirf Kapas ke peelay patty aur Gandum ka rash janta hun. Baqi masle jald add karunga.")
