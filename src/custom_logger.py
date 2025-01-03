# 2024-12-31, Kes, Initial version with color-coded logging and singleton pattern
#                  ChatGPT https://chatgpt.com/share/67738dc8-c13c-8012-bff3-5ee7528e6e72
# 2025-01-03, Logging adjustments https://chatgpt.com/share/6777667b-ad08-8012-8044-21aa61ba92b5


import logging
import os
from typing import Optional
import inspect

# Static attributes: LOG_FILE, LOG_LEVEL, FORMATTER
# (RU) Статические атрибуты: LOG_FILE, LOG_LEVEL, FORMATTER

# Class attributes: _instance, log_file, log_level, logger
# (RU) Атрибуты класса: _instance, log_file, log_level, logger

# Methods: __new__, __init__, setup_logging, log, add_gui_handler, set_log_level, test_logs
# (RU) Методы: __new__, __init__, setup_logging, log, add_gui_handler, set_log_level, test_logs

# Constants
# (RU) Константы
LOG_FILE: str = 'logs/log.log'
LOG_LEVEL: int = logging.INFO
FORMATTER: logging.Formatter = logging.Formatter('%(asctime)s %(levelname)s %(message)s (%(filename)s:%(lineno)d)')


class CustomColorFormatter(logging.Formatter):
    """
    Custom formatter to add colors to console log messages based on their level.
    """
    COLORS = {
        logging.DEBUG: "\033[0;37m",  # Серый текст
        logging.INFO: "\033[0;32m",  # Зеленый текст
        logging.WARNING: "\033[0;33m",  # Желтый текст
        logging.ERROR: "\033[0;31m",  # Красный текст
        logging.CRITICAL: "\033[1;31m"  # Жирный красный текст
    }

    RESET = "\033[0m"

    def format(self, record: logging.LogRecord) -> str:
        # Форматируем уровень логирования так, чтобы занимал 8 символов и заключаем в квадратные скобки
        record.levelname = f"[{record.levelname:<8}]"
        formatted_message = super().format(record)
        level_color = self.COLORS.get(record.levelno, self.RESET)
        return f"{level_color}{formatted_message}{self.RESET}"




class CustomLogger:
    _instance: Optional['CustomLogger'] = None  # Static attribute to hold the single instance of the logger.
                                                # (RU) Статический атрибут, содержащий единственный экземпляр логгера.

    def __new__(cls, log_file: str = LOG_FILE, log_level: int = LOG_LEVEL) -> 'CustomLogger':
        """
        Method to create (or get) the single instance of the logger.

        (RU) Метод для создания (или получения) единственного экземпляра логгера.
        """
        if not cls._instance:
            cls._instance = super(CustomLogger, cls).__new__(cls)
            cls._instance.setup_logging(log_file, log_level)
        print(f"Logger initialized with __name__: {__name__}")  # Display module name in the console
        return cls._instance

    def __init__(self, *args, **kwargs) -> None:
        """
        Prevent reinitialization of the singleton instance.

        (RU) Предотвращает повторную инициализацию единственного экземпляра.
        """
        pass

    def setup_logging(self, log_file: str = LOG_FILE, log_level: int = LOG_LEVEL) -> None:
        """
        Set up logging by creating the logs directory (if it doesn't exist)
        and configuring the logger with the specified settings.

        (RU) Настраивает логирование: создаёт директорию для логов (если нет),
        и конфигурирует логгер с нужными параметрами.
        """
        self.log_file = log_file
        self.log_level = log_level
        self.logger = logging.getLogger(self.__class__.__name__)  # Logger name is the class name
        self.logger.setLevel(log_level)

        # Create the logs directory if it doesn't exist
        # (RU) Создаёт директорию для логов, если она не существует
        logs_dir = os.path.dirname(self.log_file)
        if not os.path.exists(logs_dir):
            os.makedirs(logs_dir)

        if not self.logger.handlers:
            # Add file handler
            # (RU) Добавляет обработчик для записи логов в файл
            file_handler = logging.FileHandler(self.log_file)
            file_handler.setFormatter(FORMATTER)
            file_handler.setLevel(self.log_level)
            self.logger.addHandler(file_handler)

            # Add console handler with color formatting
            # (RU) Добавляет обработчик для вывода логов в консоль с цветами
            console_handler = logging.StreamHandler()
            console_handler.setFormatter(CustomColorFormatter(FORMATTER._fmt))
            console_handler.setLevel(self.log_level)
            self.logger.addHandler(console_handler)

    def _add_handler(self, handler: logging.Handler) -> None:
        """
        Helper method to add a handler with the predefined formatter and log level.

        (RU) Вспомогательный метод для добавления обработчика с заданным форматтером и уровнем логирования.
        """
        handler.setLevel(self.log_level)
        handler.setFormatter(FORMATTER)
        self.logger.addHandler(handler)

    def log(self, message: str, level: int = logging.INFO) -> None:
        """
        Logs a message at the specified log level.
        """
        self.logger.log(level, message, stacklevel=2)  # Даем логгеру самому обрабатывать вывод

    def add_gui_handler(self, gui_handler: logging.Handler) -> None:
        """
        Adds a handler for GUI logging.
        :param gui_handler: An instance of a class that inherits from logging.Handler

        (RU) Добавляет обработчик для GUI.
        :param gui_handler: экземпляр класса, наследующего от logging.Handler
        """
        self._add_handler(gui_handler)

    def set_log_level(self, log_level: int) -> None:
        """
        Dynamically change the log level for all handlers.

        (RU) Динамически изменяет уровень логирования для всех обработчиков.
        :param log_level: Новый уровень логирования
        """
        self.log_level = log_level
        self.logger.setLevel(log_level)
        for handler in self.logger.handlers:
            handler.setLevel(log_level)

    def test_logs(self) -> None:
        """
        Test the logger by logging messages at all levels.

        (RU) Тестирует логгер, логируя сообщения на всех уровнях.
        """
        self.log("Test INFO message", logging.INFO)
        self.log("Test WARNING message", logging.WARNING)
        self.log("Test ERROR message", logging.ERROR)
        self.log("Test DEBUG message", logging.DEBUG)
        self.log("Test CRITICAL message", logging.CRITICAL)

# Example usage
# (RU) Пример использования
if __name__ == "__main__":
    logger = CustomLogger()

    # Прямые вызовы логов с разных уровней
    logger.log("Test INFO message", logging.INFO)  # Должна показать номер этой строки
    logger.log("Test WARNING message", logging.WARNING)
    logger.log("Test ERROR message", logging.ERROR)
    logger.log("Test DEBUG message", logging.DEBUG)
    logger.log("Test CRITICAL message", logging.CRITICAL)