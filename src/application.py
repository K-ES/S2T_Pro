import tkinter as tk
from src.app_gui import AppGUI  # Импортируем интерфейс из другого файла

class Application:
    """
    Класс для управления логикой приложения и интерфейсом.
    """
    def __init__(self):
        self.root = tk.Tk()  # Создаем основное окно
        self.gui = AppGUI(self.root, self.on_button_click)  # Создаем интерфейс
        self.root.mainloop()  # Запуск главного цикла событий

    def on_button_click(self):
        """Обработчик нажатия кнопки."""
        print("Button clicked!")  # Выводим сообщение при нажатии