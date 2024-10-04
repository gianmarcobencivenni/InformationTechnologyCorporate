import argparse


def parse_args():
    # Argument parser setup for command-line options
    parser = argparse.ArgumentParser(description="Process Excel files and split them.")
    parser.add_argument(
        "--extract_csv", action="store_true", help="Use existing CSV file, if present"
    )
    parser.add_argument(
        "--process_csv", action="store_true", help="Process CSV file before split"
    )
    return parser.parse_args()
