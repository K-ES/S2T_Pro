import logging
from src.application import Application
from src.custom_logger import CustomLogger  # Импортируем CustomLogger


def main():
    logger = CustomLogger()
    logger.log("Starting the application...", level=logging.INFO)
    try:
        app = Application()
        app.run()
    except Exception as e:
        logger.log(f"An error occurred: {e}", level=logging.ERROR)


if __name__ == "__main__":
    main()