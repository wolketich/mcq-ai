# mcq-ai
Answer multiple choice question through ChatGPT-3.5

# OCR Multioption with ChatGPT

Convert images to text using OCR and process the extracted text with ChatGPT.

## Overview

This application allows users to:
- Convert images containing text into plain text using Optical Character Recognition (OCR).
- Beautify the extracted text using OpenAI's GPT-3.5 Turbo Instruct model.
- Process the text with ChatGPT to get answers or further insights.

## Features

- **Image Input**: Accepts images from both disk and clipboard.
- **Text Beautification**: Enhances the readability of the extracted text.
- **Interactive Mode**: In debug mode, users can choose various options like printing the text, saving it to a file, or processing it with ChatGPT.

## Requirements

- Python 3
- PIL (Python Imaging Library)
- pytesseract
- openai

## Setup

1. Clone the repository:
   ```bash
   git clone https://github.com/wolketich/mcq-ai/)https://github.com/wolketich/mcq-ai/
   ```

2. Navigate to the project directory:
   ```bash
   cd mcq-ai
   ```

3. Install the dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Set up the config.json file with your OpenAI API key:
   ```bash
    {
        "openai": {
            "api_key": "YOUR_API_KEY"
        }
    }
   ```

## Usage

1. Run the application:
   ```bash
   python3 app.py
   ```

   or run the application in debug-mode that allows interactive options:
   ```bash
   python3 app.py --debug
   ```

