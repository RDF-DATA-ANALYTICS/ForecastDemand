import argparse
import logging
import shutil

import kagglehub

def download_m5() -> str:
    # Download latest version
    path = kagglehub.competition_download('m5-forecasting-accuracy')
    return path


def parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Download M5 competition data")
    parser.add_argument(
        "--path",
        type=str,
        default=None,
        help="Path to download the M5 competition data. If not provided, the data will be downloaded to the default Kaggle cache directory.",
    )
    return parser

if __name__ == "__main__":
    args = parser().parse_args()
    path = download_m5()

    if args.path:
        shutil.move(path, args.path)
        logging.info(f"Moved M5 competition data to {args.path}")
    else:
        logging.info(f"M5 competition data downloaded to {path}")