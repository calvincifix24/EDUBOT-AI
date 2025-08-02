from pdf_extractor import extract_text_from_pdf
from text_summarizer import summarize_text

def main():
    pdf_path = input("Enter the path to your PDF file: ")

    try:
        print("\n📥 Extracting text...")
        text = extract_text_from_pdf(pdf_path)

        if not text.strip():
            print("❌ No readable text found in the PDF.")
            return

        print("\n🧠 Summarizing content...")
        summary = summarize_text(text)

        print("\n✅ Summary:\n")
        print(summary)

    except Exception as e:
        print(f"⚠️ Error: {e}")

if __name__ == "__main__":
    main()
