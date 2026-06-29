import streamlit as st

st.title("🌾 Taunsa Kissan AI Helper")
user_input = st.text_input("Apna masla likho:")

if st.button("Hal Batao"):
    text = user_input.lower()
    
    # ===== 15 PEELA RELATED WORDS LIST =====
    peela_words = [
        "peela", "peelay", "peely", "pely", "peelae", "pila", "peele", 
        "peel", "zard", "zardi", "peelapan", "pela", "peelepan", "peelai", "pelay"
    ]
    # Check karo koi 1 lafz bhi hai text me?
    kapas_peela = "kapas" in text and any(word in text for word in peela_words)
    # =======================================
    
    gandum_rash = "gandum" in text and ("rash" in text or "zang" in text)
    kapas_whitefly = "kapas" in text and ("whitefly" in text or "safed" in text or "makhi" in text)
    kapas_sundi = "kapas" in text and ("sundi" in text or "keera" in text or "suta" in text)

    if kapas_peela: 
        st.success("**Hal:** Kapas ke peelay patty = Nitrogen ki kami. Urea 1 bag/acre + Imidacloprid spray.")
    
    elif gandum_rash:
        st.success("**Hal:** Gandum ka rash = Zang hai. Tilt ya Nativo fungicide ka spray karo.")
    
    elif kapas_whitefly:
        st.success("**Hal:** Whitefly/Safed Makhi = Pyriproxyfen + Buprofezin ka spray subah karein.")
    
    elif kapas_sundi:
        st.success("**Hal:** Sundi/Keera = Emamectin 1.9 EC ya Lambda spray shaam ko.")
    
    else:
        st.info(f"Ye masla abhi database me nahi hai. Aap ne likha: '{user_input}'")
