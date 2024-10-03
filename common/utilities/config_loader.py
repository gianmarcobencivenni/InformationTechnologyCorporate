import json
from typing import Optional, Dict


def load_json_configs_dict(json_path: str) -> Optional[Dict]:
    """
    Loads a JSON configuration file from the specified path and returns it as a dictionary.

    Args:
        json_path (str): The file path to the JSON configuration file.

    Returns:
        Optional[Dict]: A dictionary containing the configuration data if the file is successfully loaded,
                        or None if the file is not found.
    """
    try:
        # Open the JSON file and load its contents as a dictionary
        with open(json_path, "r", encoding="utf-8") as jsonfile:
            configs: Dict = json.load(jsonfile)
            return configs

    except FileNotFoundError:
        # Return None if the file does not exist
        return None
