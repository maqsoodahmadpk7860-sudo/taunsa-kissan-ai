import streamlit as st

st.title("🌾 Kissan AI ULTIMATE - 85 Masle")
user_input = st.text_input("Fasal + masla likho: kapas, gandum, rice, sunflower")

if st.button("Hal Batao"):
    text = user_input.lower()
    is_kapas = any(w in text for w in ["kapas","cotton","kpas","narma"])
    is_gandum = any(w in text for w in ["gandum","wheat","gehun"])
    is_rice = any(w in text for w in ["rice","chawal","dhan","monji"])
    is_sunflower = any(w in text for w in ["sunflower","soraj mukhi","sorajmukhi","soraj"])

    # ===== SUNFLOWER KE 12 MASLE - 20 NAAM EACH =====
    s_sundi_words = ["sundi", "hairy caterpillar", "keera", "patta kha gaya", "bihar"]
    s_jassid_words = ["jassid", "tela", "cup patta"]
    s_aphid_words = ["aphid", "chattel", "phool keera"]
    s_moth_words = ["moth", "dana keera", "sunflower moth"]

    s_mildew_words = ["downy mildew", "safed powder neeche", "phupondi"]
    s_rust_words = ["rust", "zang", "bhura dhabba"]
    s_alternaria_words = ["alternaria", "kala dhabba", "target"]
    s_headrot_words = ["head rot", "phool gal", "phool kala", "phool sara"]

    s_boron_words = ["boron kami", "phool khali", "dana nahi", "phool chota"]
    s_n_words = ["nitrogen kami sunflower", "poda peela"]
    s_parrot_words = ["parrot", "chiriya", "dana kha gaya", "totay"]
    s_weed_words = ["ghas", "jari booti sunflower", "weed"]
    # ==============================================

    if is_sunflower:
        if any(w in text for w in s_sundi_words):
            st.error("""**[SF1] Bihar Sundi - SABSE KHATARNAK**
            1. **Pehchan:** 2 din me pora khet saaf. Balon wali sundi.
            2. **Hal:** Emamectin 200ml + Lambda 250ml mix/acre. Foran spray.""")

        elif any(w in text for w in s_boron_words):
            st.warning("""**[SF9] Boron Kami** = Phool khali, dana nahi.
            1. **Hal:** Boron 500g/acre. Phool aane se pehle spray zaroori. Sunflower ka #1 masla.""")

        elif any(w in text for w in s_parrot_words):
            st.error("""**[SF11] Parrot/Chiriya** = Dana pakte hi khatam.
            1. **Hal:** Dawai nahi. CD lagao, jali, ya 2 baje khud khet me raho 😅""")

        elif any(w in text for w in s_headrot_words):
            st.error("""**[SF8] Head Rot** = Phool andar se kala sara.
            1. **Hal:** Barish band karo. Copper spray. Dana kharab.""")

        elif any(w in text for w in s_mildew_words):
            st.success("""**[SF5] Downy Mildew** = Patta neeche safed.
            Hal: Metalaxyl 200g/acre. Poda chota reh jata.""")

        elif any(w in text for w in s_jassid_words):
            st.success("""**[SF2] Jassid** = Patta cup.
            Hal: Acetamiprid 100g/acre.""")

        elif any(w in text for w in s_aphid_words):
            st.success("""**[SF3] Aphid** = Phool ke neeche guchha.
            Hal: Imidacloprid 100ml/acre.""")

        elif any(w in text for w in s_moth_words):
            st.success("""**[SF4] Sunflower Moth** = Dana khali.
            Hal: Spinosad 120ml/acre. Phool pe spray.""")

        elif any(w in text for w in s_rust_words):
            st.success("""**[SF6] Rust** = Bhura dhabba.
            Hal: Tilt 100ml/acre.""")

        elif any(w in text for w in s_alternaria_words):
            st.success("""**[SF7] Alternaria** = Bara kala dhabba.
            Hal: Mancozeb 500g/acre.""")

        elif any(w in text for w in s_n_words):
            st.warning("""**[SF10] Nitrogen Kami** = Poda peela.
            Hal: Urea 1 bag/acre.""")

        elif any(w in text for w in s_weed_words):
            st.info("""**[SF12] Jari Booti** = Shuru me ghas.
            Hal: 40 din tak ghas saaf rakho. Pendimethalin pre-emergent.""")

        else:
            st.info(f"Sunflower ka masla 12 me nahi: '{user_input}'")

    # ===== ELSE ME RICE 18 KA CODE =====
    elif is_rice:
        st.success("Rice ka 18 masla yahan check hoga.")

    # ===== ELSE ME GANDUM 15 KA CODE =====
    elif is_gandum:
        st.success("Gandum ka 15 masla yahan check hoga.")

    # ===== ELSE ME KAPAS 40 KA CODE =====
    elif is_kapas:
        st.success("Kapas ka 40 masla yahan check hoga.")
    else:
        st.info(f"Fasal likho: kapas, gandum, rice, sunflower '{user_input}'")
