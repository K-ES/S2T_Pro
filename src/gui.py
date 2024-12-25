import tkinter as tk
from src.custom_logger import CustomLogger  # Импортируем CustomLogger

class Application:
    def __init__(self, root):
        self.root = root
        self.root.title("My Application")
        self.root.geometry("300x200")

        # Инициализация логгера
        self.logger = CustomLogger(log_file='logs/app.log')

        # Кнопка
        self.button = tk.Button(self.root, text="Click Me", command=self.on_button_click)
        self.button.pack(pady=50)

        # Логируем запуск приложения
        self.logger.log("Application started", logging.INFO)

    def on_button_click(self):
        """Обработчик нажатия кнопки."""
        self.logger.log("Button clicked", logging.INFO)  # Логируем нажатие кнопки
        print("Button clicked!")

if __name__ == "__main__":
    root = tk.Tk()
    app = Application(root)
    root.mainloop()