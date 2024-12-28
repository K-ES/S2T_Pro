# src/app_gui.py
import tkinter as tk

class AppGUI:
    """
    Класс для управления интерфейсной частью приложения (Tkinter).
    """
    def __init__(self, root):
        self.root = root  # Главное окно Tkinter
        self.setup_ui()  # Настроим интерфейс

    def setup_ui(self):
        self.root.title("S2T PRO")  # Заголовок окна
