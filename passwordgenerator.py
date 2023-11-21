import tkinter as tk
from tkinter import Label, Entry, Button, Text, Scrollbar
import random
import string

class PasswordManager:
    def __init__(self, master):
        self.master = master
        self.master.title("Password Manager")

        self.label_tag = Label(master, text="Tag:")
        self.label_tag.grid(row=0, column=0, padx=10, pady=10)

        self.entry_tag = Entry(master)
        self.entry_tag.grid(row=0, column=1, padx=10, pady=10)

        self.label_password = Label(master, text="Generated Password:")
        self.label_password.grid(row=1, column=0, padx=10, pady=10)

        self.entry_password = Entry(master, state='readonly')
        self.entry_password.grid(row=1, column=1, padx=10, pady=10)

        self.generate_button = Button(master, text="Generate Password", command=self.generate_password)
        self.generate_button.grid(row=2, column=0, columnspan=2, pady=10)

        self.save_button = Button(master, text="Save Password", command=self.save_password)
        self.save_button.grid(row=3, column=0, columnspan=2, pady=10)

        self.retrieve_button = Button(master, text="Retrieve Passwords", command=self.retrieve_passwords)
        self.retrieve_button.grid(row=4, column=0, columnspan=2, pady=10)

        self.text_display = Text(master, height=10, width=30, wrap=tk.WORD)
        self.text_display.grid(row=5, column=0, columnspan=2, pady=10)

        self.scrollbar = Scrollbar(master, command=self.text_display.yview)
        self.scrollbar.grid(row=5, column=2, sticky='nsew')
        self.text_display.config(yscrollcommand=self.scrollbar.set)

    def generate_password(self):
        length = 12
        characters = string.ascii_letters + string.digits + string.punctuation
        password = ''.join(random.choice(characters) for i in range(length))
        self.entry_password.config(state='normal')
        self.entry_password.delete(0, 'end')
        self.entry_password.insert(0, password)
        self.entry_password.config(state='readonly')

    def save_password(self):
        tag = self.entry_tag.get()
        password = self.entry_password.get()

        if tag and password:
            with open("passwords.txt", "a") as file:
                file.write(f"{tag}: {password}\n")
            self.entry_tag.delete(0, 'end')
            self.entry_password.config(state='normal')
            self.entry_password.delete(0, 'end')
            self.entry_password.config(state='readonly')

    def retrieve_passwords(self):
        self.text_display.delete(1.0, tk.END)
        try:
            with open("passwords.txt", "r") as file:
                passwords = file.readlines()
                for idx, password in enumerate(passwords, start=1):
                    self.text_display.insert(tk.END, f"{idx}. {password}")
                    delete_button = Button(self.master, text=f"Delete {idx}", command=lambda idx=idx: self.delete_password(idx))
                    delete_button.grid(row=idx+5, column=0, columnspan=2, pady=2)
        except FileNotFoundError:
            self.text_display.insert(tk.END, "No passwords saved yet.")

    def delete_password(self, idx):
        try:
            with open("passwords.txt", "r") as file:
                lines = file.readlines()
            with open("passwords.txt", "w") as file:
                for i, line in enumerate(lines, start=1):
                    if i != idx:
                        file.write(line)
            self.retrieve_passwords()
        except FileNotFoundError:
            self.text_display.insert(tk.END, "No passwords saved yet.")

if __name__ == "__main__":
    root = tk.Tk()
    app = PasswordManager(root)
    root.mainloop()
