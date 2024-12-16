from seleniumbase import BaseCase
import pandas as pd
import time

class readfile(BaseCase):
  def read_data_from_excel(self, excel_path, sheet_name):
    # Read data from Excel using pandas
    df = pd.read_excel(excel_path, sheet_name=sheet_name)
    return df
  
  def custom_wait_for_element(self, selector, timeout=10):
    start_time = time.time()
    while time.time() < start_time + timeout:
        if self.is_element_present(selector):
            return True
        time.sleep(1)
    raise Exception(f"Element {selector} not found within {timeout} seconds.")