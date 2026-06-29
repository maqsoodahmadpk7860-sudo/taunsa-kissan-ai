import streamlit as st

st.title("🌾 Taunsa Kissan AI Helper")
user_input = st.text_input("Apna masla likho:")

if st.button("Hal Batao"):
    text = user_input.lower()
    
    # ===== 15 PEELA WORDS =====
    peela_words = ["peela", "peelay", "peely", "pely", "peelae", "pila", "peele", 
                   "peel", "zard", "zardi", "peelapan", "pela", "peelepan", "peelai", "pelay"]
    kapas_peela = "kapas" in text and any(word in text for word in peela_words)
    # ==========================
    
    # ===== SUNDI KE 12 WORDS =====
    sundi_words = ["sundi", "keera", "suta", "bollworm", "armyworm", "larva", 
                   "keere", "sundiyan", "american", "pink", "spotted", "kera"]
    kapas_sundi = "kapas" in text and any(word in text for word in sundi_words)
    # ==============================
    
    gandum_rash = "gandum" in text and ("rash" in text or "zang" in text)
    kapas_whitefly = "kapas" in text and ("whitefly" in text or "safed" in text or "makhi" in text)

    if kapas_peela: 
        st.success("**Hal:** Kapas ke peelay patty = Nitrogen ki kami. Urea 1 bag/acre + Imidacloprid spray.")
    
    elif gandum_rash:
        st.success("**Hal:** Gandum ka rash = Zang hai. Tilt 250 EC ya Nativo ka spray karo.")
    
    elif kapas_whitefly:
        st.success("**Hal:** Whitefly/Safed Makhi = Pyriproxyfen + Buprofezin mix spray subah 9 baje se pehle.")
    
    elif kapas_sundi:
        st.success("""**Hal: Sundi/Keera ka attack** 
        1. **Pehchan:** Patty kha rahi ho ya sutta me surakh hai = Bollworm/Armyworm.
        2. **Zahreeli Dawai:** Emamectin Benzoate 1.9 EC @ 200ml/acre YA Lambda 2.5 EC @ 250ml/acre.
        3. **Time:** Spray sirf shaam 4 baje ke baad karein. Subah spray bekar hai.
        4. **Tip:** 1 spray Emamectin, agla spray Lambda. Repeat nahi karna warna resist ho jayegi.""")
    
    else:
        st.info(f"Ye masla abhi database me nahi hai. Aap ne likha: '{user_input}'")
