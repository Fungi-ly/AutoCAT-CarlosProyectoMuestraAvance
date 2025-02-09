import tkinter as tk
from tkinter import filedialog, messagebox
import json

class JSONEditor:
    def __init__(self, master):
        self.master = master
        self.master.title("Editor de JSON")

        self.label = tk.Label(master, text="Ruta del archivo JSON:")
        self.label.pack()

        self.entry = tk.Entry(master, width=50)
        self.entry.pack()

        self.browse_button = tk.Button(master, text="Abrir", command=self.browse_file)
        self.browse_button.pack()

        self.text = tk.Text(master, width=80, height=20)
        self.text.pack()

        self.save_button = tk.Button(master, text="Guardar", command=self.save_file)
        self.save_button.pack()

    def browse_file(self):
        file_path = filedialog.askopenfilename(filetypes=[("JSON files", "*.json")])
        if file_path:
            self.entry.delete(0, tk.END)
            self.entry.insert(0, file_path)
            self.load_file(file_path)

    def load_file(self, file_path):
        try:
            with open(file_path, 'r') as file:
                data = json.load(file)
            self.text.delete(1.0, tk.END)
            self.text.insert(tk.END, json.dumps(data, indent=4))
        except Exception as e:
            messagebox.showerror("Error", f"No se pudo cargar el archivo: {e}")

    def save_file(self):
        file_path = self.entry.get()
        if file_path:
            try:
                data = json.loads(self.text.get(1.0, tk.END))
                with open(file_path, 'w') as file:
                    json.dump(data, file, indent=4)
                messagebox.showinfo("Éxito", "Archivo guardado correctamente.")
            except Exception as e:
                messagebox.showerror("Error", f"No se pudo guardar el archivo: {e}")

if __name__ == "__main__":
    root = tk.Tk()
    app = JSONEditor(root)
    root.mainloop()