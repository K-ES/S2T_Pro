import logging
import os
from typing import Optional

# Static attributes: LOG_FILE, LOG_LEVEL, FORMATTER
# (RU) Статические атрибуты: LOG_FILE, LOG_LEVEL, FORMATTER

# Class attributes: _instance, log_file, log_level, logger
# (RU) Атрибуты класса: _instance, log_file, log_level, logger

# Methods: __new__, __init__, setup_logging, log, add_gui_handler
# (RU) Методы: __new__, __init__, setup_logging, log, add_gui_handler

# Constants
# (RU) Константы
LOG_FILE: str = 'logs/log.log'
LOG_LEVEL: int = logging.INFO
FORMATTER: logging.Formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')


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
            cls._instance.__init__(log_file, log_level)
        return cls._instance

    def __init__(self, log_file: str = LOG_FILE, log_level: int = LOG_LEVEL) -> None:
        """
        Initialize the logger. Creates 'logs' directory if it doesn't exist,
        and sets up logging at the specified log_level. Logs will be written to log_file.

        (RU) Инициализирует логгер. Создаёт директорию 'logs', если она не существует,
        и настраивает уровень логирования. Сообщения будут записаны в log_file.
        """
        if hasattr(self, 'logger'):  # Skip re-initializing if the logger is already set up
                                      # (RU) Пропустить повторную инициализацию, если логгер уже настроен
            return
        self.log_file: str = log_file
        self.log_level: int = log_level
        self.setup_logging()

    def setup_logging(self) -> None:
        """
        Set up logging by creating the logs directory (if it doesn't exist)
        and configuring the logger with the specified settings.

        (RU) Настраивает логирование: создаёт директорию для логов (если нет),
        и конфигурирует логгер с нужными параметрами.
        """
        logs_dir: str = os.path.dirname(self.log_file)
        if not os.path.exists(logs_dir):
            os.makedirs(logs_dir)

        self.logger: logging.Logger = logging.getLogger()  # Используем корневой логгер
        self.logger.setLevel(self.log_level)  # Use the log level passed during initialization
                                              # (RU) Использовать уровень логирования, переданный при инициализации

        # Проверяем, добавлены ли уже обработчики, чтобы избежать дублирования
        if not self.logger.hasHandlers():
            # Create a handler to write logs to a file
            # (RU) Создаём обработчик для записи логов в файл
            file_handler: logging.FileHandler = logging.FileHandler(self.log_file)
            file_handler.setLevel(self.log_level)

            # Apply the formatter to the file handler
            # (RU) Устанавливаем форматтер для обработчика файла
            file_handler.setFormatter(FORMATTER)
            self.logger.addHandler(file_handler)

            # Create a handler to output logs to the console
            # (RU) Создаём обработчик для вывода логов в консоль
            console_handler: logging.StreamHandler = logging.StreamHandler()
            console_handler.setLevel(self.log_level)
            console_handler.setFormatter(FORMATTER)
            self.logger.addHandler(console_handler)

    def add_gui_handler(self, gui_handler: logging.Handler) -> None:
        """
        Adds a handler for GUI logging.
        :param gui_handler: An instance of a class that inherits from logging.Handler

        (RU) Добавляет обработчик для GUI.
        :param gui_handler: экземпляр класса, наследующего от logging.Handler
        """
        self.logger.addHandler(gui_handler)

    def log(self, message: str, level: int = logging.INFO) -> None:
        """
        Logs a message at the specified log level.

        (RU) Логирует сообщение на указанном уровне логирования.
        :param message: Сообщение для логирования
        :param level: Уровень логирования
        """
        if level == logging.DEBUG:
            self.logger.debug(message)
        elif level == logging.INFO:
            self.logger.info(message)
        elif level == logging.WARNING:
            self.logger.warning(message)
        elif level == logging.ERROR:
            self.logger.error(message)
        elif level == logging.CRITICAL:
            self.logger.critical(message)
        else:
            self.logger.log(level, message)
