from seleniumbase import BaseCase
import sys
import os
from dotenv import load_dotenv
load_dotenv()

python_path = os.environ.get("PYTHONPATH")
sys.path.append(python_path)
from config.userlogin import user
from config.readdataexternal import readfile
from config.faker import *
sys.path.append(os.environ.get("BASEPATH"))
from eFiling.tiapstep import step

from Base.eAudit.Pemeriksaan.tiaptabpemeriksaan import tiaptabpemeriksaan

class inputklarifikasi(user, readfile, step, tiaptabpemeriksaan):
  def test_klarifikasi(self):
    self.loginapp("checking", "Martanegara@68")
    self.sleep(3)
    url = 'https://frontend.elhkpn.devel.torche-indonesia.com/administrator/e-audit/pemeriksaan'
    self.open(url)
    self.sleep(2)
    # self.cetakKKP()
    # self.inputtanggalklarifikasi()
    # self.inputhasilklarifikasi()
      


    # # datapribadi
    # self.kladatapribadi()
    # #Jabatan
    # self.click('#tab-jabatan')
    # self.klaJabatan()
    # keluarga
    self.click('#tab-keluarga')
    self.klarifikasiKeluarga()
   
    # #Harta
    # self.click('#tab-harta')
    # #Harta

    # # self.click('#tab-penerimaan')
    # #penerimaan#penerimaan#penerimaan#penerimaan#penerimaan
    # num_elements = 5
    # for index in range(num_elements):
    #   idinput = f"#input-penerimaan-harta-usaha-penyelenggara-negara-{index}"
    #   idinput1 = f"#input-penerimaan-harta-usaha-pasangan-{index}"
    #   idcatatan = f"#input-penerimaan-harta-usaha-text-{index}"
    #   self.type(idinput,nilaiuang)
    #   self.type(idinput1,nilaiuang)
    #   self.type(idcatatan,alamat)
    # self.click('#usaha-button-save')
    # self.click('#tab-penerimaan-usaha')
    # num_elements2 = 5
    # for index2 in range(num_elements2):
    #   idinput2 = f"#input-penerimaan-harta-pekerjaan-penyelenggara-negara-{index2}"
    #   idcatatan2 = f"#input-penerimaan-harta-pekerjaan-text-{index}"
    #   self.type(idinput2,nilaiuang)
    #   self.type(idcatatan2,alamat)
    # self.click('#pekerjaan-button-save')
    # self.click("#tab-penerimaan-lainnya")
    # num_elements3 = 4
    # for index3 in range(num_elements3):
    #   idnyatd3 = f"#input-penerimaan-harta-lainnya-text-{index3}"
    #   idinput3 = f"#input-penerimaan-harta-lainnya-penyelenggara-negara-{index3}"
    #   self.type(idnyatd3, alamat)
    #   self.type(idinput3, nilaiuang)
    # self.click('#lainnya-button-save')
    # self.click('#usaha-button-next')
    # #pengeluaran#pengeluaran#pengeluaran#pengeluaran
    # keluarnum = 4
    # for klwar in range(keluarnum):
    #   idinputkeluar = f"#input-penerimaan-harta-pekerjaan-penyelenggara-negara-{klwar}"
    #   idcatatankeluar = f"#input-penerimaan-harta-pekerjaan-text-{klwar}"
    #   self.type(idinputkeluar,nilaiuang)
    #   self.type(idcatatankeluar,alamat)
    # self.click('#pekerjaan-button-save')
    # self.click('#tab-pengeluaran-harta')
    # keluarnum2 = 3
    # for klwar2 in range(keluarnum2):
    #   kelaurharta = f"#input-penerimaan-harta-lainnya-penyelenggara-negara-{klwar2}"
    #   catatkeluar2 = f"#input-penerimaan-harta-lainnya-text-{klwar}"
    #   self.type(kelaurharta,nilaiuang)
    #   self.type(catatkeluar2,alamat)
    # self.click('#lainnya-button-save')
    # self.click("#tab-pengeluaran-lainnya")
    # keluarnum3 = 3
    # for klwar3 in range(keluarnum3):
    #   klert = f"#input-penerimaan-harta-lainnya-penyelenggara-negara-{klwar3}"
    #   incat = f"#input-penerimaan-harta-lainnya-text-{klwar3}"
    #   self.type(klert, alamat)
    #   self.type(incat, nilaiuang)
    # self.click('#lainnya-button-save')

    self.click('#tab-fasilitas')
    self.lampiranfasilitas()

    # self.click('#tab-catatan')
    # self.input('#catatan-input-text-catatan-pemeriksaan', alamat, tanggal_sebelumnya)
    # self.click('#catatan-button-simpan-catatan')

    # self.click('#tab-final')
    # self.click('#final-button-ikhtisar-harta-klarifikasi')
    # self.click('#final-button-save-and-send')


    


 