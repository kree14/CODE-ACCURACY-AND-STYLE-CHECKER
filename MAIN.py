import tkinter as tk
from tkinter import ttk, scrolledtext, messagebox
from analysis import analyze_python_code, ai_improve_code

class CodeCheckerApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Code Accuracy & Style Checker")
        self.geometry("900x600")
        self.language = tk.StringVar(value="Python")

        # Language selector
        lang_frame = ttk.Frame(self)
        lang_frame.pack(fill=tk.X, padx=10, pady=5)
        ttk.Label(lang_frame, text="Language:").pack(side=tk.LEFT)
        ttk.Combobox(lang_frame, textvariable=self.language, values=["Python", "Java"], width=10).pack(side=tk.LEFT)

        # Code input panel
        input_frame = ttk.LabelFrame(self, text="Paste your code here")
        input_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=5)
        self.code_input = scrolledtext.ScrolledText(input_frame, height=15, font=("Consolas", 12))
        self.code_input.pack(fill=tk.BOTH, expand=True)

        # Action buttons
        btn_frame = ttk.Frame(self)
        btn_frame.pack(fill=tk.X, padx=10, pady=5)
        ttk.Button(btn_frame, text="Check Code", command=self.check_code).pack(side=tk.LEFT, padx=5)
        ttk.Button(btn_frame, text="Improve with AI", command=self.improve_code).pack(side=tk.LEFT, padx=5)

        # Output/results panel
        output_frame = ttk.LabelFrame(self, text="Results")
        output_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=5)
        self.results_output = scrolledtext.ScrolledText(output_frame, height=10, font=("Consolas", 12), state=tk.DISABLED)
        self.results_output.pack(fill=tk.BOTH, expand=True)

    def check_code(self):
        code = self.code_input.get("1.0", tk.END).strip()
        lang = self.language.get()
        if not code:
            messagebox.showwarning("Input required", "Please enter some code.")
            return
        if lang != "Python":
            self.display_results("Java support coming soon!")
            return
        results = analyze_python_code(code)
        self.display_results(results)

    def improve_code(self):
        code = self.code_input.get("1.0", tk.END).strip()
        lang = self.language.get()
        if not code:
            messagebox.showwarning("Input required", "Please enter some code.")
            return
        if lang != "Python":
            self.display_results("Java support coming soon!")
            return
        improved_code = ai_improve_code(code)
        self.code_input.delete("1.0", tk.END)
        self.code_input.insert(tk.END, improved_code)
        messagebox.showinfo("AI Improvement", "Code improved! Check the input panel.")

    def display_results(self, text):
        self.results_output.config(state=tk.NORMAL)
        self.results_output.delete("1.0", tk.END)
        self.results_output.insert(tk.END, text)
        self.results_output.config(state=tk.DISABLED)

if __name__ == "__main__":
    app = CodeCheckerApp()
    app.mainloop()
