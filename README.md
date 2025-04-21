# Hidden Images

A Python program that deciphers hidden messages in images using various decryption algorithms.

## Overview

This project allows users to decrypt images containing hidden messages using five different decryption algorithms. The program reads an image file in PPM format, applies the selected decryption algorithm to transform the pixel values, and outputs a new image file with the revealed message.

## Features

- **Multiple Decryption Algorithms**: Implements 5 different decryption methods (A01-A05)
- **Image Processing**: Manipulates RGB values to reveal hidden content
- **Output Options**: 
  - Creates a new PPM file with the decrypted image
  - Optional graphical display of both input and output images (requires graphics.py)

## Requirements

- Python 3.x
- Optional: graphics.py library for visual display (commented out by default)

## Usage

1. Run the program:
   ```
   python hidden_images.py
   ```

2. When prompted, enter:
   - The filename of the image you want to decrypt (must be in PPM format)
   - The decryption algorithm you want to use (1, 2, 3, 4, or 5)

3. The program will:
   - Display basic information about the input file
   - Create a new output file with the decrypted image named: `[original_filename]_OutA0[algorithm_number].ppm`

## Decryption Algorithms

The program includes five different decryption methods:

1. **Algorithm 1**: Multiplies the red value by 10 and applies it to all channels
2. **Algorithm 2**: Sets red to 0, scales blue by 20, and scales green by 20
3. **Algorithm 3**: Scales blue values less than 16 by 16, otherwise sets to 255, and applies to all channels
4. **Algorithm 4**: Complex algorithm involving modulo operations and grayscale conversion
5. **Algorithm 5**: Bit manipulation algorithm that extracts the last 4 bits of each RGB component

## File Format

This program works with PPM (Portable Pixmap) format image files, which have the following structure:
- Line 1: Magic number (P3)
- Line 2: Comment line
- Line 3: Width and height of the image
- Line 4: Maximum color value
- Remaining lines: RGB triplets for each pixel

## Graphics Display (Optional)

The program includes a graphics display function that is commented out by default. To enable it:
1. Uncomment the import statement at the top: `from graphics import *`
2. Uncomment the graphics function call at the bottom of main()
3. Make sure you have the graphics.py library installed

## Author

Evan Phillips

## Course Information

- **Course**: CSC 110: Python for Scientists
- **Date**: March 25, 2024
