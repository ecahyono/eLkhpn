from seleniumbase import *
import sys
import os
import pandas as pd
from dotenv import load_dotenv
load_dotenv()
python_path = os.environ.get("PYTHONPATH")
sys.path.append(python_path)

from config.userlogin import user
# from config.readdataexternal import readfile
from config.faker import *

class MyTestClass(user):
  def read_data_from_excel(self, excel_path, sheet_name):
    # Read data from Excel using pandas
    df = pd.read_excel(excel_path, sheet_name=sheet_name)
    return df   
  def test_fill_form_from_excel(self):
    self.loginapp("test-user", "martanegara")
    self.sleep(3)
    self.open("https://frontend.elhkpn.devel.torche-indonesia.com/administrator/master/currencies")
    self.sleep(4)
    
    excel_path = os.environ.get("MASTERDATA")
    sheet_name = "Mata uang"
    excel_data = self.read_data_from_excel(excel_path, sheet_name)
    for index, row in excel_data.iterrows():
      print(f'Processing row {index + 1}: {row}')
      self.sleep(1)
      self.click("#currencies-button-page-create")
      self.sleep(1)
      # Find the form elements and send data from Excel
      self.input("#currencies-input-text-nama", str(row["Nama Mata Uang"]))
      self.input("#currencies-input-text-singkatan", str(row["Singkatan"]))
      self.input("#currencies-input-text-simbol", str(row["Simbol"]))
      self.input("#currencies-input-text-negara", str(row["Negara"]))
      # ...
      self.click("#currencies-button-modal-create")