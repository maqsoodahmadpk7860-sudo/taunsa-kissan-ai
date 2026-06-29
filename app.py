# ===== LEHSAN KE 10 MASLE - BLOCK =====
    is_lehsan = any(w in text for w in ["lehsan", "garlic"])

    l_thrips_words = ["thrips lehsan", "safed nuqta"]
    l_whiterot_words = ["white rot", "jar safed", "fungus lehsan"]
    l_maggot_words = ["maggot lehsan", "jar keera"]

    if is_lehsan:
        if any(w in text for w in l_whiterot_words):
            st.error("**[LH4] White Rot** = SABSE KHATARNAK. Ilaj nahi. Agle saal zameen change karo. Beej treat karo.")
        elif any(w in text for w in l_thrips_words):
            st.error("**[LH1] Thrips** = Spinosad 120ml/acre. Har 7 din.")
        elif any(w in text for w in l_maggot_words):
            st.success("**[LH2] Maggot** = Chlorpyrifos flud.")
        else:
            st.info("Lehsan ka masla 10 me check karo.")

# ===== TAMATAR KE 15 MASLE - BLOCK =====
    is_tamatar = any(w in text for w in ["tamatar", "tomato", "tamata"])

    t_borer_words = ["fruit borer", "sundi tamatar", "surakh"]
    t_whitefly_words = ["whitefly tamatar", "tylcv", "patta lapet"]
    t_late_words = ["late blight tamatar", "patta kala tamatar"]
    t_wilt_words = ["bacterial wilt", "poda murjha", "tana doodh"]
    t_calcium_words = ["calcium kami", "nichla kala", "end rot"]

    if is_tamatar:
        if any(w in text for w in t_borer_words):
            st.error("**[TM1] Fruit Borer** = Emamectin 200ml + Spinosad 120ml mix. Har 5 din.")
        elif any(w in text for w in t_whitefly_words):
            st.error("**[TM10] TYLCV Virus** = Ilaj nahi. Whitefly roko Imida se. Beemar poda ukaro.")
        elif any(w in text for w in t_late_words):
            st.error("**[TM7] Late Blight** = Mancozeb+Metalaxyl har 5 din. Tamatar ka #1 fungus.")
        elif any(w in text for w in t_wilt_words):
            st.error("**[TM9] Bacterial Wilt** = Pani band. Khet khatam. Agle saal Beej change.")
        elif any(w in text for w in t_calcium_words):
            st.warning("**[TM12] Blossom End Rot** = Calcium Kami. Calcium spray + Pani balance karo.")
        else:
            st.info("Tamatar ka masla 15 me check karo.")
