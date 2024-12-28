# src/app_gui.py
import tkinter as tk
from tkinter import ttk

class AppGUI:
    """
    Class to manage the interface part of the application (Tkinter).
    """
    def __init__(self, root):
        self.root = root  # Main Tkinter window
        self.setup_ui()  # Setup the interface

    def setup_ui(self):
        self.root.title("S2T PRO")  # Window title
        self.root.state("zoomed")  # Window maximized (works on Windows)

        # Create a Notebook for tabs
        self.notebook = ttk.Notebook(self.root)
        self.notebook.pack(fill='both', expand=True)

        # Log tab
        self.log_tab = ttk.Frame(self.notebook)
        self.notebook.add(self.log_tab, text="Application Log")

        # Text field to display logs
        self.log_text = tk.Text(self.log_tab, wrap='word', height=30, width=80)
        self.log_text.pack(fill='both', expand=True, padx=10, pady=10)

        # Example log entry
        self.write_log("Application started...")

    def write_log(self, message):
        """
        Method to add a message to the log.
        """
        self.log_text.insert(tk.END, message + "\n")
        self.log_text.see(tk.END)  # Scroll to the last message
