from seleniumbase import BaseCase
import time

userlogin = "superadmin"
file_input = "input[type=file]" 
file_path = "C:/Users/user/Documents/TRCH/KPK/eLkhpn/assets/image/barcode.jpg" 
class test_input(BaseCase):
  def test_MDP(self):
    self.open ("https://frontend.elhkpn.devel.torche-indonesia.com")
    self.maximize_window()
    popup = "#cls-popup-lanppg"
    self.wait_for_element_present(popup)
    self.click(popup)
    self.input("#username", userlogin)
    # self.input("#password", "naufal@Hafizh1001")
    # self.input("#password", "Iqbal@123")
    self.input("#password", "superadmin")
    # self.input("#password", "Galih@123")
    self.click("#sign-in")
    time.sleep(3)

    #Manajemen Dokumen
    self.open("https://frontend.elhkpn.devel.torche-indonesia.com/administrator/e-audit/pemeriksaan/41/manajemen-dokumen")
    time.sleep(3)
    for i in range(10):
      self.click('#manajemen-dokumen-button-page-create')
      self.type('#manajemen-dokumen-input-text-document_name','Dokumen Contoh')
      self.type(file_input, file_path)
      self.click('#manajemen-dokumen-button-modal-create')
      time.sleep(2)

