from local_summarizer import summarize_with_huggingface, extract_action_items, clean_transcript

# Step 1: Read transcript
with open("meeting_transcript.txt", "r", encoding="utf-8") as f:
    raw_transcript = f.read().strip()

# Step 2: Check and clean
if not raw_transcript:
    raise ValueError("❌ Transcript is empty.")
transcript = clean_transcript(raw_transcript)

# Step 3: Summarize
print("🧠 Generating summary...")
summary = summarize_with_huggingface(transcript)

# Step 4: Extract tasks
print("✅ Extracting action items...")
tasks = extract_action_items(transcript)

# Step 5: Save both to file
with open("meeting_summary.txt", "w", encoding="utf-8") as f:
    f.write("📋 Summary:\n")
    f.write(summary)
    f.write("\n\n✅ Action Items:\n")
    f.write(tasks)

print("🎉 meeting_summary.txt created with summary + action items.")

