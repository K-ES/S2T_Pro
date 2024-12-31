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

class CustomColorFormatter(logging.Formatter):
    """
    Custom formatter to add colors to console log messages based on their level.

    (RU) Кастомный форматтер для добавления цветов к сообщениям в консоли в зависимости от уровня.
    """
    COLORS = {
        logging.DEBUG: "\033[1;94;40m",  # Bold Blue with Black background
        logging.INFO: "\033[1;92;45m",   # Bold Green with Magenta background
        logging.WARNING: "\033[1;93;41m",# Bold Yellow with Red background
        logging.ERROR: "\033[1;91;43m",  # Bold Red with Yellow background
        logging.CRITICAL: "\033[1;95;44m"# Bold Magenta with Blue background
    }
    RESET = "\033[0m"

    def format(self, record: logging.LogRecord) -> str:
        level_color = self.COLORS.get(record.levelno, self.RESET)
        record.msg = f"{level_color}{record.msg}{self.RESET}"
        return super().format(record)

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
            console_handler.setFormatter(CustomColorFormatter('%(asctime)s - %(levelname)s - %(message)s'))
            console_handler.setLevel(self.log_level)
            self.logger.addHandler(console_handler)

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
