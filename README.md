# 🎙️ Meeting Transcriber & Summarizer
Meeting Transcriber & Summarizer is a Python-based project that transcribes audio meeting recordings using OpenAI’s Whisper model and summarizes them using Hugging Face Transformers. The application includes a simple Streamlit UI for user interaction.

# 🚀 Features

- Upload .mp3 or .wav files for transcription.
- Converts speech to text using Whisper or Faster-Whisper.
- Summarizes the transcript using T5-small from Hugging Face.
- Clean UI using Streamlit (optional) or CLI.
- Option to download the final summary.

# 🛠️ Technologies Used

- Python 3.10
- OpenAI Whisper / Faster-Whisper
- Hugging Face Transformers (T5-small)
- Streamlit (optional UI)
- ffmpeg (for audio processing)

# 📦 Dependencies

- openai-whisper or faster-whisper
- streamlit
- transformers
- torch
- ffmpeg

# ⚙️ Installation
1. Clone the repository:
    git clone https://github.com/samruddhi2003/meeting-transcriber.git
    cd meeting-transcriber

2. Install dependencies:
    pip install -r requirements.txt

3. (Optional) Install ffmpeg:
    - Windows: choco install ffmpeg
    - Ubuntu: sudo apt install ffmpeg

4. Run with Streamlit:
    streamlit run app.py

# 📁 Project Structure

- app.py — Streamlit UI logic
- transcribe_meeting.py — Audio transcription logic
- local_summarizer.py — Text summarization functions
- meeting_sample.mp3 — Example input
- meeting_transcript.txt — Output transcript

# 🧪 How It Works

1. User uploads a .mp3 or .wav file.
2. Whisper or Faster-Whisper transcribes it into text.
3. The transcript is passed to T5-small for summarization.
4. Output is displayed in the UI and available for download.

# 📄 Example Usage

- Run app.py with Streamlit to use the UI.
- Or run transcribe_meeting.py and local_summarizer.py manually for CLI version.

# 📤 Deployment

You can deploy this project on:
- Streamlit Cloud (streamlit.io)
- Local machine with Python installed
- Any basic web server with Gradio or Flask (optional)
# ⚠️ Note
This app is deployed on Streamlit Cloud (CPU-only). For large audio files or faster performance, we recommend running locally on a GPU or deploying with GPU support (Colab Pro / Hugging Face Spaces / RunPod).

# 📜 License
This project is licensed under the MIT License.
