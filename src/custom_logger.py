import logging
import os

# Static attributes: LOG_FILE, LOG_LEVEL, FORMATTER
# (RU) Статические атрибуты: LOG_FILE, LOG_LEVEL, FORMATTER

# Class attributes: _instance, log_file, log_level, logger
# (RU) Атрибуты класса: _instance, log_file, log_level, logger

# Methods: __new__, __init__, setup_logging, log
# (RU) Методы: __new__, __init__, setup_logging, log

# Constants
# (RU) Константы
LOG_FILE = 'logs/log.log'
LOG_LEVEL = logging.INFO
FORMATTER = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')

class CustomLogger:
    _instance = None  # Static attribute to hold the single instance of the logger.
                      # (RU) Статический атрибут, содержащий единственный экземпляр логгера.

    def __new__(cls, log_file=LOG_FILE, log_level=LOG_LEVEL):
        """
        Method to create (or get) the single instance of the logger.

        (RU) Метод для создания (или получения) единственного экземпляра логгера.
        """
        if not cls._instance:
            cls._instance = super(CustomLogger, cls).__new__(cls)
            cls._instance.__init__(log_file, log_level)
        return cls._instance

    def __init__(self, log_file=LOG_FILE, log_level=LOG_LEVEL):
        """
        Initialize the logger. Creates 'logs' directory if it doesn't exist,
        and sets up logging at the specified log_level. Logs will be written to log_file.

        (RU) Инициализирует логгер. Создаёт директорию 'logs', если она не существует,
        и настраивает уровень логирования. Сообщения будут записаны в log_file.
        """
        if hasattr(self, 'logger'):  # Skip re-initializing if the logger is already set up
                                    # (RU) Пропустить повторную инициализацию, если логгер уже настроен
            return
        self.log_file = log_file
        self.log_level = log_level
        self.setup_logging()

    def setup_logging(self):
        """
        Set up logging by creating the logs directory (if it doesn't exist)
        and configuring the logger with the specified settings.

        (RU) Настраивает логирование: создаёт директорию для логов (если нет),
        и конфигурирует логгер с нужными параметрами.
        """
        logs_dir = os.path.dirname(self.log_file)
        if not os.path.exists(logs_dir):
            os.makedirs(logs_dir)

        self.logger = logging.getLogger()
        self.logger.setLevel(self.log_level)  # Use the log level passed during initialization
                                              # (RU) Использовать уровень логирования, переданный при инициализации

        # Create a handler to write logs to a file
        # (RU) Создаём обработчик для записи логов в файл
        file_handler = logging.FileHandler(self.log_file)
        file_handler.setLevel(self.log_level)

        # Apply the formatter to the file handler
        # (RU) Устанавливаем форматтер для обработчика файла
        file_handler.setFormatter(FORMATTER)
        self.logger.addHandler(file_handler)

        # Create a handler to output logs to the console
        # (RU) Создаём обработчик для вывода логов в консоль
        console_handler = logging.StreamHandler()
        console_handler.setLevel(self.log_level)
        console_handler.setFormatter(FORMATTER)
        self.logger.addHandler(console_handler)

    def log(self, message, level=logging.INFO):
        """
        Logs a message at the specified log level.

        (RU) Логирует сообщение на указанном уровне логирования.
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
