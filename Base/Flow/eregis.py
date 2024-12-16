from seleniumbase import *
import sys

sys.path.append('C:/Users/user/Documents/TRCH/KPK/eLkhpn')
from config.userlogin import user
from config.faker import *

class eregsi(user):
  def daftarkanuserpndanverifikasi(self):
    self.loginapp("test-user","naertanegara")