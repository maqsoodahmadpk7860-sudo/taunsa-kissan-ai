import streamlit as st

st.title("🌾 Taunsa Kissan AI Helper")
user_input = st.text_input("Apna masla likho:")

if st.button("Hal Batao"):
    text = user_input.lower()
    
    # ===== 15 PEELA WORDS =====
    peela_words = ["peela", "peelay", "peely", "pely", "peelae", "pila", "peele", 
                   "peel", "zard", "zardi", "peelapan", "pela", "peelepan", "peelai", "pelay"]
    kapas_peela = "kapas" in text and any(word in text for word in peela_words)
    
    # ===== SUNDI KE 10 TARIQE =====
    sundi_words = ["sundi", "keera", "suta", "bollworm", "armyworm", "larva", 
                   "keere", "sundiyan", "american", "pink"] 
    kapas_sundi = "kapas" in text and any(word in text for word in sundi_words)
    
    # ===== WHITEFLY KE 10 TARIQE =====
    whitefly_words = ["whitefly", "safed", "makhi", "safed makhi", "bemari", "ju", 
                      "phirni", "chitti", "safaid", "white fly"] 
    kapas_whitefly = "kapas" in text and any(word in text for word in whitefly_words)
    # ==============================

    gandum_rash = "gandum" in text and ("rash" in text or "zang" in text)

    if kapas_peela: 
        st.success("**Hal:** Kapas ke peelay patty = Nitrogen ki kami. Urea 1 bag/acre + Imidacloprid spray.")
    
    elif gandum_rash:
        st.success("**Hal:** Gandum ka rash = Zang hai. Tilt 250 EC ya Nativo ka spray karo.")
    
    elif kapas_sundi:
        st.success("""**Hal: Sundi/Keera ka attack** 
        1. **Pehchan:** Patty kha rahi ho ya sutta me surakh = Bollworm/Armyworm.
        2. **Dawai:** Emamectin 1.9 EC @ 200ml/acre YA Lambda 2.5 EC @ 250ml/acre.
        3. **Time:** Spray sirf shaam 4 baje ke baad. Subah spray na karein.
        4. **Tip:** 1 baar Emamectin, agli baar Lambda. Rotate karna zaroori hai.""")
    
    elif kapas_whitefly:
        st.success("""**Hal: Whitefly/Safed Makhi ka attack** 
        1. **Pehchan:** Patty ulti karo, choti safed makhiyan urr rahi hongi. Patty chipchipi hai.
        2. **Dawai Mix:** Pyriproxyfen 10.8 EC + Buprofezin 25 SC. Dono mix karke spray karein.
        3. **Time:** Subah 9 baje se pehle ya shaam ko. Dhoop me spray waste hai.
        4. **Tip:** Sirf 1 zehar se nahi maregi. Mix spray + 7 din baad repeat karein.""")
    
    else:
        st.info(f"Ye masla abhi database me nahi hai. Aap ne likha: '{user_input}'")
