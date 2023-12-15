from seleniumbase import *
import time
import pyautogui
import sys

sys.path.append('C:/Users/user/Documents/TRCH/KPK/eLkhpn')
from config.userlogin import user
from config.faker import *

class test_kelolaadminunitkerja(user):
  def test_EREGKAI (self):
    self.loginapp("test-user","Martanegara@68")
    time.sleep(4)
    self.open("https://frontend.elhkpn.devel.torche-indonesia.com/administrator/e-registration/kelola-admin-unit-kerja")
    time.sleep(4)