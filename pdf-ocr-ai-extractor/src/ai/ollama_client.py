import ollama
from ocr.tesseract_ocr import extract_text_from_pdf

class OllamaClient:
    def __init__(self, model_name):
        self.model_name = model_name

    def extract_relevant_info(self, text):
        prompt = (
            "From the following bank statement text, extract a list of all transactions. "
            "For each transaction, provide the date, a brief description, the withdrawal amount (if any), the deposit amount (if any), and the resulting balance. "
            "Format the response as a markdown table with five columns: 'Date', 'Description', 'Withdrawal', 'Deposit', and 'Balance'. "
            "Do not include any summary or extra text, only output the markdown table.\n\n"
            "Bank statement:\n"
            f"{text}"
        )
        response = ollama.generate(
            model=self.model_name,
            prompt=prompt,
            stream=False
        )
        return response['response']

