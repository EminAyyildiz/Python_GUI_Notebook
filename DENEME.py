import tkinter as tk
from tkinter import filedialog, messagebox


class Notebook:
    def __init__(self, master):
        self.master = master
        master.title("Notebook---Written by EMİN AYYILDIZ")
        self.text_area = tk.Text(master)
        self.text_area.configure(bg="gray")
        self.text_area.pack(fill=tk.BOTH, expand=True)
        self.setup_but()

    def setup_but(self):
        new_file_button = tk.Button(self.master, text="New File", command=self.new_file)
        new_file_button.pack(side=tk.LEFT, padx=5, pady=5)
        save_but = tk.Button(self.master, text="Save", command=self.save_file, bg="blue")
        save_but.pack(side=tk.LEFT, padx=5, pady=5)
        delete_but = tk.Button(self.master, text="Delete", command=self.delete_file, bg="blue")
        delete_but.pack(side=tk.LEFT, padx=5, pady=5)

    def new_file(self):
        if len(self.text_area.get("1.0", tk.END)) > 1:
            msg_box = messagebox.askquestion('WARNING', 'Do you want to save what you wrote?')
            if msg_box == 'yes':
                self.save_file()
            else:
                self.text_area.delete("1.0", tk.END)

    def save_file(self):
        file_path = filedialog.asksaveasfilename(defaultextension=".txt")
        if file_path:
            with open(file_path, "w") as file:
                file.write(self.text_area.get("1.0", tk.END))

    def delete_file(self):
        self.text_area.delete("1.0", tk.END)


root = tk.Tk()
notepad = Notebook(root)
root.mainloop()
