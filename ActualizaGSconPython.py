import csv
import time
import gspread
import pandas as pd
from oauth2client.service_account import ServiceAccountCredentials
from gspread_dataframe import get_as_dataframe, set_with_dataframe


def actualiza_google_spreadsheets():
    scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
    cred = ServiceAccountCredentials.from_json_keyfile_name('credencials.json',scope)
    client = gspread.authorize(cred)
    gs1 = client.open_by_key('********************************************')

# lee archivo
    nombre_archivo = 'test.csv'
    with open(nombre_archivo, mode="r", newline="") as file:
        reader = csv.reader(file)
        rows = list(reader)

    rows = pd.DataFrame(rows)

    worksheet = gs1.get_worksheet(0)
    worksheet.clear()
    set_with_dataframe(worksheet, rows)

    return

actualiza_google_spreadsheets()
