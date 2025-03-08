import os
from pytubefix import YouTube
import streamlit as st
from sys import argv

def baixar(url):
        yt = YouTube(url)
        print("Title: ", yt.title)
        st.write(f"📌 **Título:** ", yt.title)
        st.write(f"📌 **Visualizações:** ", yt.views)

        stream = yt.streams.get_highest_resolution()
        status = stream.download(output_path="downloads")
        if status : 
            st.success("✅ Download concluído!")
        else:
             st.error("❌ Erro desconhecido ao baixar o vídeo.")

def main():
    st.title("🎬 Baixador de Vídeos do YouTube")
    url = st.text_input("📌 Insira a URL do vídeo:")
    
    if st.button("Baixar 🎥"):
        if url:
            baixar(url)
        else:
            st.warning("⚠️ Por favor, insira uma URL válida.")

if __name__ == "__main__":
    main()