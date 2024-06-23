from PIL import Image

def encrypt_image(image_path, encrypted_path):
    img = Image.open("C:\\Users\\HP\\Downloads\\ff.jpeg")
    width, height = img.size
    encrypted_img = Image.new('RGB', (width, height))
    for x in range(width):
        for y in range(height):
            pixel = img.getpixel((x, y))
            encrypted_pixel = (pixel[2], pixel[1], pixel[0])
            encrypted_img.putpixel((x, y), encrypted_pixel)
    encrypted_img.save(encrypted_path)
    print(f"Image encrypted and saved as {encrypted_path}")

def decrypt_image(encrypted_path, decrypted_path):
    encrypted_img = Image.open(encrypted_path)
    width, height = encrypted_img.size
    decrypted_img = Image.new('RGB', (width, height))
    for x in range(width):
        for y in range(height):
            encrypted_pixel = encrypted_img.getpixel((x, y))
            decrypted_pixel = (encrypted_pixel[2], encrypted_pixel[1], encrypted_pixel[0])
            decrypted_img.putpixel((x, y), decrypted_pixel)
    decrypted_img.save(decrypted_path)
    print(f"Image decrypted and saved as {decrypted_path}")

if __name__ == "__main__":
    encrypt_image('input_image.jpg', 'encrypted_image.jpg')
    decrypt_image('encrypted_image.jpg', 'decrypted_image.jpg')
