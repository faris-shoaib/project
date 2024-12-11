import tkinter as tk
from tkinter import messagebox
from gtts import gTTS
import os

def play_text():
    text = text_entry.get()
    if text.strip():
        try:
            tts = gTTS(text=text, lang='en')
            tts.save("output.mp3")
            os.system("start output.mp3" if os.name == "nt" else "afplay output.mp3")
        except Exception as e:
            messagebox.showerror("خطأ", f"حدث خطأ أثناء تشغيل الصوت: {e}")
    else:
        messagebox.showwarning("تحذير", "يرجى إدخال النص أولاً!")

def reset_text():
    text_entry.delete(0, tk.END)

def exit_program():
    root.destroy()

# إعداد واجهة التطبيق
root = tk.Tk()
root.title("Text to Speech")
root.geometry("400x300")
root.configure(bg="#f0f0f0")

# العنوان
header = tk.Label(root, text="Text to Speech", font=("Arial", 20, "bold"), bg="#f0f0f0", fg="#333")
header.pack(pady=10)

# الوصف
sub_header = tk.Label(root, text="Enter your text below:", font=("Arial", 12), bg="#f0f0f0", fg="#555")
sub_header.pack()

# مربع النص
text_entry = tk.Entry(root, width=40, font=("Arial", 14), justify="center", bd=2, relief="solid")
text_entry.pack(pady=10)

# إطار الأزرار
button_frame = tk.Frame(root, bg="#f0f0f0")
button_frame.pack(pady=20)

# زر التشغيل
play_button = tk.Button(button_frame, text="Play", font=("Arial", 12, "bold"), bg="#4caf50", fg="white", width=10, command=play_text)
play_button.grid(row=0, column=0, padx=10)

# زر إعادة التعيين
reset_button = tk.Button(button_frame, text="Reset", font=("Arial", 12, "bold"), bg="#2196f3", fg="white", width=10, command=reset_text)
reset_button.grid(row=0, column=1, padx=10)

# زر الخروج
exit_button = tk.Button(button_frame, text="Exit", font=("Arial", 12, "bold"), bg="#f44336", fg="white", width=10, command=exit_program)
exit_button.grid(row=0, column=2, padx=10)

# تذييل
footer = tk.Label(root, text="Developed by: faris shoaib", font=("Arial", 10), bg="#f0f0f0", fg="#999")
footer.pack(side="bottom", pady=10)

root.mainloop()