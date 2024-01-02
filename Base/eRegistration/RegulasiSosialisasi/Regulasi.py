from seleniumbase import BaseCase
import sys
import os
from dotenv import load_dotenv
load_dotenv()
python_path = os.environ.get("PYTHONPATH")
sys.path.append(python_path)
from config.userlogin import user
from config.faker import *

class input(user): 
  def test_MDP(self):
    self.loginapp("test-user", "martanegara")
    self.open("https://frontend.elhkpn.devel.torche-indonesia.com/administrator/e-registration/regulasi-sosialisasi/regulasi")
    self.sleep(3)
    for i in range(5):
      self.click('#regulasi-button-page-create')
      self.sleep(2)
      self.wait_for_element_clickable('#regulasi-dropdown-instansi', timeout=20)
      self.click("#regulasi-dropdown-instansi")
      self.click("#regulasi-dropdown-instansi_3")
      self.input('#regulasi-input-text-nomor-regulasi', jumlah )
      self.input('#regulasi-text-area-pengelola-lhkpn', textfield)
      self.input('#regulasi-text-area-sanksi', textfield)
      self.input('#regulasi-text-area-wajib-lapor', textfield)
      self.input('#regulasi-text-area-wajib-lapor', textfield)
      self.input(file_input, file_path)
      self.click('#regulasi-button-modal-save')
      self.sleep(2)


