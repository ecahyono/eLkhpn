from seleniumbase import BaseCase
import sys
import os
from dotenv import load_dotenv
load_dotenv()
python_path = os.environ.get("PYTHONPATH")
sys.path.append(python_path)
from config.userlogin import user
from config.faker import *

class test_kelolaadmininstansi(user):
  def test_EREGKAI (self):
    self.loginapp("test-user","martanegara")
    self.sleep(3)
    self.open("https://frontend.elhkpn.devel.torche-indonesia.com/administrator/e-registration/kelola-admin-instansi")
    self.sleep(3)
    self.click('#agency-admins-button-page-create')
    self.wait_for_element_present('#agency-admins-dropdown-instansi')
    self.input('#agency-admins-input-text-username',nama)
    self.input('#agency-admins-input-text-nama',nama)
    self.input('#agency-admins-input-text-email',fake_email)
    self.input('#agency-admins-input-text-no-tlp',telepon)
    self.input('#agency-admins-input-text-no-sk',nik)
    self.click('#agency-admins-dropdown-instansi')
    self.click('#agency-admins-dropdown-instansi_3')
    self.input('#agency-admins-input-text-work-unit',textfield)
    self.input('#agency-admins-input-text-work-sub-unit',textfield)
    self.input('#agency-admins-input-text-position',textfield)
    self.click('#agency-admins-button-modal-save')
    self.sleep(5)
