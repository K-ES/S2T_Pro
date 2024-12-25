import tkinter as tk
from src.custom_logger import CustomLogger  # Импортируем CustomLogger

class Application:
    def __init__(self, root):
        self.root = root
        self.root.title("My Application")
        self.root.geometry("300x200")

        # Инициализация логгера с уровнем DEBUG
        self.logger = CustomLogger()

        # Кнопка
        self.button = tk.Button(self.root, text="Click Me", command=self.on_button_click)
        self.button.pack(pady=50)

        # Логируем запуск приложения
        self.logger.log("Application started")  # Здесь не нужно передавать уровень, он уже установлен

    def on_button_click(self):
        """Обработчик нажатия кнопки."""
        self.logger.log("Button clicked")  # Логируем нажатие кнопки
        print("Button clicked!")

if __name__ == "__main__":
    root = tk.Tk()
    app = Application(root)
    root.mainloop()
