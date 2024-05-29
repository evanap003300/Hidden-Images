# PROGRAMMING: Hidden Images
# AUTHOR: Evan Phillips
# DATE DUE: 3/25/24
# DATE SUBMITTED: 3/25/24
# COURSE TITLE: CSC 110: Python for Scientists
# DESCRIPTION: This project disiphers hidden messages in images

# UNCOMMENT FOR GRAPHICS
# from graphics import *

def decryptA01(r, g, b):
    """
    Decrypts pixel values using Algorithm 1.

    Args:
        r (int): The red component of the pixel.
        g (int): The green component of the pixel.
        b (int): The blue component of the pixel.

    Returns:
        tuple: The decrypted red, green, and blue components.
    """
    # Process
    return r * 10, r * 10, r * 10


def decryptA02(r, g, b):
    """
    Decrypts pixel values using Algorithm 2.

    Args:
        r (int): The red component of the pixel.
        g (int): The green component of the pixel.
        b (int): The blue component of the pixel.

    Returns:
        tuple: The decrypted red, green, and blue components.
    """
    # Process
    return 0, b * 20, g * 20


def decryptA03(r, g, b):
    """
    Decrypts pixel values using Algorithm 3.

    Args:
        r (int): The red component of the pixel.
        g (int): The green component of the pixel.
        b (int): The blue component of the pixel.

    Returns:
        tuple: The decrypted red, green, and blue components.
    """
    # Process
    if (b < 16):
        blue = b * 16
    else:
        blue = 255
    red = blue
    green = blue
    return red, green, blue


def decryptA04(r, g, b):
    """
    Decrypts pixel values using Algorithm 4.

    Args:
        r (int): The red component of the pixel.
        g (int): The green component of the pixel.
        b (int): The blue component of the pixel.

    Returns:
        tuple: The decrypted red, green, and blue components.
    """
    #Process
    # Undo the subtraction
    red = (255 - r) % 3
    green = (170 - g) % 5
    blue = (85 - b) % 17
    
    #Process
    # Recover the original red value
    redOriginal = (red * 85 + green * 51 + blue * 120) % 255
    
    #Process
    # Convert to grayscale
    return redOriginal, redOriginal, redOriginal

# Helper method for decryptA05
def decrypt_value(value):
    """
    Decrypts a single color component value.

    Args:
        value (int): The color component value to decrypt.

    Returns:
        int: The decrypted color component value.
    """
    #Process
    # Convert value to binary string with leading zeros
    binary_string = format(value, '08b')

    #Process
    # Take the last 4 bits as a substring
    substring = binary_string[-4:]

    #Process
    # Concatenate '0000' to the substring
    new_byte = substring + "0000"

    #Process
    # Convert the binary string back to an integer
    new_value = int(new_byte, 2)

    #Process
    return new_value


def decryptA05(r, g, b):
    """
    Decrypts pixel values using Algorithm 5.

    Args:
        r (int): The red component of the pixel.
        g (int): The green component of the pixel.
        b (int): The blue component of the pixel.

    Returns:
        tuple: The decrypted red, green, and blue components.
    """
    #Process
    decrypted_red = decrypt_value(r)
    decrypted_green = decrypt_value(g)
    decrypted_blue = decrypt_value(b)
    return decrypted_red, decrypted_green, decrypted_blue


def graphics(width, height, image_data, algorithm):
    """
    Display input and output images using the selected decryption algorithm.

    Args:
        width (int): Width of the image.
        height (int): Height of the image.
        image_data (list): List containing image pixel data.
        algorithm (str): The selected decryption algorithm.
    """
    # Initialize
    inputWin = GraphWin("INPUT", width, height)
    outputWin = GraphWin("OUTPUT", width, height)

    # Initialize
    displayInputImage = Image(Point(width / 2, height / 2), '')
    displayOutputImage = Image(Point(width / 2, height / 2), '')
    
    # Loop through the image data by 3 to extract RGB values for each pixel
    for i in range(0, len(image_data), 3):
        # Process
        red = int(image_data[i])
        green = int(image_data[i + 1])
        blue = int(image_data[i + 2])
        
        # Process
        # Calculate the row and column indices for setting pixels
        row = i // 3 % width
        col = i // (3 * width)
        
        # Process
        # Set pixels in the input display image
        displayInputImage.setPixel(row, col, color_rgb(red, green, blue))

        # Process
        # Decrypt pixel colors according to the selected algorithm
        if algorithm == "1":
            red, green, blue = decryptA01(red, green, blue)
        elif algorithm == "2":
            red, green, blue = decryptA02(red, green, blue)
        elif algorithm == "3":
            red, green, blue = decryptA03(red, green, blue)
        elif algorithm == "4":
            red, green, blue = decryptA04(red, green, blue)
        else:
            red, green, blue = decryptA05(red, green, blue)
        
        # Process
        # Set pixels in the output display image
        displayOutputImage.setPixel(row, col, color_rgb(red, green, blue))
    
    # Output
    # Draw images centered in the windows
    displayInputImage.draw(inputWin)
    displayOutputImage.draw(outputWin)


def main():
    """
    Main function to run the program.
    """
    # Input
    input_file_name = input("Enter the filename of the image that you want to decrypt: ")
    algorithm = input("Enter the decryption algorithm you want to use (1, 2, 3, 4, or 5): ")
    
    # Process
    infile = open(input_file_name, "r");
    
    # Process
    line1 = infile.readline();
    
    # Output
    print(line1, end="")
    
    # Process
    line2 = infile.readline();
    
    # Output
    print(line2, end="");
    
    # Process
    line3 = infile.readline();
    
    # Output
    print(line3, end="");
    
    # Process
    line4 = infile.readline()
    
    # Output
    print(line4, end="");
    
    # Process
    output_file_name = input_file_name[:-4] + "_OutA0" + algorithm + ".ppm"
    
    # Process
    outfile = open(output_file_name, "w")
    
    # Output
    print(line1, file = outfile, end = "")
    print("# Evan Phillips 03/11/2024", file = outfile)
    print(line3, file = outfile, end = "")
    print(line4, file = outfile, end = "")
    
    # Process
    image_data = infile.read().split();
    
    # Loop through the image data by 3 to extract RGB values for each pixel
    for i in range(0, len(image_data), 3):
        # Process
        red = int(image_data[i])
        green = int(image_data[i+1]);
        blue = int(image_data[i+2]);
        
        # Process
        if (algorithm == "1"): 
            red, green, blue = decryptA01(red, green, blue)
        elif (algorithm == "2"): 
            red, green, blue = decryptA02(red, green, blue)
        elif (algorithm == "3"): 
            red, green, blue = decryptA03(red, green, blue)
        elif (algorithm == "4"): 
            red, green, blue = decryptA04(red, green, blue)
        else:
            red, green, blue = decryptA05(red, green, blue)
        
        # Output
        print(red, green, blue, file = outfile);
    
    # UNCOMMENT FOR GRAPHICS
    #width = int(line3[:3])
    #height = int(line3[4:])
    #graphics(width, height, image_data, algorithm)
    
    # Terminate
    infile.close();
    outfile.close();

# Run main()
if __name__ == "__main__":   
    main()