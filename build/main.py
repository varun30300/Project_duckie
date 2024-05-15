from Tools import KnowledgeInitializer
from langchain_openai import ChatOpenAI
import AgentCaller
import tkinter as tk
from tkinter import ttk
import os 

CHAT_MODEL = ChatOpenAI(model = "gpt-4o")
VERBOSE = False

# check if the database is changed, if yes, get new embedded knowledge retrieved tool 
retriever_tool = KnowledgeInitializer.knowledge_initializer()

history = [
                {   
                    "actor" : "human",
                    "content" : "Hi"
                } ,
                {
                    "actor" : "ai" ,
                    "content" : "Hello ! How cam I help you ?"
                } 
            ]

def add_history (actor, content):
    history.append({
        "actor" : actor,
        "content" : content
    })

def on_enter_pressed(event):
    human_text = human_text_box.get("1.0", tk.END).strip()
    add_history("human", human_text)
    human_text_box.delete(1.0, tk.END) 
    print(human_text)
    if human_text == "quit":
        root.destroy()
    else : 
        reponse = AgentCaller.duckie_response(CHAT_MODEL, human_text, retriever_tool, VERBOSE)
        add_history("ai", reponse['output'])
        update_display()
        print(reponse['output'])
    return "break"

def clear_frame():
    for widget in history_box.winfo_children():
        if isinstance(widget, tk.Label):
            widget.destroy()

def update_display():
    clear_frame()
    for exchange in history:
        label = tk.Label(history_box, text=exchange['content'], wraplength=400, font=('Arial', 13), justify="left", bg="white")
        if exchange["actor"] == "ai" : 
            label.pack(anchor="w")
        elif exchange["actor"] == "human" : 
            label.pack(anchor="e")


def list_files():
    directory = "Knowledge"  # Specify the directory path
    files = os.listdir(directory)
    for file in files:
        listbox.insert(tk.END, file)
    listbox.config(height=len(files), font=('Arial', 16))

def open_file():
    selection = listbox.curselection()  # Get the index of the selected item
    if selection:
        index = selection[0]
        filename = listbox.get(index)  # Get the filename from the selected index
        filepath = os.path.join("Knowledge", filename)  # Construct the full filepath
        with open(filepath, 'r') as file:
            content = file.read()
        # Create a new window to display the file content
        file_window = tk.Toplevel(root)
        file_window.title(filename)
        text_widget = tk.Text(file_window, wrap=tk.WORD)
        text_widget.insert(tk.END, content)
        text_widget.pack(fill=tk.BOTH, expand=True)


root = tk.Tk()
root.title("DUCKIE")
root.geometry("1500x800")
root.maxsize(width=1500, height=800)
root.minsize(width=1500, height=800)

root.columnconfigure(0, weight=15)  # 30% width
root.columnconfigure(1, weight=85)  # 70% width
root.rowconfigure(0, weight=1)
root.rowconfigure(1, weight=10)
root.rowconfigure(2, weight=1)

# Create a title label
title_label = tk.Label(root, text="Files in Directory", font=('Arial', 14, 'bold'))
title_label.grid(row=0, column=0, sticky="w", padx=10, pady=10)

# Create a Listbox widget
listbox = tk.Listbox(root, width=20)
listbox.grid(row=1, column=0, sticky="new", padx=10, pady=10)

list_files()

# Create a  history widget
history_box = tk.Frame(root, relief="ridge") 
history_box.grid(row=1, column=1, sticky="esw" , padx=50, pady=10)

update_display()

# Create a Frame for the text box at the bottom right
# text_frame = tk.Frame(root)
# text_frame.grid(row=0, column=1, padx=padding, pady=padding, sticky="nsew")

# Create a Text widget for user input
human_text_box = tk.Text(root, height=2, font=('Arial', 13))
human_text_box.grid(row=2, column=1, sticky="ew", padx=10, pady=10)

# Set column weights to adjust the column widths



# Bind double click event to open_file function
listbox.bind("<Double-Button-1>", lambda event: open_file())
human_text_box.bind("<Return>", on_enter_pressed)

# Run the Tkinter event loop
root.mainloop()

# while True : 

#     human_text = input("Query : ")

#     if human_text == "quit":
#         break

#     reponse = AgentCaller.duckie_response(CHAT_MODEL, human_text, retriever_tool, VERBOSE)

#     history.append(reponse)

#     print(reponse['output'])

# print(history)
