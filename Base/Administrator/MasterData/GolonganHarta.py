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
    self.open("https://frontend.elhkpn.devel.torche-indonesia.com/administrator/master/asset-groups")
    time.sleep(4)
    
    excel_path = "C:/Users/user/Documents/TRCH/KPK/eLkhpn/assets/data/MasterData.xlsx"
    sheet_name = "Jenis Pelepasan Harta"
    excel_data = self.read_data_from_excel(excel_path, sheet_name)
    for index, row in excel_data.iterrows():
      time.sleep(1)
      self.click("#asset-disposal-types-button-page-create")
      # Find the form elements and send data from Excel
      self.type("#asset-disposal-types-input-text-nama", str(row["Jenis Pelepasan Harta"]))
      # ...
      self.click("#asset-disposal-types-button-modal-create")
      time.sleep(1)