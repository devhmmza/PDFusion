#Merge PDF files with ease 
import os
import tkinter as tk
from tkinter import filedialog, messagebox
from PyPDF2 import PdfMerger

root = tk.Tk()
root.title("PDF Merger")
root.geometry("400x300")

pdf_files = []

def add_files():
    files = filedialog.askopenfilenames(filetypes=[("PDF Files", "*.pdf")])
    for file in files:
        pdf_files.append(file)
        listbox.insert(tk.END, os.path.basename(file))

def merge_pdfs():
    if not pdf_files:
        messagebox.showwarning("No files", "Please add some PDF files")
        return
    merger = PdfMerger()
    for pdf in pdf_files:
        merger.append(pdf)

    save_path = filedialog.asksaveasfilename(defaultextension=".pdf", filetypes=[("PDF Files", "*.pdf")])
    if save_path:
        merger.write(save_path)
        merger.close()
        messagebox.showinfo("Success", "PDFs merged successfully!")

def clear_list():
    pdf_files.clear()
    listbox.delete(0, tk.END)

btn_add = tk.Button(root, text="Add PDF Files", command=add_files)
btn_add.pack(pady=10)

btn_merge = tk.Button(root, text="Merge PDFs", command=merge_pdfs)
btn_merge.pack(pady=10)

btn_clear = tk.Button(root, text="Clear List", command=clear_list)
btn_clear.pack(pady=10)

listbox = tk.Listbox(root, width=50)
listbox.pack(pady=10)

root.mainloop()
