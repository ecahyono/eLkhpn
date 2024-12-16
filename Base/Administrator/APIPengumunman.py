from seleniumbase import *
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
    self.open("https://frontend.elhkpn.devel.torche-indonesia.com/administrator/api-pengumuman")
    self.sleep(2)
    for i in range(2): 
      self.click('#api-pengumuman-button-generate-api')
      self.wait(3)
      self.click('#api-instansi-input-dropdown-instansi')
      self.click('#api-instansi-input-dropdown-instansi_0')
      self.input(file_input,file_path)
      self.input('#api-pengumuman-input-text-link-web', fakeurl)
      self.input('#api-pengumuman-input-text-link-web',fakeurl)
