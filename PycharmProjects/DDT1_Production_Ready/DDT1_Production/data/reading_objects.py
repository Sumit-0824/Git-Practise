from pathlib import Path
from openpyxl import load_workbook

DATA_FILE = Path(__file__).resolve().parent / "test_data.xlsx"

def read_sheet(sheet_name):
    wb = load_workbook(DATA_FILE, data_only=True)
    ws = wb[sheet_name]
    rows = list(ws.iter_rows(values_only=True))
    headers = [str(x).strip() if x is not None else "" for x in rows[0]]
    return [dict(zip(headers, row)) for row in rows[1:] if any(v is not None for v in row)]

def read_test_data():
    return read_sheet("login_order")
