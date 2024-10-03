from enum import Enum


class ConfigKeys(Enum):
    """JSON Configuration file keys"""

    INPUT_XLSX_NAME = "input_xlsx_name"
    MODEL_XLSX_NAME = "model_xlsx_name"
    SOURCE_CSV_PATH = "source_csv_path"
    NUM_TARGET_FILE = "num_target_file"
