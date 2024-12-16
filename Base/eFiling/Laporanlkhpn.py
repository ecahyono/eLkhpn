from seleniumbase import BaseCase
import sys
import os
from dotenv import load_dotenv
load_dotenv()

sys.path.append(os.environ.get("PYTHONPATH"))
from config.userlogin import user
from config.faker import *
from tiapstep import step

userlogin = UserNIK

class efiling(user,step):
  def test_Laporan (self):
    self.loginapp(userlogin, "martanegara")
    # self.loginapp(userlogin, "Martanegara@68")
    try:
      buttonedit = "#filling-button-row-edit-0"
      self.wait_for_element_present(buttonedit, timeout=15)
      self.click(buttonedit)
    except:
      butonnew = "#create-new-lhkpn"
      self.click(butonnew)
      self.sleep(1)
      try:
        self.click('[aria-label="Pilih Status"]')
        self.wait(1)
        self.click((f'[aria-label="{pilihstatuslaporan}"]'))
        self.input("#filling-calendar-tanggal-pelaporan", tanggal_sekarang)
      except: 
        pass
      self.click('#filling-button-modal-next')
    self.sleep(4)

    # #stepdatapribadi
    # self.sleep(4)
    # self.type(file_input, file_path)
    # self.input('#datapribadis-inputtext-page-npwp', userlogin)
    # self.click('#btn-next-stp1')
    # self.click('#datapribadis-input-text-page-alamat')
    # self.input('#datapribadis-inputtext-page-kode-pos','40151')
    # self.click('#btn-prev-stp1')
      
    # Stepjabatan
    # self.click("#efil-stp-2")
    # self.sleep(4)
    # self.jabatan()
    # # StepKeluarga
    # self.click("#efil-stp-3")
    # self.sleep(4)
    # self.keluarga()
      
    ############## Stepharta #################
    self.click("#efil-stp-4")
    self.sleep(4)
    try: 
      self.click('[aria-label="Load Data Sebelumnya"]')
      self.sleep(3)
      self.click('[aria-label="Periksa Data"]')
    except:
      pass
    #####Tanah/Bangunan######
    self.sleep(4)
    self.harta_tanahbangunan()
    #####Alat Transportasi/Mesin######
    self.click('#tab-alat-transportasi-mesin')
    self.sleep(4)
    self.harta_bergerak()
    #####Harta Bergerak Lainnya######
    self.click('#tab-tanah-bergerak-lainnya')
    self.sleep(4)
    self.harta_bergeraklainnya()
    #####Alat surat Berhargan######
    self.click('#tab-surat-berharga')
    self.sleep(4)
    self.harta_suratberharga()
    ####Alat surat Berhargan######
    self.click('#tab-kas-setara-kas')
    self.sleep(4)
    self.harta_kassetarakas()
    #####Alat surat Berhargan######
    self.click('#tab-harta-lainnya')
    self.sleep(4)
    self.harta_lainnya()
    ######HUTANG######
    self.click('#tab-hutang')
    self.sleep(4)
    self.harta_hutang()

    # Step 5
    self.click("#efil-stp-5")
    self.sleep(4)
    klilpopup = "#penerimaan-button-modal-success-edit"
    pengeluaranpupop = "#pengeluaran-button-modal-success-edit"
    nilai = f'{nilaiuang}'
    h1_selector = '.text-2xl.font-semibold'

    #kolompn
    num_elements = 2
    for index in range(num_elements):
      idnyatd = f"#column-penerimaan-dari-pekerjaan-pn-{index}"
      idinput = f"#input-pn-penerimaan-dari-pekerjaan-{index}"

      self.click(idnyatd)
      self.type(idinput, nilai)
      self.click(h1_selector)
      self.click(klilpopup)
    # num_elements1 = 5
    # for index1 in range(num_elements1):
    #   idnyatd1 = f"#column-penerimaan-dari-pekerjaan-pasangan-{index1}"
    #   idinput1 = f"#input-pasangan-penerimaan-dari-pekerjaan-{index1}"

    #   self.click(idnyatd1)
    #   self.type(idinput1, nilai)
    #   self.click(h1_selector)
    #   self.click(klilpopup)
    # #
    # self.click('#tab-penerimaan-dari-usaha-dan-kekayaan')
    # #
    # num_elements2 = 5
    # for index2 in range(num_elements2):
    #   idnyatd2 = f"#column-penerimaan-dari-usaha-dan-kekayaan-{index2}"
    #   idinput2 = f"#input-penerimaan-dari-usaha-dan-kekayaan-{index2}"

    #   self.click(idnyatd2)
    #   self.type(idinput2, nilai)
    #   self.click(h1_selector)
    #   self.click(klilpopup)
    # #
    # self.click("#tab-penerimaan-lainnya")
    # #
    # num_elements3 = 4
    # for index3 in range(num_elements3):
    #   idnyatd3 = f"#column-penerimaan-lainnya-{index3}"
    #   idinput3 = f"#input-penerimaan-lainnya-{index3}"

    #   self.click(idnyatd3)
    #   self.type(idinput3, nilai)
    #   self.click(h1_selector)
    #   self.click(klilpopup)

    # Step 6
    self.click("#efil-stp-6")
    self.sleep(4)

    num_elements4 = 1
    for index4 in range(num_elements4):
      idnyatd4 = f"#column-pengeluaran-rutin-{index4}"
      idinput4 = f"#input-pengeluaran-rutin-{index4}"

      self.click(idnyatd4)
      self.type(idinput4, nilai)
      self.click(h1_selector)
      self.click(pengeluaranpupop)
    # #
    # self.click("#tab-pengeluaran-harta")
    # #
    # num_elements5 = 3
    # for index5 in range(num_elements5):
    #   idnyatd5 = f"#column-pengeluaran-harta-{index5}"
    #   idinput5 = f"#input-pengeluaran-harta-{index5}"

    #   self.click(idnyatd5)
    #   self.type(idinput5, nilai)
    #   self.click(h1_selector)
    #   self.click(pengeluaranpupop)
    # #
    # self.click("#tab-pengeluaran-lainnya")
    # #
    # num_elements6 = 3
    # for index6 in range(num_elements6):
    #   idnyatd5 = f"#column-pengeluaran-lainnya-{index6}"
    #   idinput6 = f"#input-pengeluaran-lainnya-{index6}"

    #   self.click(idnyatd5)
    #   self.type(idinput6, nilai)
    #   self.click(h1_selector)
    #   self.click(pengeluaranpupop)

    # Step 7
    self.click("#efil-stp-7")
    self.sleep(4)
    # Step 8
    self.click("#efil-stp-8")
    self.sleep(4)
    self.lampiranfasilitas()









    

    

    

      

    

