from seleniumbase import BaseCase
import pandas as pd
import time
import sys
from faker import Faker
sys.path.append('C:/Users/user/Documents/TRCH/KPK/eLkhpn')
from config.userlogin import user
fake = Faker('id_ID')
textfield = fake.text()[:50]

file_input = "input[type=file]" 
file_path = "C:/Users/user/Documents/TRCH/KPK/eLkhpn/assets/image/barcode.jpg" 

class MyTestClass(user):
  def read_data_from_excel(self, excel_path, sheet_name):
    # Read data from Excel using pandas
    df = pd.read_excel(excel_path, sheet_name=sheet_name)
    return df
  def test_fill_form_from_excel(self):
    self.loginapp("test-user", "martanegara")
    time.sleep(3)
    self.open("https://frontend.elhkpn.devel.torche-indonesia.com/administrator/master/currencies")
    time.sleep(4)
    
    excel_path = "C:/Users/user/Documents/TRCH/KPK/eLkhpn/assets/data/MasterData.xlsx"
    sheet_name = "Mata uang"
    excel_data = self.read_data_from_excel(excel_path, sheet_name)
    for index, row in excel_data.iterrows():
      time.sleep(1)
      self.click("#currencies-button-page-create")
      time.sleep(1)
      # Find the form elements and send data from Excel
      self.type("#currencies-input-text-nama", str(row["Nama Mata Uang"]))
      self.type("#currencies-input-text-singkatan", str(row["Singkatan"]))
      self.type("#currencies-input-text-simbol", str(row["Simbol"]))
      self.type("#currencies-input-text-negara", str(row["Negara"]))
      # ...
      self.click("#currencies-button-modal-create")