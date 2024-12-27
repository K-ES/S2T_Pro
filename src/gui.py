# src/app_gui.py
import tkinter as tk

class AppGUI:
    """
    Класс для управления интерфейсной частью приложения (Tkinter).
    """
    def __init__(self, root, on_button_click):
        self.root = root  # Главное окно Tkinter
        self.on_button_click = on_button_click
        self.setup_ui()  # Настроим интерфейс

    def setup_ui(self):
        """
        Метод для создания всех виджетов интерфейса.
        """
        self.root.title("Tkinter Application")  # Заголовок окна
        self.button = tk.Button(self.root, text="Click Me", command=self.on_button_click)
        self.button.pack(pady=50)  # Размещаем кнопку