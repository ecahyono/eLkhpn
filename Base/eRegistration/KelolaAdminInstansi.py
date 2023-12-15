from seleniumbase import *
import time
import pyautogui
import sys

sys.path.append('C:/Users/user/Documents/TRCH/KPK/eLkhpn')
from config.userlogin import user
from config.faker import *

class test_kelolaadmininstansi(user):
  def test_EREGKAI (self):
    self.loginapp("test-user","martanegara")
    time.sleep(4)
    self.open("https://frontend.elhkpn.devel.torche-indonesia.com/administrator/e-registration/kelola-admin-instansi")
    time.sleep(4)
    self.click('#agency-admins-button-page-create')
    self.input('#agency-admins-input-text-nama','nama')
    self.input('#agency-admins-input-text-email','email@gmail.com')
    # self.input('#agency-admins-input-text-nama','0994857345345')
    # self.input('#agency-admins-input-text-nama','SK---n834756')
    self.click('#agency-admins-dropdown-instansi')
    self.click('#agency-admins-dropdown-instansi_3')
    self.input('#agency-admins-input-text-work-unit','nama')
    self.input('#agency-admins-input-text-work-sub-unit','nama')
    self.input('#agency-admins-input-text-position','nama')
    input()