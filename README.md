#Overview

This is a simple text editor built using Python's Tkinter GUI toolkit. It allows users to type, edit, and save text files in JSON format while preserving selected themes. The editor supports four predefined themes: Light Mode, Dark Mode, Pink Princess, and Goth.

#Features

Text Editing: Cut, copy, paste, and basic text formatting options.

Font Selection: Switch between Helvetica and Courier fonts.

Theme Support: Choose from four themes:

Light Mode: White background, black text.

Dark Mode: Black background, white text.

Pink Princess: Soft pink background with vibrant pink text.

Goth: Black background with red text.

Save & Open in JSON: The editor saves content along with the selected theme in a JSON file.

Theme Persistence: The last selected theme is stored and reloaded when the application starts.

#Installation

Ensure you have Python installed (version 3.4+ recommended, but does include fallbacks for older versions).

Install Tkinter if not included in your Python distribution.

Clone or download this repository.

Run the script using:

python textedit.py

#Usage

Type your text in the editor.

Use the Edit menu for text operations (Cut, Copy, Paste).

Select a font from the Fonts menu.

Choose a theme from the Themes menu.

Click Save As to store your text along with the selected theme in a JSON file.

Click Open to load a previously saved JSON file and restore the theme.

JSON Structure

When saved, the JSON file will have the following structure:

{
  "content": "Your text here...",
  "theme": "Selected Theme"
}

Example of a saved JSON file for the "Pink Princess" theme:

{
  "content": "princess theme test",
  "theme": "Pink Princess"
}

Future improvements to come.
