import tkinter as tk
from tkinter import scrolledtext

from faq_web_app import get_best_answer  # reuse same engine

def send_message():
    user_text = entry.get().strip()
    if not user_text:
        return
    chat_area.config(state=tk.NORMAL)
    chat_area.insert(tk.END, "You: " + user_text + "\n")
    reply = get_best_answer(user_text)
    chat_area.insert(tk.END, "Bot: " + reply + "\n\n")
    chat_area.config(state=tk.DISABLED)
    chat_area.see(tk.END)
    entry.delete(0, tk.END)

root = tk.Tk()
root.title("FAQ Chatbot")

chat_area = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=60, height=20)
chat_area.config(state=tk.DISABLED)
chat_area.pack(padx=10, pady=10)

entry = tk.Entry(root, width=50)
entry.pack(side=tk.LEFT, padx=(10, 0), pady=(0, 10))
entry.bind("<Return>", lambda event: send_message())

send_button = tk.Button(root, text="Send", width=10, command=send_message)
send_button.pack(side=tk.LEFT, padx=10, pady=(0, 10))

root.mainloop()
