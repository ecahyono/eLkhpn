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
    self.open("https://frontend.elhkpn.devel.torche-indonesia.com/administrator/api-instansi")
    self.sleep(2)
    for i in range(2): 
      self.click('#api-instansi-button-generate-api')
      self.wait(3)
      self.click('#api-instansi-input-dropdown-instansi')
      self.click('#api-instansi-input-dropdown-instansi_0')

      self.input('#api-instansi-input-text-email',fake_email)
      self.input('#api-instansi-input-text-password',ulainnya)
      self.input('#api-instansi-input-text-ip-permission',alamat)
      
      listchecklist = ['akses-wajib-lapor','akses-harta','akses-keluarga','akses-pengumuman-batch','akses-report','akses-wajib-lapor-kemenku','akses-harta-kemenku','akses-detail-harta','akses-pelaporan-bkn','akses-satu-data-indonesia']

      for index in listchecklist:
        self.click(f"label[for='api-instansi-input-check-{index}']")
      self.sleep(5)