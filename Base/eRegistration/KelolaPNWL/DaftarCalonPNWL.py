from seleniumbase import BaseCase
import sys
import os
from dotenv import load_dotenv
load_dotenv()
python_path = os.environ.get("PYTHONPATH")
sys.path.append(python_path)
from config.userlogin import user
from config.faker import *

class test_input(user):
  def test_MDP(self):
    self.loginapp("test-user", "martanegara")
    self.sleep(3)
    UserNIK = "3175071308136667"
    useremail = 'cahlima589@gmail.com'
    usernotelp = '0881022731233'

    self.get('https://frontend.elhkpn.devel.torche-indonesia.com/administrator/e-registration/kelola-pnwl/daftar-individual')
    self.sleep(4)
    self.click('#daftar-individual-button-page-create')
    self.input('#daftar-individual-input-text-nik', UserNIK)
    self.sleep(4)
    self.input('#daftar-individual-input-text-front_degree',"PN")
    self.input('#daftar-individual-input-text-back_degree',"WL")
    self.input('#daftar-individual-input-text-email', useremail)
    self.input('#daftar-individual-input-text-no_hp', usernotelp)
    self.click('#daftar-individual-button-selanjutnya')
    self.sleep(4)
    self.click('#daftar-individual-dropdown-work_unit_agency')
    self.input('#daftar-individual-input-filter-page-instansi',"kesehatan")
    self.click('#daftar-individual-dropdown-work_unit_agency_1')
    self.click('#daftar-individual-dropdown-work_unit')
    self.click('#daftar-individual-dropdown-work_unit_0')
    self.click('#daftar-individual-dropdown-work_sub_unit')
    self.click('#daftar-individual-dropdown-work_sub_unit_0')
    self.click('#daftar-individual-dropdown-position')
    self.click('#daftar-individual-dropdown-position_0')
    input("Cek data dulu trus Klik ENTER")
    self.click('#daftar-individual-button-modal-save')

    input("Cek data dulu trus Klik ENTER")
    self.open('https://frontend.elhkpn.devel.torche-indonesia.com/administrator/e-registration/kelola-pnwl/verifikasi-data-individual')
    self.click('#daftar-individual-button-row-approve-0')
    self.click('#daftar-individual-button-modal-approve')
    input("Cek dulu trus Klik ENTER")
    print("Done Bang")
  
