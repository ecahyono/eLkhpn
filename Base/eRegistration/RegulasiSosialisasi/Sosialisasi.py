from seleniumbase import *
import time
import pyautogui
import sys

sys.path.append('C:/Users/user/Documents/TRCH/KPK/eLkhpn')
from config.userlogin import user
from config.faker import *


class inputsosialisasi(user): 
  def test_sosialisasi(self):
    self.loginapp("test-user", "martanegara")
    self.open("https://frontend.elhkpn.devel.torche-indonesia.com/administrator/e-registration/regulasi-sosialisasi/sosialisasi")
    time.sleep(3)
    self.click('#sosialisasi-button-page-create')
    time.sleep(2)
    self.wait_for_element_clickable('#sosialisasi-dropdown-instansi', timeout=10)
    self.click("#sosialisasi-dropdown-instansi")
    self.click("#sosialisasi-dropdown-instansi_3")
    self.click('#sosialisasi-dropdown-unit-kerja')
    self.click('#sosialisasi-dropdown-unit-kerja_0')
    self.click('//div[4]/div[2]/span')
    self.click('#sosialisasi-dropdown-bimtek_1')
    self.input('#sosialisasi-text-area-tempat', textfield)
    self.click('#sosialisasi-input-calendar-tanggal')
    self.wait(1)
    self.click(kliktanggal)
    self.wait(1)
    self.input('#sosialisasi-text-area-waktu-pelaksanaan', textfield)
    self.input('#sosialisasi-text-area-pelaksana', textfield)
    self.input('#sosialisasi-input-text-jumlah-peserta', jumlah)

    self.click('#sosialisasi-button-modal-save')
    Pesan = self.find_element("span.mb-4[data-pc-section='summary']")
    try:
        check = Pesan.text
        print(f"Form submission successful. Message: {check}")
        self.post_message(f"message: {check}")
    except Exception as e:
      print(f"Error: {e}")
      print("Form submission successful, but unable to retrieve the message element.")

 
