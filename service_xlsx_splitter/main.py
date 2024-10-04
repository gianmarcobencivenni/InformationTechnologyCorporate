"""
This script processes a large Excel file by first converting it to a CSV format and then splitting the CSV data into 
multiple smaller Excel files while maintaining the original file's formatting. The script offers the option to use an 
existing CSV file if available, allowing users to skip the CSV generation step.

### Functionality:
- Converts a specified Excel file to a CSV format.
- Splits the CSV into multiple Excel files, each containing a portion of the data.
- Copies header and alternating row styles, merged cell structures, and column widths from a model Excel file to the 
  smaller Excel files.
- Uses a configuration file (`config.json`) to define the input/output paths, formatting model, and the number of 
  output files.

### Parameters:
- The script accepts command-line arguments via `argparse`:
  - `--csv`: Skip the CSV generation step if the CSV file already exists.
  
- The script loads the following configuration values from a `config.json` file:
  - `INPUT_XLSX_NAME`: The name of the input Excel file (without extension).
  - `MODEL_XLSX_NAME`: The name of the model Excel file used for copying styles and formatting.
  - `NUM_TARGET_FILE`: The number of output Excel files to create.
  - `TABLE_START_ROW`: The row index where the data table begins in the original Excel file.
  - `HEADER_ROWS`: The number of rows at the top of the file to be treated as a header.
  - `ROW_REF_ODD`: The reference row for the style of odd-numbered rows in the data table.
  - `ROW_REF_EVEN`: The reference row for the style of even-numbered rows in the data table.

### Usage:
1. Ensure that the input Excel file and the model Excel file are present in the `input` folder.
2. Define the desired configuration in the `config.json` file.
3. Run the script with the command:
   ```bash
   python .\service_xlsx_splitter\main.py
"""

import argparse
import os
import sys

# Add current working directory to system path for importing modules
CWD = os.getcwd()
sys.path.append(CWD)

from common.utilities.config_loader import load_json_configs_dict
from common.utilities.configuration_keys import ConfigKeys
from common.utilities.logger import SingletonLogger
from common.xlsx.large_xlsx_splitter_utils import excel_to_csv, split_csv_to_excel


CONFIG_JSON_PATH = os.path.join(CWD, "service_xlsx_splitter", "config.json")


# Configure logger with colored output and a structured format
logger = logger = SingletonLogger.get_instance("my_logger", log_to_console=True)


def main() -> None:
    """
    Main function to process an Excel file by converting it to CSV and splitting it into multiple smaller Excel files.
    The CSV conversion can be skipped if an existing CSV file is already present by passing the --csv option.
    """

    # Argument parser setup for command-line options
    parser = argparse.ArgumentParser(description="Process Excel files and split them.")
    parser.add_argument(
        "--csv", action="store_true", help="Use existing CSV file, if present"
    )
    args = parser.parse_args()

    # Load configuration values from the JSON file
    configs: dict = load_json_configs_dict(json_path=CONFIG_JSON_PATH)

    # Fetch configuration values for input and model Excel names and the number of target files
    INPUT_XLSX_NAME: str | None = str(
        configs.get(ConfigKeys.INPUT_XLSX_NAME.value, None)
    )
    MODEL_XLSX_NAME: str | None = str(
        configs.get(ConfigKeys.MODEL_XLSX_NAME.value, None)
    )
    NUM_TARGET_FILE: int | None = int(
        configs.get(ConfigKeys.NUM_TARGET_FILE.value, None)
    )
    TABLE_START_ROW: int = int(configs.get(ConfigKeys.TABLE_START_ROW.value, None))
    HEADER_ROWS: int = int(configs.get(ConfigKeys.HEADER_ROWS.value, None))
    ROW_REF_ODD: int = int(configs.get(ConfigKeys.ROW_REF_ODD.value, None))
    ROW_REF_EVEN: int = int(configs.get(ConfigKeys.ROW_REF_EVEN.value, None))

    # Check if mandatory configuration values are present
    if not (
        INPUT_XLSX_NAME
        and MODEL_XLSX_NAME
        and NUM_TARGET_FILE
        and TABLE_START_ROW
        and HEADER_ROWS
        and ROW_REF_EVEN
        and ROW_REF_ODD
    ):
        logger.error("Input configuration missing.")
        exit(-1)

    # Define file paths for input Excel, CSV, output folder, and model Excel file
    INPUT_XLSX_PATH: str = os.path.join(CWD, "input", f"{INPUT_XLSX_NAME}.xlsx")
    INPUT_CSV_PATH: str = os.path.join(CWD, "input", f"{INPUT_XLSX_NAME}.csv")
    OUTPUT_FOLDER: str = os.path.join(CWD, "output", INPUT_XLSX_NAME)
    MODEL_XLSX_PATH: str = os.path.join(CWD, "input", f"{MODEL_XLSX_NAME}.xlsx")

    # If the --csv option is not specified, generate a CSV from the Excel file
    if not args.csv:
        logger.info(f"Generating CSV file from {INPUT_XLSX_PATH}...")
        excel_to_csv(
            input_file_excel=INPUT_XLSX_PATH,
            output_file_csv=INPUT_CSV_PATH,
            delimiter=";",  # CSV delimiter (using this since some fields may contain commas: ',')
        )
        logger.info(f"CSV created: {INPUT_CSV_PATH}")
    else:
        logger.info(f"Using existing CSV file: {INPUT_CSV_PATH}")

    # Split the CSV into multiple Excel files using the specified model for formatting
    logger.info(f"Splitting CSV into {NUM_TARGET_FILE} Excel files...")

    split_csv_to_excel(
        model_xlsx_path=MODEL_XLSX_PATH,
        source_csv_file=INPUT_CSV_PATH,
        output_folder=OUTPUT_FOLDER,
        product_name=INPUT_XLSX_NAME,
        N=NUM_TARGET_FILE,
        table_start_row=TABLE_START_ROW,
        header_rows=HEADER_ROWS,
        row_ref_odd=ROW_REF_ODD,
        row_ref_even=ROW_REF_EVEN,
    )

    logger.info(f"Files successfully created in {OUTPUT_FOLDER}")


if __name__ == "__main__":
    main()
