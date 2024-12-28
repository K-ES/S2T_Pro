# custom_logger.py

import logging
import os


class CustomLogger:
    _instance = None  # Статический атрибут для хранения единственного экземпляра

    def __new__(cls, log_file='logs/log.log', log_level=logging.INFO):
        """
        Метод для создания (или получения) единственного экземпляра логгера.
        """
        if not cls._instance:
            cls._instance = super(CustomLogger, cls).__new__(cls)
            cls._instance.__init__(log_file, log_level)
        return cls._instance

    def __init__(self, log_file='logs/log.log', log_level=logging.INFO):
        """
        Инициализация логгера. Создает директорию 'logs' (если она не существует) и
        настраивает логирование на уровне log_level. Логи будут записываться в файл log_file.
        """
        if hasattr(self, 'logger'):  # Если логгер уже инициализирован, пропускаем повторную инициализацию
            return

        self.log_file = log_file
        self.log_level = log_level
        self.setup_logging()

    def setup_logging(self):
        """
        Настроить логирование, создавая директорию для логов (если не существует) и настраивая логгер.
        """
        logs_dir = os.path.dirname(self.log_file)
        if not os.path.exists(logs_dir):
            os.makedirs(logs_dir)

        self.logger = logging.getLogger()
        self.logger.setLevel(self.log_level)  # Используем уровень, переданный в конструктор

        # Создаем обработчик для записи в файл
        file_handler = logging.FileHandler(self.log_file)
        file_handler.setLevel(self.log_level)

        # Создаем формат для логов
        formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
        file_handler.setFormatter(formatter)
        self.logger.addHandler(file_handler)

        # Создаем обработчик для вывода в консоль
        console_handler = logging.StreamHandler()
        console_handler.setLevel(self.log_level)
        console_handler.setFormatter(formatter)
        self.logger.addHandler(console_handler)

    def log(self, message, level=logging.INFO):
        """Записывает сообщение в лог с указанным уровнем"""
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
