from transformers import pipeline

# Load the summarization pipeline from Hugging Face
summarizer = pipeline("summarization")

def summarize_text(text, max_length=130, min_length=30):
    """
    Summarizes the input text using a pretrained transformer model.
    Args:
        text (str): The text to summarize.
        max_length (int): Maximum length of the summary.
        min_length (int): Minimum length of the summary.
    Returns:
        str: The summarized text.
    """
    summary = summarizer(text, max_length=max_length, min_length=min_length, do_sample=False)
    return summary[0]['summary_text']
