import pdfplumber

def parse_resume(file_path):
    try:
        with pdfplumber.open(file_path) as pdf:
            first_page = pdf.pages[0]
            text = first_page.extract_text()
            return {"extracted_text": text[:100]} 
    except Exception as e:
        return {"error": str(e)}

# profiles to be tested
test_files = ["parsers/test1.pdf", "parsers/test2.pdf", "parsers/test3.pdf", "parsers/test4.pdf"]

# process each file and print the results
for file_path in test_files:
    print(f"--- Processing: {file_path} ---")
    result = parse_resume(file_path)
    print(result)
    print("-" * 30)