import cv2
import os
import tkinter as tk
from tkinter import ttk, simpledialog, messagebox
from ttkthemes import ThemedTk

def encrypt_image(image_path, message, password):
    img = cv2.imread(image_path)
    key = generate_key(password)

    n, m, z = 0, 0, 0
    for char in message:
        img[n, m, z] ^= key
        n += 1
        m += 1
        z = (z + 1) % 3

    encrypted_path = "Encryptedmsg.jpg"
    cv2.imwrite(encrypted_path, img)
    os.system(f"start {encrypted_path}")

def decrypt_image(encrypted_image_path, password):
    img = cv2.imread(encrypted_image_path)
    key = generate_key(password)

    n, m, z = 0, 0, 0
    decrypted_message = ""
    for _ in range(len(password)):
        for _ in range(3):
            decrypted_message += chr(img[n, m, z] ^ key)
            n += 1
            m += 1
            z = (z + 1) % 3

    return decrypted_message

def generate_key(password):
    key = sum(map(ord, password)) % 256
    return key

def encrypt_button_clicked():
    message = simpledialog.askstring("Input", "Enter secret message:")
    password = simpledialog.askstring("Input", "Enter encryption password:")

    if message and password:
        encrypt_image("mypic.jpg", message, password)
        messagebox.showinfo("Success", "Encryption successful!")
    else:
        messagebox.showerror("Error", "Message and password are required.")

def decrypt_button_clicked():
    password_decrypt = simpledialog.askstring("Input", "Enter decryption password:")

    if password_decrypt:
        decrypted_message = decrypt_image("Encryptedmsg.jpg", password_decrypt)
        if decrypted_message:
            messagebox.showinfo("Decryption", f"Decrypted message: {decrypted_message}")
        else:
            messagebox.showerror("Error", "Decryption failed. Invalid password.")
    else:
        messagebox.showerror("Error", "Decryption password is required.")

def main():
    root = ThemedTk(theme="arc")  # Choose your preferred theme

    root.title("Steganography Tool")
    root.geometry("400x200")

    # Create labels
    label = ttk.Label(root, text="Steganography Tool", font=("Helvetica", 16))
    label.grid(row=0, column=1, pady=10)

    # Create buttons
    encrypt_button = ttk.Button(root, text="Encrypt", command=encrypt_button_clicked)
    encrypt_button.grid(row=1, column=0, padx=20, pady=10)

    decrypt_button = ttk.Button(root, text="Decrypt", command=decrypt_button_clicked)
    decrypt_button.grid(row=1, column=2, padx=20, pady=10)

    root.mainloop()

if __name__ == "__main__":
    main()
