from transformers import pipeline

def clean_transcript(text):
    lines = text.splitlines()
    cleaned_lines = [line.strip() for line in lines if len(line.strip()) > 10]
    return ' '.join(cleaned_lines)

def summarize_with_huggingface(text, max_tokens=500):
    summarizer = pipeline("summarization", model="t5-small", tokenizer="t5-small")

    words = text.split()
    if not words:
        raise ValueError("Transcript is empty or invalid.")

    summaries = []
    for i in range(0, len(words), max_tokens):
        chunk_words = words[i:i + max_tokens]
        chunk_text = ' '.join(chunk_words)
        chunk_text = "summarize: " + chunk_text

        try:
            summary = summarizer(chunk_text, max_length=120, min_length=30, do_sample=False)
            summaries.append(summary[0]['summary_text'])
        except Exception as e:
            summaries.append(f"[Error: {str(e)} in chunk: {chunk_text[:100]}...]")

    return "\n\n".join(summaries)

# ✅ Final wrapper to be imported from app.py (Only summary returned)
def summarize_text(transcript):
    cleaned = clean_transcript(transcript)
    summary = summarize_with_huggingface(cleaned)
    return summary
