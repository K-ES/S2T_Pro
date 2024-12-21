import tkinter as tk
from tkinter import filedialog, messagebox, ttk
import re
import os
import configparser
import logging
from datetime import datetime

# Setup logging to use a fixed file 'log.log' and overwrite it each time
def setup_logging():
    logs_dir = "logs"
    if not os.path.exists(logs_dir):
        os.makedirs(logs_dir)

    log_filename = os.path.join(logs_dir, "log.log")  # Фиксированное имя файла

    # Устанавливаем кодировку UTF-8 для записи логов
    logging.basicConfig(
        filename=log_filename,
        level=logging.INFO,
        format='%(asctime)s - %(levelname)s - %(message)s',
        encoding='utf-8',  # Добавляем параметр encoding для записи в кодировке UTF-8
        filemode='w'  # Параметр filemode='w' перезаписывает файл каждый раз
    )
    logging.info("Logging initialized.")  # Записываем начальную информацию в лог

# Initialize logging at the start of the program
setup_logging()

# Load settings from a configuration file
def load_settings():
    settings_dir = "settings"
    settings_file = os.path.join(settings_dir, "settings.ini")

    # Ensure settings directory exists
    if not os.path.exists(settings_dir):
        logging.error("Settings directory does not exist.")
        messagebox.showerror("Error", "Settings directory does not exist. Please create it and add the settings.ini file.")
        raise FileNotFoundError("Settings directory is missing.")

    # Create a default settings file if it doesn't exist
    if not os.path.exists(settings_file):
        config = configparser.ConfigParser()
        config['DEFAULT'] = {
            'repository_path': './s2t/ekp',
            'default_file': ''
        }
        with open(settings_file, 'w', encoding='utf-8') as file:
            config.write(file)
        logging.info("Default settings file created.")

    # Load settings from the file
    try:
        config = configparser.ConfigParser()
        config.read(settings_file, encoding='utf-8')
        logging.info("Settings loaded successfully.")
        return config['DEFAULT']
    except Exception as e:
        logging.error(f"Failed to load settings: {e}")
        messagebox.showerror("Error", f"Failed to load settings: {e}")
        raise

settings = load_settings()
repository_path = settings.get('repository_path', './s2t/ekp')
default_file = settings.get('default_file', '')

# Function to extract lines ending with AS (
def extract_lines_ending_with_as(content):
    as_line_pattern = r".*\bAS\s*\($"
    matches = list(re.finditer(as_line_pattern, content, re.IGNORECASE | re.MULTILINE))
    logging.info(f"Extracted {len(matches)} lines ending with AS (.")  # Логируем количество найденных строк
    return matches

# Function to update the CTE list with lines ending with AS (
def update_cte_list():
    content = editor_text.get(1.0, tk.END)
    matches = extract_lines_ending_with_as(content)
    cte_list.delete(0, tk.END)
    for match in matches:
        line_number = editor_text.index(f"1.0 + {match.start()} chars").split(".")[0]
        display_text = f"Line {line_number}: {match.group().strip()}"
        cte_list.insert(tk.END, display_text)
    logging.info("CTE list updated with lines ending with AS (.")  # Логируем обновление списка

def highlight_editor_content(event=None):
    content = editor_text.get(1.0, tk.END)

    # Очистим существующие теги
    editor_text.tag_remove("cte", "1.0", tk.END)
    editor_text.tag_remove("comment", "1.0", tk.END)
    editor_text.tag_remove("multiline_comment", "1.0", tk.END)

    # Подсветим строки, заканчивающиеся на AS (
    # as_pattern = r".*AS\s*\(\s*$"
    # as_pattern = r".*AS\s*\(\s*$"
    as_pattern = r".*AS\s*\(.*"
    as_matches = list(re.finditer(as_pattern, content))
    logging.info(f"Found {len(as_matches)} lines ending with 'AS ('.")  # Логируем поиск
    for match in as_matches:
        start_index = f"1.0 + {match.start()} chars"
        end_index = f"1.0 + {match.end()} chars"
        editor_text.tag_add("cte", start_index, end_index)
        # logging.info(f"Line ending with 'AS (': {match.group().strip()}")  # Логируем каждую найденную строку

    # Подсветим одно- и многострочные комментарии
    comment_pattern = r"--.*"
    comment_matches = list(re.finditer(comment_pattern, content))
    logging.info(f"Found {len(comment_matches)} single-line comments.")  # Логируем количество комментариев
    for match in comment_matches:
        start_index = f"1.0 + {match.start()} chars"
        end_index = f"1.0 + {match.end()} chars"
        editor_text.tag_add("comment", start_index, end_index)
        # logging.info(f"Single-line comment: {match.group().strip()}")  # Логируем каждую найденную строку

    multiline_comment_pattern = r"/\*.*?\*/"
    multiline_comment_matches = list(re.finditer(multiline_comment_pattern, content, re.DOTALL))
    logging.info(f"Found {len(multiline_comment_matches)} multi-line comments.")  # Логируем количество многострочных комментариев
    for match in multiline_comment_matches:
        start_index = f"1.0 + {match.start()} chars"
        end_index = f"1.0 + {match.end()} chars"
        editor_text.tag_add("multiline_comment", start_index, end_index)
        # logging.info(f"Multi-line comment: {match.group().strip()}")  # Логируем каждую найденную строку

    # Настроим стиль тегов
    editor_text.tag_config("multiline_comment", foreground="green")
    editor_text.tag_config("cte", foreground="blue")
    editor_text.tag_config("comment", foreground="red")

    logging.info("Editor content highlighted.")  # Логируем завершение подсветки

