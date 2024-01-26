from seleniumbase import BaseCase

from faker import Faker
import sys
sys.path.append('C:/Users/user/Documents/TRCH/KPK/eLkhpn')

from config.userlogin import user

fake = Faker('id_ID')

file_input = "input[type=file]" 
file_path = "C:/Users/user/Documents/TRCH/KPK/eLkhpn/assets/image/barcode.jpg" 
class input(user): 
  def test_MDP(self):  
    self.loginapp("test-user", "martanegara")
    self.open("https://frontend.elhkpn.devel.torche-indonesia.com/administrator/e-audit/penugasan")
    self.sleep(3)
    self.click('#penugasan-input-dropdown-page-status-penugasan')
    self.sleep(2)

