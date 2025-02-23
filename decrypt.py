import cv2

def decrypt_message(image_path, correct_password):
    img = cv2.imread(image_path)  # Load the encrypted image

    if img is None:
        print("Error: Could not load image.")
        return

    height, width, _ = img.shape

    # Retrieve message length from the first pixel
    message_length = img[0, 0, 0]

    # Ask user for decryption password
    entered_password = input("Enter passcode for Decryption: ")
    if entered_password != correct_password:
        print("YOU ARE NOT AUTHORIZED!")
        return

    decrypted_message = ""
    n, m, z = 0, 1, 0  # Start from (0,1) to match encryption

    for _ in range(message_length):
        decrypted_message += chr(img[n, m, z])  # Convert pixel value to character
        n = (n + 1) % height
        m = (m + 1) % width
        z = (z + 1) % 3  # Cycle through RGB channels

    print("\n🔓 Decrypted Message:", decrypted_message)

# User input
image_path = "encryptedImage.png"  # Encrypted image path
correct_password = input("Enter the correct passcode used in encryption: ")

# Decrypt and display message
decrypt_message(image_path, correct_password)