# Function to save the edited file and update the CTE list
def save_file():
    file_path = filedialog.asksaveasfilename(defaultextension=".sql", filetypes=[("SQL Files", "*.sql"), ("All Files", "*.*")])
    if not file_path:
        logging.warning("Save operation canceled by the user.")  # Логируем предупреждение
        return

    with open(file_path, 'w', encoding='utf-8') as file:
        content = editor_text.get(1.0, tk.END)
        file.write(content)

    update_cte_list()
    highlight_editor_content()
    logging.info(f"File saved to {file_path}.")  # Логируем успешное сохранение

# Function to open a file in the editor
def open_file_editor(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()
        logging.info(f"File {file_path} opened successfully.")  # Логируем успешное открытие
    except UnicodeDecodeError:
        with open(file_path, 'r', encoding='windows-1251') as file:
            content = file.read()
        logging.warning(f"File {file_path} opened with fallback encoding (windows-1251).")  # Логируем предупреждение о кодировке

    editor_text.delete(1.0, tk.END)
    editor_text.insert(tk.END, content)

    update_cte_list()
    highlight_editor_content()

# Function to jump to a specific line in the editor
def jump_to_line(line_number):
    editor_text.see(f"{line_number}.0")
    editor_text.mark_set(tk.INSERT, f"{line_number}.0")
    editor_text.focus()

# Create the main application window
root = tk.Tk()
root.title("CTE Extractor")
root.state('zoomed')  # Start in maximized mode

# Add notebook (tabs)
tabs = ttk.Notebook(root)
tabs.pack(expand=1, fill="both")

# Tab 1: File Editor
editor_frame = ttk.Frame(tabs)
tabs.add(editor_frame, text="File Editor")

# Add a listbox for CTEs with a label
cte_list_frame = ttk.Frame(editor_frame)
cte_list_frame.pack(side=tk.LEFT, fill=tk.Y, padx=5, pady=5)
cte_list_label = ttk.Label(cte_list_frame, text="Список строк с AS (", font=("Arial", 10, "bold"))
cte_list_label.pack(anchor="w")
cte_list = tk.Listbox(cte_list_frame, width=50, font=("Courier", 10))
cte_list.pack(fill=tk.Y, expand=1)

# Add click event to jump to a line with AS (
def on_cte_click(event):
    selected_index = cte_list.curselection()
    if selected_index:
        selected_line = cte_list.get(selected_index)
        line_number = selected_line.split(":")[0].split()[1]
        jump_to_line(line_number)

cte_list.bind("<Double-1>", on_cte_click)

# Add a text widget for editing files
editor_text = tk.Text(editor_frame, wrap="word", font=("Courier", 10))
editor_text.pack(side=tk.LEFT, expand=1, fill="both", padx=5, pady=5)
editor_text.bind("<KeyRelease>", highlight_editor_content)  # Bind key release event to highlight content

# Add Save button
save_button = tk.Button(editor_frame, text="Save File", command=save_file, font=("Arial", 12, "bold"))
save_button.pack(side=tk.BOTTOM, pady=5)

# Open default file in editor at startup
if default_file:
    if os.path.exists(default_file):
        open_file_editor(default_file)
    else:
        logging.warning(f"Default file '{default_file}' does not exist.")  # Логируем, если файл не найден

# Run the application
root.mainloop()
