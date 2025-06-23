import os
import streamlit as st
import subprocess
from transcribe_meeting import transcribe_audio
from local_summarizer import summarize_text

st.set_page_config(page_title="Meeting Transcriber & Summarizer", layout="centered")

st.title("🎙️ Meeting Audio Transcriber & Summarizer")

uploaded_file = st.file_uploader("Upload your meeting audio file (.mp3 or .wav)", type=["mp3", "wav"])

if uploaded_file is not None:
    with open("uploaded_audio.mp3", "wb") as f:
        f.write(uploaded_file.read())
    
    st.info("Transcribing audio...")
    transcript = transcribe_audio("uploaded_audio.mp3")
    
    st.success("Transcription complete!")
    st.subheader("📝 Transcript")
    st.text_area("", transcript, height=300)
    
    st.info("Summarizing transcript...")
    summary = summarize_text(transcript)

    
    st.success("Summarization complete!")

    st.subheader("📄 Summary")
    st.write(summary)

    try:
       output = subprocess.check_output(["ffmpeg", "-version"]).decode()
       st.text("✅ FFmpeg is installed!")
       st.text(output.splitlines()[0])
    except Exception as e:
       st.error(f"❌ FFmpeg check failed: {e}")

    st.text("FFmpeg exists: " + str(os.system("which ffmpeg") == 0))

    

    # Option to download
    full_summary = f"📄 Summary:\n{summary}"
    st.download_button("📥 Download Summary", data=full_summary, file_name="meeting_summary.txt", mime="text/plain")
