from src.pdf_processor import extract_text_from_pdf


pdf_path = "data/sample_resumes/mana infy.pdf"

text = extract_text_from_pdf(pdf_path)

print("Extracted Resume Text:")
print(text)