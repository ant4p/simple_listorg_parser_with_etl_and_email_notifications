import os
import pandas as pd

from dotenv import load_dotenv

load_dotenv()

FILE_PATH = os.getenv('FILE_PATH')
SHEET_NAME = os.getenv('SHEET_NAME')
COLUMN_NAME = os.getenv('COLUMN_NAME')


def get_email_list(file_path, sheet_name, column_name):
    try:
        df = pd.read_excel(file_path, sheet_name=sheet_name)
        if column_name in df.columns:
            column_data = df[column_name].tolist()
            return column_data
        else:
            print(f'Fail: column {column_name} not found in file.')
            return None
    except FileNotFoundError:
        print(f'Fail: file {file_path} not found.')
    except Exception as e:
        print(f'Fail: fail to read file {e}.')
