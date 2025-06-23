from faster_whisper import WhisperModel

# Load the model - you can also try "tiny", "small", etc. for speed
model = WhisperModel("base")  # use "tiny" or "small" for even faster speed

# Transcribe the audio
segments, info = model.transcribe("meeting_sample.mp3")

# Save the transcription
with open("meeting_transcript.txt", "w", encoding="utf-8") as f:
    for segment in segments:
        f.write(segment.text.strip() + "\n")

print("✅ Transcription complete. Saved to 'meeting_transcript.txt'")
