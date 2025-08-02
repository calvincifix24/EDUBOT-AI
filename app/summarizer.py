from transformers import pipeline

# Load summarization pipeline
summarizer = pipeline("summarization")

def summarize_text(text):
    # Limit input length for performance and cost
    if len(text.split()) > 500:
        text = " ".join(text.split()[:500])
    summary = summarizer(text, max_length=120, min_length=30, do_sample=False)
    return summary[0]['summary_text']

# Example usage
if __name__ == "__main__":
    sample_text = '''
    Studying effectively requires a balance of motivation, planning, and time management.
    With AI, students can now automate tasks like summarizing notes, generating quizzes,
    and organizing schedules, making learning more personalized and efficient.
    '''
    print(summarize_text(sample_text))
