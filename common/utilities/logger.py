import logging
import sys
from colorlog import ColoredFormatter


class SingletonLogger:
    _instance = None

    @staticmethod
    def get_instance(
        logger_name: str, log_to_console: bool = True, log_file_path: str = None
    ) -> logging.Logger:
        if SingletonLogger._instance is None:
            SingletonLogger._instance = SingletonLogger.get_logger(
                logger_name, log_to_console, log_file_path
            )
            SingletonLogger._instance.setLevel(logging.INFO)
        return SingletonLogger._instance

    @staticmethod
    def get_logger(
        logger_name: str, log_to_console: bool = True, log_file_path: str = None
    ) -> logging.Logger:
        """
        Initializes and configures a logger with structured and optionally colored output.
        The logger can log to the console or to a specified log file.

        Args:
            logger_name (str): The name of the logger.
            log_to_console (bool): If True, log messages are printed to the terminal (default: True).
            log_file_path (str): If specified, log messages will be written to the provided file path.

        Returns:
            logging.Logger: Configured logger instance.
        """
        # Create a logger instance
        logger = logging.getLogger(logger_name)
        logger.setLevel(logging.DEBUG)

        # If logging to console is enabled, configure the console handler
        if log_to_console:
            console_handler = logging.StreamHandler(sys.stdout)
            console_handler.setLevel(logging.INFO)  # or DEBUG based on your needs

            # Define the log format for console output
            console_formatter = ColoredFormatter(
                "%(log_color)s[%(asctime)s] [%(levelname)s] - %(message)s",
                datefmt="%Y-%m-%d %H:%M:%S",
                log_colors={
                    "DEBUG": "cyan",
                    "INFO": "green",
                    "WARNING": "yellow",
                    "ERROR": "red",
                    "CRITICAL": "bold_red",
                },
            )
            console_handler.setFormatter(console_formatter)
            if not logger.handlers:  # Prevent adding duplicate handlers
                logger.addHandler(console_handler)

        # If a log file path is provided, configure the file handler
        if log_file_path:
            file_handler = logging.FileHandler(log_file_path)
            file_handler.setLevel(logging.INFO)

            # Define the log format for file output
            file_formatter = logging.Formatter(
                "[%(asctime)s] [%(levelname)s] - %(message)s",
                datefmt="%Y-%m-%d %H:%M:%S",
            )
            file_handler.setFormatter(file_formatter)
            if not logger.handlers:  # Prevent adding duplicate handlers
                logger.addHandler(file_handler)

        return logger
