# logger.py

import os
import logging

class Logger:
    @staticmethod
    def setup_logging():
        """
        Настраивает логирование для приложения.
        Создаёт директорию 'logs' (если она не существует) и файл 'log.log',
        перезаписывая его при каждом запуске приложения.
        """
        logs_dir = "logs"
        if not os.path.exists(logs_dir):
            os.makedirs(logs_dir)
            logging.debug(f"Создана директория для логов: {logs_dir}")

        log_filename = os.path.join(logs_dir, "log.log")  # Фиксированное имя файла

        # Устанавливаем кодировку UTF-8 для записи логов
        logging.basicConfig(
            filename=log_filename,
            level=logging.INFO,
            format='%(asctime)s - %(levelname)s - %(message)s',
            encoding='utf-8',  # Кодировка UTF-8
            filemode='w'        # Перезаписываем файл при каждом запуске
        )
        logging.info("Logging initialized.")  # Начальная запись в лог