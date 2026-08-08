import streamlit as st
import google.generativeai as genai

st.set_page_config(page_title="YKS Askeri Koç", page_icon="🎯")

st.title("🎯 YKS Askeri Disiplin Koçu")

api_key = st.text_input("Gemini API Anahtarını Gir:", type="password")

if api_key:
    try:
        genai.configure(api_key=api_key)
        # Model adını en basit haliyle tanımlıyoruz
        model = genai.GenerativeModel('gemini-1.5-flash')
        
        ders = st.selectbox("Ders", ["Matematik", "Türkçe", "Fen", "Sosyal"])
        konu = st.text_input("Konu")
        verim = st.select_slider("Verim", ["Kötü", "Orta", "İyi", "Kusursuz"])
        
        if st.button("Raporu Gönder"):
            with st.spinner('Koç değerlendiriyor...'):
                prompt = f"Sen sert bir YKS koçusun. {ders} dersinden {konu} çalıştım. Verimim: {verim}. Askeri bir dille kısa ve öz yorum yap."
                response = model.generate_content(prompt)
                st.write(response.text)
    except Exception as e:
        st.error(f"Bir hata oluştu: {e}")
else:
    st.info("Lütfen devam etmek için API anahtarınızı girin.")

