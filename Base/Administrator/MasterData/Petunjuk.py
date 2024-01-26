from seleniumbase import BaseCase

from faker import Faker
import sys
sys.path.append('C:/Users/user/Documents/TRCH/KPK/eLkhpn')

from config.userlogin import user

fake = Faker('id_ID')
textfield = fake.text()[:50]

file_input = "input[type=file]" 
file_path = "C:/Users/user/Documents/TRCH/KPK/eLkhpn/assets/image/barcode.jpg" 
class inputpetunjuk(user): 
  def test_MDP(self):  
    self.loginapp("test-user", "martanegara")
    self.open("https://frontend.elhkpn.devel.torche-indonesia.com/administrator/master/efilling-guides")
    self.sleep(3)
    for i in range(5):
      self.click('#efilling-guides-button-page-create')
      self.input('#efilling-guides-input-text-guide_name',textfield)
      self.input('#efilling-guides-input-text-guide_title',textfield)
      self.input('.ck-blurred.ck.ck-content.ck-editor__editable.ck-rounded-corners.ck-editor__editable_inline',textfield)
      self.sleep(1)
      self.click('#efilling-guides-button-modal-create')
      
    input("Press Enter to exit...")

