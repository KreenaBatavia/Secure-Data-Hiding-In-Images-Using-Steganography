import cv2
import numpy as np

def encrypt_message(image_path, message, password):
    img = cv2.imread(image_path)  # Load the image

    if img is None:
        print("Error: Could not load image.")
        return

    height, width, _ = img.shape  # Get image dimensions

    # Ensure the message fits inside the image
    if len(message) > height * width:
        print("Error: Message is too long for the image.")
        return

    print(f"Image size: {width}x{height}, Max chars: {height * width}")
    
    # Store message length in the first pixel (for proper decryption)
    img[0, 0, 0] = len(message)

    n, m, z = 0, 1, 0  # Start from (0,1) to avoid overwriting message length

    for char in message:
        img[n, m, z] = ord(char)  # Store ASCII value
        n = (n + 1) % height
        m = (m + 1) % width
        z = (z + 1) % 3  # Cycle through RGB channels

    # Save the encrypted image as PNG (to prevent compression artifacts)
    encrypted_image_path = "encryptedImage.png"
    cv2.imwrite(encrypted_image_path, img)
    print(f"Encrypted image saved as {encrypted_image_path}")

# User input
image_path = "mypic.jpg"  # Input image
message = input("Enter secret message: ")
password = input("Enter a passcode: ")

# Encrypt and save
encrypt_message(image_path, message, password)
