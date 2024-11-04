# Image Encryption and Decryption Tool

## Overview
This project is a Python-based tool that encrypts and decrypts images using pixel manipulation techniques. The tool allows users to input an image file and apply basic mathematical operations to each pixel for encryption and decryption, ensuring a simple and educational approach to understanding image data manipulation.

## Features
- **Encrypt Image**: Modify pixel values with a numerical key to create an encrypted version of an image.
- **Decrypt Image**: Reverse the pixel modification process to retrieve the original image.
- **User Interface**: Simple command-line interface for ease of use.
- **ASCII Art**: Engaging visual presentation when the tool runs.

## How It Works
- **Encryption**: Adds a user-defined key to the pixel values in the image and ensures they remain within the 0-255 range using modulo operation.
- **Decryption**: Subtracts the user-defined key to revert the image to its original state, maintaining pixel values within valid limits.

## Prerequisites
- Python 3.x
- Pillow library (PIL)

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/francis28832/PRODIGY_CS_02.git
   cd your-repository
