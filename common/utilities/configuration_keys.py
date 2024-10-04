from enum import Enum


class ConfigKeys(Enum):
    """JSON Configuration file keys"""

    INPUT_XLSX_NAME = "input_xlsx_name"
    MODEL_XLSX_NAME = "model_xlsx_name"
    SOURCE_CSV_PATH = "source_csv_path"
    NUM_TARGET_FILE = "num_target_file"
    TABLE_START_ROW = "table_start_row"
    HEADER_ROWS = "header_rows"
    ROW_REF_ODD = "row_ref_odd"
    ROW_REF_EVEN = "row_ref_even"
