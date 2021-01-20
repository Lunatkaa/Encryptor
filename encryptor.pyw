from cryptography.fernet import Fernet
from tkinter import *
import pyperclip

file = open('key.key', 'rb')
key = file.read()
file.close()

fernet = Fernet(key)


def decrypt(text):
    decrypted = fernet.decrypt(text.encode())
    result_label['text'] = decrypted.decode()


def encrypt(text):
    encrypted = fernet.encrypt(text.encode())
    result_label['text'] = encrypted.decode()


def copy_to_clipboard():
    pyperclip.copy(result_label['text'])


root = Tk()
root.title('Encryptor/Decryptor')
root.resizable(height=False, width=False)

shit_label = Label(root, text='Enter your sentence', font=('Arial', 14))
shit_label.grid(row=0, column=2, sticky=N)

result_label = Label(root, font=('Arial', 14), wrap=300)
result_label.grid(row=3, column=2, sticky=S)

sentence_entry = Entry(root, width=50, font=('Arial', 14))
sentence_entry.grid(row=1, column=0, columnspan=4)

encrypt_button = Button(root, bg='grey', fg='white',
                        text='ENCRYPT', font=('Arial', 14), command=lambda: encrypt(sentence_entry.get()))
encrypt_button.grid(row=2, column=1, sticky=E)

decrypt_button = Button(root, bg='grey', fg='white',
                        text='DECRYPT', font=('Arial', 14), command=lambda: decrypt(sentence_entry.get()))
decrypt_button.grid(row=2, column=3, sticky=W)

copy_button = Button(root, bg='grey', fg='white',
                     text='COPY', font=('Arial', 14), command=copy_to_clipboard)
copy_button.grid(row=4, column=2)


root.mainloop()

# du huresniohn
