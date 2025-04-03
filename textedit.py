import sys
import json
from tkinter import *
from tkinter import filedialog, messagebox

# Create the main window
root = Tk()
text = Text(root)
text.grid()

# Save text function
def saveas():
    global text
    content = text.get("1.0", "end-1c")  # Get the content of the text area

    # Open file dialog to choose save location
    savelocation = filedialog.asksaveasfilename(defaultextension=".json",
                                                filetypes=[("JSON files", "*.json"),
                                                          ("All files", "*.*")])
    if savelocation:
        theme_name = loadTheme()  # Get the currently selected theme
        # Save content and theme in a JSON file
        with open(savelocation, "w") as file1:
            json.dump({"content": content, "theme": theme_name}, file1)

# Font changer functions
def FontHelvetica():
    text.config(font=("Helvetica", 12))

def FontCourier():
    text.config(font=("Courier", 12))

# Font menu
menubar = Menu(root)
root.config(menu=menubar)

fontmenu = Menu(menubar, tearoff=0)
menubar.add_cascade(label="Fonts", menu=fontmenu)
fontmenu.add_command(label="Courier", command=FontCourier)
fontmenu.add_command(label="Helvetica", command=FontHelvetica)

# Open file function
def openFile():
    global current_theme
    file_path = filedialog.askopenfilename(filetypes=[("JSON files", "*.json"),
                                                      ("All files", "*.*")])
    if file_path:
        try:
            with open(file_path, "r") as file:
                data = json.load(file)
                content = data.get("content", "")
                theme = data.get("theme", "Light Mode")
                text.delete("1.0", END)  # Clear the existing content
                text.insert(INSERT, content)  # Insert the content from the file
                apply_theme(theme)  # Apply the saved theme
        except json.JSONDecodeError:
            print("Error: The file is not a valid JSON file or is empty.")
            # Optionally, show an error message to the user using a pop-up
            messagebox.showerror("Error", "Invalid or empty file selected.")

openButton = Button(root, text="Open", command=openFile)
openButton.grid()

# Cut, copy, paste functions
def cutText():
    text.event_generate("<<Cut>>")

def copyText():
    text.event_generate("<<Copy>>")

def pasteText():
    text.event_generate("<<Paste>>")

# Edit menu
editMenu = Menu(menubar, tearoff=0)
menubar.add_cascade(label="Edit", menu=editMenu)
editMenu.add_command(label="Cut", command=cutText)
editMenu.add_command(label="Copy", command=copyText)
editMenu.add_command(label="Paste", command=pasteText)

# Theme options
themes = {
    "Light Mode": {"bg": "#ffffff", "fg": "#000000", "insert": "#000000", "font": ("Arial", 12)},
    "Dark Mode": {"bg": "#000000", "fg": "#ffffff", "insert": "#ffffff", "font": ("Arial", 12)},
    "Pink Princess": {"bg": "#ffe8e6", "fg": "#fc3468", "insert": "#ffb3b3", "font": ("Consolas", 12)},
    "Goth": {"bg": "#000000", "fg": "#ff0000", "insert": "#ac0000", "font": ("Times New Roman", 12)}
}

# Theme toggle button
theme_menu = Menu(menubar, tearoff=0)
menubar.add_cascade(label="Themes", menu=theme_menu)

# Apply theme function
def apply_theme(theme_name):
    theme = themes.get(theme_name, themes["Light Mode"])  # Default to Light Mode if not found
    text.config(bg=theme["bg"], fg=theme["fg"], insertbackground=theme["insert"], font=theme["font"])
    save_theme(theme_name)

# Save theme function
def save_theme(theme_name):
    with open("theme.json", "w") as file:
        json.dump({"theme": theme_name}, file)

# Load theme function
def loadTheme():
    try:
        with open("theme.json", "r") as file:
            data = json.load(file)
            return data.get("theme", "Light Mode")
    except (FileNotFoundError, json.JSONDecodeError):
        return "Light Mode"

# Load the saved theme on start
apply_theme(loadTheme())

# Add theme options in the menu
for theme_name in themes.keys():
    theme_menu.add_command(label=theme_name, command=lambda t=theme_name: apply_theme(t))

# Add save button
button = Button(root, text="Save As", command=saveas)
button.grid()

root.mainloop()
