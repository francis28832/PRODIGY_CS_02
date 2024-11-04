from PIL import Image
import numpy as np

# ASCII Art Header
print(r"""
   ____                                 _____        _    _______          _ 
  / ___|___  _ __ ___  _ __   ___ _   _| ____|_  __ / \  | ____| |   _  __| |
 | |   / _ \| '_ ` _ \| '_ \ / _ \ | | |  _| \ \/ // _ \ |  _| | | | |/ _` |
 | |__| (_) | | | | | | |_) |  __/ |_| | |___ >  < / ___ \| |___| |_| | (_| |
  \____\___/|_| |_| |_| .__/ \___|\__, |_____/_/\_/_/   \_\_____|\__,_|\__,_|
                     |_|        |___/                                        
""")
print("Welcome to the Image Encryption Tool!\n")

def encrypt_image(image_path, key):
    # Load the image
    img = Image.open(image_path)
    img_array = np.array(img)

    # Perform encryption by adding the key value to each pixel
    encrypted_array = (img_array + key) % 256  # Ensures pixel values stay between 0-255
    encrypted_img = Image.fromarray(encrypted_array.astype('uint8'))

    # Save encrypted image
    encrypted_img.save("encrypted_image.png")
    print("\nImage encrypted and saved as 'encrypted_image.png'")

def decrypt_image(encrypted_image_path, key):
    # Load the encrypted image
    img = Image.open(encrypted_image_path)
    img_array = np.array(img)

    # Perform decryption by subtracting the key value from each pixel
    decrypted_array = (img_array - key) % 256  # Ensures pixel values stay between 0-255
    decrypted_img = Image.fromarray(decrypted_array.astype('uint8'))

    # Save decrypted image
    decrypted_img.save("decrypted_image.png")
    print("\nImage decrypted and saved as 'decrypted_image.png'")

def main():
    print("=" * 60)
    choice = input("Type 'e' to encrypt or 'd' to decrypt an image: ").lower()
    image_path = input("Enter the path of the image: ")
    key = int(input("Enter a numerical key for encryption/decryption: "))
    
    if choice == 'e':
        encrypt_image(image_path, key)
    elif choice == 'd':
        decrypt_image(image_path, key)
    else:
        print("\nInvalid option, please choose 'e' or 'd'.")
    print("=" * 60)

if __name__ == "__main__":
    main()

