from seleniumbase import BaseCase
import sys
import os
from dotenv import load_dotenv
load_dotenv()
python_path = os.environ.get("PYTHONPATH")
sys.path.append(python_path)
from config.userlogin import user
from config.faker import *

class test_input(user):
  def test_MDP(self):
    self.loginapp("test-user", "martanegara")
    self.sleep(3)    
    self.sleep(5)
    self.open('https://frontend.elhkpn.devel.torche-indonesia.com/administrator/e-registration/kelola-pnwl/verifikasi-data-individual')
    
    self.click('#daftar-individual-button-row-approve-0')
    self.click('#daftar-individual-button-modal-approve')
    input("Cek dulu trus Klik ENTER")
    print("Done Bang")