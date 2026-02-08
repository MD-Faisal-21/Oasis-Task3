#Random Password Generator
import tkinter as tk
from tkinter import messagebox
import random
import string
import pyperclip


class PasswordGeneratorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Secure Password Generator")
        self.root.geometry("460x420")
        self.root.resizable(False, False)

        self.build_ui()

    def build_ui(self):
        title = tk.Label(
            self.root,
            text="Random Password Generator",
            font=("Segoe UI", 18, "bold")
        )
        title.pack(pady=12)

        options_frame = tk.Frame(self.root)
        options_frame.pack(pady=10)

        tk.Label(options_frame, text="Password Length:", font=("Segoe UI", 11)).grid(row=0, column=0, sticky="w")
        self.length_var = tk.IntVar(value=12)
        self.length_slider = tk.Scale(
            options_frame,
            from_=6,
            to=64,
            orient="horizontal",
            variable=self.length_var,
            length=250
        )
        self.length_slider.grid(row=0, column=1, pady=5)

        self.use_letters = tk.BooleanVar(value=True)
        self.use_digits = tk.BooleanVar(value=True)
        self.use_symbols = tk.BooleanVar(value=True)
        self.exclude_similar = tk.BooleanVar(value=False)

        tk.Checkbutton(options_frame, text="Include Letters (A–Z, a–z)", variable=self.use_letters).grid(row=1, column=0, columnspan=2, sticky="w")
        tk.Checkbutton(options_frame, text="Include Numbers (0–9)", variable=self.use_digits).grid(row=2, column=0, columnspan=2, sticky="w")
        tk.Checkbutton(options_frame, text="Include Symbols", variable=self.use_symbols).grid(row=3, column=0, columnspan=2, sticky="w")
        tk.Checkbutton(options_frame, text="Exclude Similar Characters (O, 0, l, 1)", variable=self.exclude_similar).grid(row=4, column=0, columnspan=2, sticky="w")

        self.output_box = tk.Entry(self.root, width=45, font=("Consolas", 11))
        self.output_box.pack(pady=15)

        button_frame = tk.Frame(self.root)
        button_frame.pack(pady=5)

        tk.Button(button_frame, text="Generate", width=14, command=self.generate_password).grid(row=0, column=0, padx=6)
        tk.Button(button_frame, text="Copy", width=14, command=self.copy_password).grid(row=0, column=1, padx=6)
        tk.Button(button_frame, text="Clear", width=14, command=self.clear_output).grid(row=0, column=2, padx=6)

        note = tk.Label(
            self.root,
            text="Tip: Longer passwords with mixed characters are more secure.",
            font=("Segoe UI", 9)
        )
        note.pack(pady=12)

    def build_character_pool(self):
        pool = ""

        if self.use_letters.get():
            pool += string.ascii_letters
        if self.use_digits.get():
            pool += string.digits
        if self.use_symbols.get():
            pool += "!@#$%^&*()-_=+[]{};:,.<>?/"

        if self.exclude_similar.get():
            for ch in "O0l1I":
                pool = pool.replace(ch, "")

        return pool

    def generate_password(self):
        length = self.length_var.get()
        pool = self.build_character_pool()

        if not pool:
            messagebox.showerror("Selection Error", "Please select at least one character type.")
            return

        password = "".join(random.choice(pool) for _ in range(length))
        self.output_box.delete(0, tk.END)
        self.output_box.insert(0, password)

    def copy_password(self):
        password = self.output_box.get()
        if not password:
            messagebox.showwarning("No Password", "Generate a password first.")
            return
        pyperclip.copy(password)
        messagebox.showinfo("Copied", "Password copied to clipboard.")

    def clear_output(self):
        self.output_box.delete(0, tk.END)


if __name__ == "__main__":
    root = tk.Tk()
    app = PasswordGeneratorApp(root)
    root.mainloop()
