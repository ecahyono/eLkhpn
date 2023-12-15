from seleniumbase import BaseCase
import time
from faker import Faker
import sys
sys.path.append('C:/Users/user/Documents/TRCH/KPK/eLkhpn')

from config.userlogin import user

fake = Faker('id_ID')
noreg = fake.random_int(min=100000, max=999999)
text = fake.text()

file_input = "input[type=file]" 
file_path = "C:/Users/user/Documents/TRCH/KPK/eLkhpn/assets/pdf/140820221164035191098.pdf" 
class input(user): 
  def test_MDP(self):
    self.loginapp("test-user", "martanegara")
    self.open("https://frontend.elhkpn.devel.torche-indonesia.com/administrator/e-registration/regulasi-sosialisasi/regulasi")
    time.sleep(3)
    for i in range(5):
        self.click('#regulasi-button-page-create')
        time.sleep(2)
        self.wait_for_element_clickable('#regulasi-dropdown-instansi', timeout=3)
        self.click("#regulasi-dropdown-instansi")
        self.click("#regulasi-dropdown-instansi_3")
        self.input('#regulasi-input-text-nomor-regulasi', noreg )
        self.input('#regulasi-text-area-pengelola-lhkpn', text)
        self.input('#regulasi-text-area-sanksi', text)
        self.input('#regulasi-text-area-wajib-lapor', text)
        self.input('#regulasi-text-area-wajib-lapor', text)
        self.input(file_input, file_path)
        self.click('#regulasi-button-modal-save')
        time.sleep(2)


