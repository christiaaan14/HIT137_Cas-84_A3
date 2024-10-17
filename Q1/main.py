import tkinter as tk
from tkinter import messagebox, ttk
from translator import FilipinoTranslator
from error_handler import TranslationError

# Main Tkinter Application
class TranslationApp(tk.Tk):
    def __init__(self):
        super().__init__()

        # Basic window setup
        self.title("English to Filipino Translation App")
        self.geometry("500x400")
        self.config(bg="#f0f0f0")

        # Adding more polish and improving the layout
        self.create_widgets()

    def create_widgets(self):
        # Header Label with custom font and styling
        self.header_label = tk.Label(self, text="English to Filipino Translation App", font=("Helvetica", 18, "bold"), bg="#34495e", fg="white", pady=20)
        self.header_label.pack(fill=tk.X)

        # Input label with spacing and better alignment
        self.input_label = tk.Label(self, text="Enter text to translate:", font=("Arial", 12), bg="#f0f0f0", pady=10)
        self.input_label.pack(pady=10)

        # Input Entry box with larger width and placeholder hint
        self.input_text = tk.Entry(self, width=50, font=("Arial", 12), borderwidth=2, relief="solid")
        self.input_text.pack(pady=10)

        # Translate button styled with ttk for better appearance
        self.translate_button = ttk.Button(self, text="Translate", command=self.perform_translation)
        self.translate_button.pack(pady=10)

        # Result label placeholder with formatting
        self.result_label = tk.Label(self, text="", font=("Arial", 12), bg="#f0f0f0", pady=10)
        self.result_label.pack(pady=20)

        # Status bar for error/status messages
        self.status_label = tk.Label(self, text="Ready", font=("Arial", 10), bg="#d5dbdb", fg="black", anchor="w")
        self.status_label.pack(side=tk.BOTTOM, fill=tk.X)

    # Method override to handle translation
    def perform_translation(self):
        user_input = self.input_text.get()
        translator = FilipinoTranslator()

        try:
            # Error handling for empty input
            if not user_input:
                raise TranslationError("Input cannot be empty!")

            # Perform translation and update the result label
            translated_text = translator.translate(user_input)
            self.result_label.config(text=f"Translated Text: {translated_text}")
            self.status_label.config(text="Translation Successful", fg="green")

        except TranslationError as e:
            messagebox.showerror("Translation Error", str(e))
            self.status_label.config(text="Translation Failed", fg="red")


if __name__ == "__main__":
    app = TranslationApp()
    app.mainloop()
