from seleniumbase import BaseCase
import pandas as pd

class readfile(BaseCase):
  def read_data_from_excel(self, excel_path, sheet_name):
    # Read data from Excel using pandas
    df = pd.read_excel(excel_path, sheet_name=sheet_name)
    return df