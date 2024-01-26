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
    self.open("https://frontend.elhkpn.devel.torche-indonesia.com/administrator/faq")
    self.sleep(3)
    for k in range(2):
      for i in range(4): 
        self.click('#daftar-faq-button-page-create')
        self.click('[aria-label="Pilih Kategori"]')
        self.click(f'#daftar-faq-input-dropdown-kategori_{i}')
        self.input('#daftar-faq-input-text-pertanyaan','Apa itu e-Registration?')
        self.input('.ck.ck-content.ck-editor__editable.ck-rounded-corners.ck-editor__editable_inline.ck-blurred','Apa itu e-Registration?')
        self.sleep(1)
        self.click(".cursor-pointer.inline-flex.relative.select-none.align-bottom.w-6.h-6")
        self.click("#daftar-faq-button-modal-save")
        self.sleep(2)