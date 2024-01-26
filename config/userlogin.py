from seleniumbase import BaseCase

class user(BaseCase):
  def loginapp(self, username, password):
    self.open ("https://frontend.elhkpn.devel.torche-indonesia.com")
    self.maximize_window()
    popup = "#cls-popup-lanppg"
    self.wait_for_element_present(popup)
    self.click(popup)
    self.input("#username", username)
    self.input("#password", password)
  
    self.click("#sign-in")
    self.sleep(3)
    popup = "#cls-popup-lanppg"
    self.wait_for_element_present(popup)
    self.click(popup)