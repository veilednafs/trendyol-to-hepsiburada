import tkinter as tk
from tkinter import filedialog, messagebox
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

def browse_file(entry):
    filename = filedialog.askopenfilename()
    entry.delete(0, tk.END)
    entry.insert(0, filename)

def run_conversion():
    input_file = input_entry.get()
    template_file = template_entry.get()
    output_file = output_entry.get()
    try:
        convert_products(input_file, template_file, output_file)
        messagebox.showinfo("Başarılı", "Dönüştürme tamamlandı.")
    except Exception as e:
        messagebox.showerror("Hata", str(e))

root = tk.Tk()
root.title("Trendyol → Hepsiburada Dönüştürücü")

tk.Label(root, text="Giriş Dosyası").grid(row=0, column=0, padx=10, pady=5)
input_entry = tk.Entry(root, width=40)
input_entry.grid(row=0, column=1)
tk.Button(root, text="Seç", command=lambda: browse_file(input_entry)).grid(row=0, column=2)

tk.Label(root, text="Şablon Dosyası").grid(row=1, column=0, padx=10, pady=5)
template_entry = tk.Entry(root, width=40)
template_entry.grid(row=1, column=1)
tk.Button(root, text="Seç", command=lambda: browse_file(template_entry)).grid(row=1, column=2)

tk.Label(root, text="Çıktı Dosyası").grid(row=2, column=0, padx=10, pady=5)
output_entry = tk.Entry(root, width=40)
output_entry.grid(row=2, column=1)
tk.Button(root, text="Kaydet", command=lambda: browse_file(output_entry)).grid(row=2, column=2)

tk.Button(root, text="DÖNÜŞTÜR", command=run_conversion, bg="green", fg="white").grid(row=3, column=1, pady=20)

root.mainloop()
