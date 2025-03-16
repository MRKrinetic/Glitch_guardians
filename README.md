# AI-Powered OCR, Translation, and Distance Calculator

This application combines Optical Character Recognition (OCR), machine translation, and distance calculation capabilities into a user-friendly Streamlit web interface.

## Features

- **OCR (Optical Character Recognition)**
  - Upload and process images containing handwritten or printed text
  - Extract text from images using Tesseract OCR
  - Support for various image formats (JPG, PNG, JPEG)

- **Translation**
  - Translate text between multiple languages (English, Hindi, Marathi)
  - Powered by Google Translate API
  - Fine-tuned translation model for English to Marathi translations

- **Distance Calculation**
  - Calculate distance between two locations
  - Get estimated travel duration
  - Powered by GoMaps.pro API

## Setup Instructions

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd <repository-name>
   ```

2. **Create and activate a virtual environment**
   ```bash
   python -m venv venv
   # On Windows
   .\venv\Scripts\activate
   # On Unix or MacOS
   source venv/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Install Tesseract OCR**
   - Download and install Tesseract OCR from: https://github.com/UB-Mannheim/tesseract/wiki
   - Ensure the installation path matches the one in the code (default: `C:\Program Files\Tesseract-OCR\tesseract.exe`)

5. **Set up API Keys**
   - Replace the GoMaps.pro API key in `streamlit(app).py` with your own key

## Usage

1. **Start the application**
   ```bash
   streamlit run "streamlit(app).py"
   ```

2. **Using the Application**
   - Upload an image or enter text manually
   - For OCR: Use the file uploader to process images
   - For translation: Select source and target languages
   - For distance calculation: Enter source and destination locations

## Project Structure

- `streamlit(app).py`: Main application file with Streamlit interface
- `model.py`: Translation model implementation
- `fine_tune.py`: Model fine-tuning script
- `ocr.py`: OCR functionality
- `data.csv`: Training data for model fine-tuning
- `requirements.txt`: Project dependencies
- `venv/`: Virtual environment directory

## Dependencies

- Python 3.8+
- Streamlit
- PyTesseract
- OpenCV
- Transformers
- Torch
- Pandas
- And more (see requirements.txt)

## Notes

- The translation model is fine-tuned specifically for English to Marathi translation
- Internet connection required for translation and distance calculation features
- Make sure to have sufficient system resources for running the ML models

## License

[Your License Here]

## Contributing

Feel free to submit issues and enhancement requests!
