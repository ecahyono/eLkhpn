from seleniumbase import BaseCase
import time
from faker import Faker
import sys
import random
sys.path.append('C:/Users/user/Documents/TRCH/KPK/eLkhpn')

from config.userlogin import user

fake = Faker('id_ID')

file_input = "input[type=file]" 
file_path = "C:/Users/user/Documents/TRCH/KPK/eLkhpn/assets/image/barcode.jpg" 

kategori = ['Pengertian dan Konsep','Pengisian Data','Pengisi e-LHKPN','Lainnya']
kategori_terpilih = random.choice(kategori)

class input(user): 
  def test_MDP(self):
    self.loginapp("test-user", "martanegara")
    self.open("https://frontend.elhkpn.devel.torche-indonesia.com/administrator/faq")
    time.sleep(3)
    for i in range(10): 
      self.click('#daftar-faq-button-page-create')
      self.click('[aria-label="Pilih Kategori"]')
      self.click(f'[aria-label="{kategori_terpilih}"]')
      self.input('#daftar-faq-input-text-pertanyaan','Pertanyaan dari kami adalah')
      self.input('.ck.ck-content.ck-editor__editable.ck-rounded-corners.ck-editor__editable_inline.ck-blurred','Jawaban dari kami adalah')
      time.sleep(1)
      self.click(".cursor-pointer.inline-flex.relative.select-none.align-bottom.w-6.h-6")
      self.click("#daftar-faq-button-modal-save")
      time.sleep(2)