import tkinter as tk
from tkinter import scrolledtext
from langchain_ollama import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate
import logging

# Set up logging
logging.basicConfig(level=logging.INFO)

# Define the prompt template
template = """
Answer the Question below.

Here is the conversation history: {context}

Question: {question}

Answer:
"""

# Initialize the model and prompt template
model = OllamaLLM(model="llama3")
prompt = ChatPromptTemplate.from_template(template)
chain = prompt | model

class ChatbotApp:
    def __init__(self, root):
        self.root = root
        self.context = ""
        
        self.root.title("AI ChatBot")
        self.root.geometry("600x400")
        
        self.chat_display = scrolledtext.ScrolledText(self.root, wrap=tk.WORD, state=tk.DISABLED)
        self.chat_display.grid(row=0, column=0, columnspan=2, padx=10, pady=10, sticky="nsew")
        
        self.user_input = tk.Entry(self.root, width=80)
        self.user_input.grid(row=1, column=0, padx=10, pady=10, sticky="ew")
        self.user_input.bind("<Return>", self.send_message)
        
        self.send_button = tk.Button(self.root, text="Send", command=self.send_message)
        self.send_button.grid(row=1, column=1, padx=10, pady=10)
        
        self.root.grid_rowconfigure(0, weight=1)
        self.root.grid_columnconfigure(0, weight=1)

    def send_message(self, event=None):
        user_input_text = self.user_input.get()
        if user_input_text.lower() == 'q':
            self.root.quit()
            return
        
        self.update_chat_display(f"You: {user_input_text}\n")
        self.user_input.delete(0, tk.END)
        
        try:
            result = chain.invoke({"context": self.context, "question": user_input_text})
            self.update_chat_display(f"Bot: {result}\n")
            
            self.context += f"\nUser: {user_input_text}\nAI: {result}"
            if len(self.context) > 1000:
                self.context = self.context[-1000:]
        
        except Exception as e:
            logging.error("An error occurred: %s", e)
            self.update_chat_display("An error occurred. Please try again.\n")
    
    def update_chat_display(self, message):
        self.chat_display.config(state=tk.NORMAL)
        self.chat_display.insert(tk.END, message)
        self.chat_display.config(state=tk.DISABLED)
        self.chat_display.yview(tk.END)

if __name__ == "__main__":
    root = tk.Tk()
    app = ChatbotApp(root)
    root.mainloop()
