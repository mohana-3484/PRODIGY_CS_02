from PIL import Image

# Encrypt Image
def encrypt_image(input_image, output_image, key):
    img = Image.open(input_image).convert("RGB")
    pixels = img.load()

    width, height = img.size

    for x in range(width):
        for y in range(height):
            r, g, b = pixels[x, y]

            r = (r + key) % 256
            g = (g + key) % 256
            b = (b + key) % 256

            pixels[x, y] = (r, g, b)

    img.save(output_image)
    print("Image Encrypted Successfully!")


# Decrypt Image
def decrypt_image(input_image, output_image, key):
    img = Image.open(input_image).convert("RGB")
    pixels = img.load()

    width, height = img.size

    for x in range(width):
        for y in range(height):
            r, g, b = pixels[x, y]

            r = (r - key) % 256
            g = (g - key) % 256
            b = (b - key) % 256

            pixels[x, y] = (r, g, b)

    img.save(output_image)
    print("Image Decrypted Successfully!")


print("\n===== IMAGE ENCRYPTION TOOL =====")

choice = input("Encrypt or Decrypt (E/D): ").upper()

if choice == "E":
    encrypt_image("input.jpg", "encrypted.png", 50)

elif choice == "D":
    decrypt_image("encrypted.png", "decrypted.png", 50)

else:
    print("Invalid Choice! Please enter E or D.")