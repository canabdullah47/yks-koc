import streamlit as st
import google.generativeai as genai

st.set_page_config(page_title="YKS Askeri Koç", page_icon="🎯", layout="wide")

st.title("🎯 YKS Askeri Disiplin Koçu")
st.markdown("---")

api_key = st.text_input("Gemini API Anahtarını Gir (Sadece bir kez):", type="password")

if api_key:
    genai.configure(api_key=api_key)
    model = genai.GenerativeModel('models/gemini-1.5-flash')
    with st.sidebar:
        st.header("📋 Günlük Rapor")
        calisma_suresi = st.slider("Net Odaklanma Süresi (Saat)", 0, 16, 8)
        ders = st.selectbox("Çalışılan Ders", ["TYT Matematik", "TYT Türkçe", "TYT Fen", "TYT Sosyal", "AYT", "Kamp/Genel"])
        konu = st.text_input("Konu")
        performans = st.select_slider("Verim", options=["Kötü", "Orta", "İyi", "Kusursuz"])
        zorluk = st.text_area("Takıldığın yerler/Bahaneler:")
        
        if st.button("Raporu Gönder"):
            prompt = f"""
            Sen askeri disipline sahip, sert, profesyonel bir YKS koçusun. Hedef: İlk 10.000.
            Bugünkü veriler: {ders} - {konu}, {calisma_suresi} saat, verim: {performans}.
            Zorluklar: {zorluk}.
            
            GÖREV:
            1. Askeri bir dille raporu değerlendir (başarıyı takdir et, rehaveti anında kes).
            2. 14 Eylül'e kadar vaktin daraldığını hatırlatarak yarın için acımasız ve stratejik bir hedef belirle.
            """
            response = model.generate_content(prompt)
            st.session_state.analiz = response.text

    if 'analiz' in st.session_state:
        st.subheader("📢 Koçun Emri")
        st.write(st.session_state.analiz)
else:
    st.warning("⚠️ Lütfen API anahtarını gir.")
