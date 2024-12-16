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
    #Manajemen Dokumen
    url = 'https://frontend.elhkpn.devel.torche-indonesia.com/administrator/e-audit/pemeriksaan'
    self.open(url)
    # self.sleep(3)
    # for k in range(0,5):
    #   try:
    #     idbutton= f'audit-button-action-manajemen-dokumen-{k}'
    #     self.wait_for_element(f'#{idbutton}')
    #     print(f'Tombol {idbutton} ketemu di baris {k}')
    #     self.click(f'#{idbutton}')
    #   except:
    #     print(f"Tombol {idbutton} Tidak nemu. Kalem lagi dicari.")  
    #   break       
    self.sleep(3)
    self.click('#audit-button-action-manajemen-dokumen-0')
    for i in range(10):
      self.click('#manajemen-dokumen-button-page-create')
      self.type('#manajemen-dokumen-input-text-document_name','Dokumen Contoh')
      self.type(file_input, file_path)
      self.click('#manajemen-dokumen-button-modal-create')
      self.sleep(2)
    

