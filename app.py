# app.py
import streamlit as st
from fpdf import FPDF

st.title("Helmes PDF Sample")

# テキスト入力
user_text = st.text_area("PDFにするテキストを入力してください", "ここに本文を入力")

# ボタンを押すとPDF生成
if st.button("PDFを生成"):
    pdf = FPDF()
    pdf.add_page()
    # フォントはiPhone/Mac標準
    pdf.set_font("Arial", size=12)
    pdf.multi_cell(0, 10, user_text)
    pdf_file = "generated_document.pdf"
    pdf.output(pdf_file)
    
    # ダウンロードリンク表示
    with open(pdf_file, "rb") as f:
        st.download_button(
            label="PDFをダウンロード",
            data=f,
            file_name=pdf_file,
            mime="application/pdf"
        )
