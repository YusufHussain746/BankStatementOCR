# PDF OCR AI Extractor

This project is designed to extract text from PDF files using Tesseract OCR, process the extracted text with an AI model via Ollama, and organize the relevant information into a structured Excel file.

## Project Structure

```
pdf-ocr-ai-extractor
├── src
│   ├── main.py                # Entry point of the application
│   ├── ocr
│   │   └── tesseract_ocr.py   # Functions for OCR processing
│   ├── ai
│   │   └── ollama_client.py    # Interactions with the Ollama AI model
│   ├── excel
│   │   └── excel_writer.py      # Functions for writing to Excel files
│   └── utils
│       └── pdf_utils.py        # Utility functions for PDF handling
├── requirements.txt            # Project dependencies
└── README.md                   # Project documentation
```

## Installation

To set up the project, you need to install the required dependencies. You can do this by running:

```
pip install -r requirements.txt
```

Make sure you have **Tesseract OCR** and **Poppler** installed on your system:

- **Tesseract OCR:**  
  Download and install from [Tesseract OCR GitHub](https://github.com/tesseract-ocr/tesseract).

- **Poppler:**  
  Poppler is required for converting PDF pages to images.  
  - **Windows:** Download the latest Poppler for Windows from [poppler-windows releases](https://github.com/oschwartz10612/poppler-windows/releases/), extract it, and add the `bin` folder to your system PATH.
  - **macOS:** Install via Homebrew: `brew install poppler`
  - **Linux:** Install via your package manager, e.g., `sudo apt-get install poppler-utils`

## Usage

1. Place your PDF files in a designated folder.
2. Run the application using the following command:

```
python src/main.py
```

3. The application will extract text from the PDF, process it with the AI model, and save the structured information into an Excel file.

## Functionality

- **Text Extraction**: Uses Tesseract OCR to extract text from PDF files.
- **AI Processing**: Interacts with the Ollama AI model to extract relevant information from the text.
- **Excel Output**: Writes the structured information into an Excel file for easy access and analysis.

## Contributing

Contributions are welcome! Please feel free to submit a pull request or open an issue for any enhancements or bug fixes.

## License

This project is licensed under the MIT License. See the LICENSE file for more details.