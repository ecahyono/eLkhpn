from seleniumbase import BaseCase
from os import environ, path
import time
import sys

sys.path.append('C:/Users/user/Documents/TRCH/KPK/eLkhpn')

from config.userlogin import user
from config.readdataexternal import readfile
from config.faker import *
from eFiling.tiapstep import step


class inputklarifikasi(user, readfile, step):
  def test_klarifikasi(self):
    self.loginapp("checking", "Martanegara@68")
    time.sleep(3)
    url = 'https://frontend.elhkpn.devel.torche-indonesia.com/administrator/e-audit/pemeriksaan'
    self.open(url)
    time.sleep(2)
    submitBAK = '#audit-button-modal-save'
    for i in range(0,5):
      try:
        self.find_element(f'tr[data-p-index="{i}"] span:contains("Baru")')
        print(f'Text "Baru" found in row {i}')
        cetak_button_id = f'audit-button-action-cetak-kkp-{i}'
        self.click(f'#{cetak_button_id}')      
        self.wait_for_element_clickable(cetak_button_id)  
      except:
        print(f"Text 'Baru' not found in row {i}. Continuing...")
      break 
    for j in range(0,5):
      try:
        idbuttontgl= f'audit-button-action-input-tanggal-klarifikasi-{j}'
        self.wait_for_element(f'#{idbuttontgl}')
        print(f'Tombol {idbuttontgl} ketemu di baris {j}')
        self.click(f'#{idbuttontgl}')
        self.click(submitBAK)
      except:
        print(f"Tombol {idbuttontgl} Tidak nemu. Kalem lagi dicari.")  
      break       
    for k in range(0,5):
      try:
        idbuttoninput= f'audit-button-action-input-hasil-klarifikasi-{k}'
        self.wait_for_element(f'#{idbuttoninput}')
        print(f'Tombol {idbuttoninput} ketemu di baris {k}')
        self.click(f'#{idbuttoninput}')
      except:
        print(f"Tombol {idbuttoninput} Tidak nemu. Kalem lagi dicari.")  
      break       
    self.sleep(3)


 