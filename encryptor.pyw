from cryptography.fernet import Fernet
from tkinter import *

file = open('key.key', 'rb')
key = file.read()
file.close()

fernet = Fernet(key)


def decrypt(text):
    pass


def encrypt(text):
    encrypted = fernet.encrypt(text.encode())
    sentence_entry.delete(0, END)
    sentence_entry.insert(0, encrypted.decode())


root = Tk()
root.title('Encryptor/Decryptor')

shit_label = Label(root, text='Enter your sentence', font=('Arial', 14))
shit_label.grid(row=0, column=0, sticky=N)

sentence_entry = Entry(root, width=35)
sentence_entry.grid(row=1, column=0, columnspan=2)

encrypt_button = Button(root, bg='grey', fg='white',
                        text='ENCRYPT', font=('Arial', 14), command=lambda: encrypt(sentence_entry.get()))
encrypt_button.grid(row=2, column=0)

decrypt_button = Button(root, bg='grey', fg='white',
                        text='DECRYPT', font=('Arial', 14))
decrypt_button.grid(row=2, column=1)


root.mainloop()
