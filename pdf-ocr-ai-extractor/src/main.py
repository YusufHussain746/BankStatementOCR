from ocr.tesseract_ocr import extract_text_from_pdf
from ai.ollama_client import OllamaClient
from excel.excel_writer import write_to_excel
import os

def main(pdf_file_path, excel_output_path):
    if not os.path.exists(pdf_file_path):
        print(f"Error: The file {pdf_file_path} does not exist.")
        return

    # Step 1: Extract text from the PDF using Tesseract OCR
    extracted_text = extract_text_from_pdf(pdf_file_path)
    print("Extracted text: \n", extracted_text)  
    if not extracted_text:
        print("Error: No text extracted from the PDF.")
        return

    # Step 2: Feed the extracted text to the AI model using Ollama
    ollama_client = OllamaClient(model_name="gemma3:12b")
    structured_info = ollama_client.extract_relevant_info(extracted_text)
    print("AI response: \n", structured_info)
    # Step 3: Write the structured information to an Excel file
    write_to_excel(structured_info, excel_output_path)
    print(f"Successfully written the structured information to {excel_output_path}")

if __name__ == "__main__":
    pdf_file = input("Enter the path to the PDF file: ").strip()
    # Get the base name without extension
    base_name = os.path.splitext(os.path.basename(pdf_file))[0]
    # Create the output Excel path
    excel_dir = r"C:\Users\User\Desktop\PDF Extractor MOE\excels"
    os.makedirs(excel_dir, exist_ok=True)
    excel_file = os.path.join(excel_dir, f"{base_name}.xlsx")
    main(pdf_file, excel_file)