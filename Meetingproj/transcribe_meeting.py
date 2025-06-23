import whisper
import os
import subprocess

def install_ffmpeg():
    try:
        subprocess.run(["ffmpeg", "-version"], check=True)
    except:
        subprocess.run(["apt-get", "update"], check=True)
        subprocess.run(["apt-get", "install", "-y", "ffmpeg"], check=True)

install_ffmpeg()



def transcribe_audio(audio_path="meeting_sample.mp3"):
    """
    Transcribes the given audio file using OpenAI's Whisper model and saves it to meeting_transcript.txt.
    
    Parameters:
    audio_path (str): Path to the audio file (default is 'meeting_sample.mp3').

    Returns:
    str: The transcribed text.
    """
    # Load the Whisper model
    model = whisper.load_model("tiny")

    # Transcribe the audio
    result = model.transcribe(audio_path)

    # Print the transcript
    print("\n📝 Transcript:\n")
    print(result["text"])

    # Save transcript to file
    with open("meeting_transcript.txt", "w", encoding="utf-8") as f:
        f.write(result["text"])

  
    return result["text"]
