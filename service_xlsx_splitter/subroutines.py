import os
import sys
from argparse import Namespace

# Add current working directory to system path for importing modules
CWD = os.getcwd()
sys.path.append(CWD)

from common.utilities.logger import SingletonLogger
from common.xlsx.large_xlsx_splitter_utils import excel_to_csv, process_csv

# Configure logger with colored output and a structured format
logger = logger = SingletonLogger.get_instance("my_logger", log_to_console=True)


def extract_csv_from_excel(args: Namespace, input_xlsx_path: str, output_csv_path: str):
    # If the --extract_csv option is specified, generate a CSV from the Excel file
    if args.extract_csv:
        logger.info(f"Generating CSV file from {input_xlsx_path}...")
        try:
            excel_to_csv(
                input_file_excel=input_xlsx_path,
                output_file_csv=output_csv_path,
                delimiter=";",  # CSV delimiter (using this since some fields may contain commas: ',')
            )
            logger.info(f"CSV created: {output_csv_path}")
        except Exception as e:
            logger.error(f"An error occurred while exporting the excel to csv: {e}")
            exit(-1)
    else:
        logger.info(f"Using existing CSV file: {output_csv_path}")


def process_csv_file(args: Namespace, input_csv_path: str, processed_csv_path: str):
    if args.process_csv:
        logger.info(f"Processing CSV file at {input_csv_path} before splitting.")
        try:
            process_csv(
                input_csv=input_csv_path,
                output_csv=processed_csv_path,
            )
        except Exception as e:
            logger.error(f"An error occurred while processing the csv file: {e}")
            exit(-1)
