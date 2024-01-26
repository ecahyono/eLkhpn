from seleniumbase import BaseCase
import sys
import os
from dotenv import load_dotenv
load_dotenv()
python_path = os.environ.get("PYTHONPATH")
sys.path.append(python_path)
from config.faker import *

submitBAK = '#audit-button-modal-save'
class tiaptabpemeriksaan(BaseCase):
  def cetakKKP(self):
    for i in range(0,5):
      try:
        self.find_element(f'tr[data-p-index="{i}"] span:contains("Baru")')
        print(f'Text "Baru" found in row {i}')
        cetak_button_id = f'audit-button-action-cetak-kkp-{i}'
        self.click(f'#{cetak_button_id}')      
        self.wait_for_element_clickable(cetak_button_id)  
      except:
        print(f"Text 'Baru' not found in row {i}. Continuing...")
      break
  def inputtanggalklarifikasi(self):
    for j in range(0,5):
      try:
        idbuttontgl= f'audit-button-action-input-tanggal-klarifikasi-{j}'
        self.wait_for_element(f'#{idbuttontgl}')
        print(f'Tombol {idbuttontgl} ketemu di baris {j}')
        self.click(f'#{idbuttontgl}')
        self.click(submitBAK)
      except:
        print(f"Tombol {idbuttontgl} Tidak nemu. Kalem lagi dicari.")  
      break  
  def inputhasilklarifikasi(self):
    for k in range(0,5):
      try:
        idbuttoninput= f'audit-button-action-input-hasil-klarifikasi-{k}'
        self.wait_for_element(f'#{idbuttoninput}')
        print(f'Tombol {idbuttoninput} ketemu di baris {k}')
        self.click(f'#{idbuttoninput}')
      except:
        print(f"Tombol {idbuttoninput} Tidak nemu. Kalem lagi dicari.")  
      break       
  
  def kladatapribadi(self):
    self.click('#data-pribadi-button-page-edit')
    self.input('#data-pribadi-textarea-page-alamat-domisili', alamat)
    self.click('#data-pribadi-button-modal-save')
  def klaJabatan(self):
    for c in range(2):
      self.click('#jabatan-button-rangkap-jabatan')
      self.sleep(4)
      self.click('#jabatan-dropdown-lembaga')
      self.click('#jabatan-dropdown-lembaga_3')
      self.click('#jabatan-dropdown-unit-kerja')
      self.click('#jabatan-dropdown-unit-kerja_0')
      self.click('#jabatan-dropdown-sub-unit-kerja')
      self.click('#jabatan-dropdown-sub-unit-kerja_0')
      self.click('#jabatan-dropdown-jabatan')
      self.click('#jabatan-dropdown-jabatan_0')
      self.input('#jabatan-text-alamat', alamat)
      self.click('#jabatan-button-modal-save')
      self.sleep(2)
  def klarifikasiKeluarga(self):
    self.click('#families-button-page-tambah-data-keluarga')
    self.input('#families-input-text-page-nik', nik)
    self.input('#families-input-text-page-nama', nama)
    self.click('#families-dropdown-page-hubungan')
    self.click('#families-dropdown-page-hubungan_4')
    self.input('#families-input-text-page-tempat-lahir', alamat)
    self.click('#families-input-calendar-page-tanggal-lahir')
    self.sleep(3)
    self.click(kliktanggal)
    self.click('#families-input-radio-page-jenis-kelamin')
    self.input('#families-input-text-page-pekerjaan', alamat)
    self.input('#families-input-text-page-nomor-handphone', telepon)
    self.input('#families-input-text-page-alamat', alamat)
    self.click('#families-button-modal-save')


