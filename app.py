#!/usr/bin/env python3

"""
OCR Multioption question and answer it with ChatGPT

This app converts an image to text using OCR and then processes it with ChatGPT.

Author: Vladislav Cernega
Version: 1.0
Date: 25-09-2023
"""

import json
import sys
from PIL import Image, ImageGrab
import pytesseract
import openai

CONFIG_PATH = "config.json"

with open(CONFIG_PATH, "r") as f:
    config = json.load(f)

openai.api_key = config["openai"]["api_key"]


def beautify_text(text):
    """Beautify the given text using OpenAI GPT-3.5 Turbo Instruct model."""
    prompt = (
        "Enhance the readability of this text by eliminating non-readable characters, "
        "unnecessary quotations, special characters, and parentheses. \n" + text
    )
    response = openai.Completion.create(
        model="gpt-3.5-turbo-instruct",
        prompt=prompt,
        temperature=1,
        max_tokens=256,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    return response.choices[0].text.strip()


def ask_gpt(prompt):
    """Generate a response for the given prompt using OpenAI GPT-3.5 Turbo Instruct model."""
    response = openai.Completion.create(
        model="gpt-3.5-turbo-instruct",
        prompt=prompt,
        temperature=1,
        max_tokens=256,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    return response.choices[0].text.strip()


def process_image(debug_mode):
    """Process an image, extract and beautify text, and provide user options for further actions."""
    if debug_mode:
        print("Welcome to OCR")
        option = input("Please select an option (1: Image on Disk, 2: Image from Clipboard): ")

        if option == "1":
            image_path = input("Enter the image path: ")
            img = Image.open(image_path)
        elif option == "2":
            img = ImageGrab.grabclipboard()
        else:
            print("Invalid option. Exiting.")
            sys.exit()

        text = pytesseract.image_to_string(img)
        text = beautify_text(text)

        option = input("Select an option (1: Print, 2: Save, 3: Process with ChatGPT): ")

        if option == "1":
            print(text)
        elif option == "2":
            file_path = input("Enter the file path: ")
            with open(file_path, "w") as file:
                file.write(text)
        elif option == "3":
            print(f"OCR Text: {text.splitlines()[0]}")
            print(f"Answer: {ask_gpt(text)}")
    else:
        img = ImageGrab.grabclipboard()
        text = pytesseract.image_to_string(img)
        text = beautify_text(text)
        print(f"OCR Text: {text}\n\nAnswer: {ask_gpt(text)}")


def main():
    debug_mode = "--debug" in sys.argv
    process_image(debug_mode)


if __name__ == "__main__":
    main()

