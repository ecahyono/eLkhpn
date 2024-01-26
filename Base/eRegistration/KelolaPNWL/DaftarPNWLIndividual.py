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
    UserNIK = nik
    useremail = 'sepululhpuluh@gmail.com'
    usernotelp = telepon

    self.get('https://frontend.elhkpn.devel.torche-indonesia.com/administrator/e-registration/kelola-pnwl/daftar-individual')
    self.sleep(4)
    self.click('#daftar-individual-button-page-create')
    self.input('#daftar-individual-input-text-nik', f'{UserNIK}')
    self.sleep(2)
    self.input('#daftar-individual-input-text-nama',nama)
    self.input('#daftar-individual-input-text-front_degree',"PN")
    self.input('#daftar-individual-input-text-back_degree',"WL")
    self.input('#daftar-individual-input-text-birth_place',alamat)
    self.click("label[for='Laki-laki']")
    self.input('#daftar-individual-input-text-email', useremail)
    self.input('#daftar-individual-input-text-no_hp', f"{usernotelp}")
    self.click('#daftar-individual-button-selanjutnya')
    self.sleep(2)
    self.input('#daftar-individual-input-text-nip_nrp', f'{UserNIK}')
    self.click('#daftar-individual-dropdown-work_unit_agency')
    self.input('#daftar-individual-input-filter-page-instansi',"PEMERINTAH KOTA BANDUNG")
    self.click('#daftar-individual-dropdown-work_unit_agency_0')
    self.click('#daftar-individual-dropdown-work_unit')
    self.click('#daftar-individual-dropdown-work_unit_0')
    self.click('#daftar-individual-dropdown-work_sub_unit')
    self.click('#daftar-individual-dropdown-work_sub_unit_0')
    self.click('#daftar-individual-dropdown-position')
    self.click('#daftar-individual-dropdown-position_0')
    self.click('#daftar-individual-button-modal-save')
    self.sleep(2)
    self.open('https://frontend.elhkpn.devel.torche-indonesia.com/administrator/e-registration/kelola-pnwl/verifikasi-data-individual')
    self.sleep(4)
    self.click('#daftar-individual-button-row-approve-0')
    self.click('#daftar-individual-button-modal-approve')
    input("Cek dulu trus Klik ENTER")
    print("Done Bang")


 
  
