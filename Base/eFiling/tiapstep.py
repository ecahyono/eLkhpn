from seleniumbase import BaseCase
import sys
import os
from dotenv import load_dotenv
load_dotenv()
python_path = os.environ.get("PYTHONPATH")
sys.path.append(python_path)
from config.faker import *
from config.readdataexternal import readfile

class step(readfile):
  def jabatan(self):
    self.custom_wait_for_element('#tanah-bangunan-btn-ambil-data-dari-bpn')
    for c in range(1):
      self.click('#btn-create-rangkap-jabatan')
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
  def keluarga(self):
    listtgl = [usuami,uistri,uanak,uanakBT,ulainnya]
    for a in range(4):
      self.click('#data-keluarga-button-page-tambah-data-keluarga')
      self.sleep(3)
      self.click(".p-hidden-accessible #data-keluarga-input-radio-jenis-kewarganegaraan-wni")
      self.input('#data-keluarga-input-text-page-nik', nik)
      self.input('#data-keluarga-input-text-page-nama', nama)
      self.click('#data-keluarga-dropdown-page-hubungan')
      self.click(f'#data-keluarga-dropdown-page-hubungan_{a}')
      self.input('#data-keluarga-input-text-page-tempat-lahir', alamat)
      print(listtgl)
      input('leriufbsldjfbsdlfuukhnldfsk')
      self.input('#data-keluarga-input-calendar-page-tanggal-lahir',f'{listtgl}')
      # self.click('#data-keluarga-input-radio-jenis-kelamin-perempuan')
      self.click('#data-keluarga-input-radio-jenis-kelamin-laki-laki')
      self.input('#data-keluarga-input-text-page-pekerjaan', alamat)
      self.input('#data-keluarga-input-text-page-nomor-handphone', telepon)
      # self.input('#data-keluarga-input-text-page-alamat', alamat)
      self.click('#data-keluarga-input-text-page-alamat')
      self.click('#data-keluarga-button-modal-save')
  def harta_tanahbangunan(self):
    butonselanjutnya = "#tanah-bangunan-button-selanjutnya"
    ######Tanah/Bangunan######
    # self.click("#tanah-bangunan-btn-ambil-data-dari-bpn")
    # input("EDIT SENDIRI Data Dari BPN nya oke klo udah klik ENTER")
    for i in range(1):
      self.click("#tanah-bangunan-btn-create")
      self.sleep(2)
      self.click("#tanah-bangunan-dropdown-country-from")
      self.click("#tanah-bangunan-dropdown-country-from_0")
      self.click("#tanah-bangunan-dropdown-provinsi")
      self.input("#tanah-bangunan-input-filter-page-provinsi","Lampung")
      self.click("#tanah-bangunan-dropdown-provinsi_0")
      self.click("#tanah-bangunan-dropdown-kabupaten-kota")
      self.click("#tanah-bangunan-dropdown-kabupaten-kota_0")
      self.click("#tanah-bangunan-dropdown-kecamatan")
      self.click("#tanah-bangunan-dropdown-kecamatan_0")
      self.click("#tanah-bangunan-dropdown-kelurahan")
      self.click("#tanah-bangunan-dropdown-kelurahan_0")
      self.input("#tanah-bangunan-input-text-street", "jl Sarijadi sariasih no 38")
      self.type("input[placeholder='Masukkan Luas Tanah']", "500")
      self.type("input[placeholder='Masukkan Luas Bangunan']", "500")
      self.click(butonselanjutnya)
      self.click("#tanah-bangunan-dropdown-evidence_type")
      self.click("#tanah-bangunan-dropdown-evidence_type_0")
      self.input("#tanah-bangunan-input-text-evidence_number", "500")
      self.click("#tanah-bangunan-input-checkbox-atas-nama-pn_yang_bersangkutan")
      # self.click("#tanah-bangunan-input-checkbox-atas-nama-pasangan_anak")
      # self.click("#tanah-bangunan-input-checkbox-atas-nama-lainnya")
      # self.click("#tanah-bangunan-dropdown-child_couple")
      # self.click("#tanah-bangunan-dropdown-child_couple_0")
      # self.input("#tanah-bangunan-input-text-other_info","nama pasangan")

      self.click("#tanah-bangunan-input-checkbox-asal-usul-hasil_sendiri")
      
      TanggalTransaksi  = "#tanah-bangunan-input-calendar-transaction_date"
      keterangan        = "#tanah-bangunan-input-text-asset_description"
      namapihk2         = "#tanah-bangunan-input-text-name"
      alamatpihk2       ="#tanah-bangunan-input-text-address"
      modalsavebtn      = '#tanah-bangunan-button-modal-save'
      list_checkbox     = ["#tanah-bangunan-input-checkbox-asal-usul-warisan"]
                    # '#tanah-bangunan-input-checkbox-asal-usul-hibah_dengan_akta',
                    # '#tanah-bangunan-input-checkbox-asal-usul-hibah_tanpa_akta',
                    # '#tanah-bangunan-input-checkbox-asal-usul-hadiah',
                    # '#tanah-bangunan-input-checkbox-asal-usul-lainnya']

      for checkbox_id in list_checkbox:
        self.click(checkbox_id)
        self.click(TanggalTransaksi)
        self.click(kliktanggal)
        self.input(BesarNilai,nilaiuang)
        self.input(keterangan,"Asal Usul Harta")
        self.input(namapihk2,"Pemberi Harta")
        self.input(alamatpihk2,"Alamat Pemberi Harta")
        self.click(modalsavebtn)

      self.click(butonselanjutnya)
      self.click("#tanah-bangunan-input-checkbox-pemanfaatan-tempat_tinggal")
      self.click("#tanah-bangunan-input-checkbox-pemanfaatan-disewakan")
      self.click("#tanah-bangunan-input-checkbox-pemanfaatan-pertanian")
      self.click("#tanah-bangunan-input-checkbox-pemanfaatan-lainnya")
      self.input("input[placeholder='Masukkan Nilai Perolehan']", nilaiuang)
      self.input("input[placeholder='Masukkan Nilai Esitimasi Saat Pelaporan']", nilaiuang)
      self.click("#tanah-bangunan-input-calendar-acquisition_year")
      self.click(pilihtahun)
      self.click(modalsavebtn)
      self.sleep(3)
  def harta_bergerak(self):
    tab2selanjutnya = "#harta-bergerak-button-selanjutnya"
    # self.click("#harta-bergerak-btn-ambil-data-dari-bapenda")
    # input("EDIT SENDIRI Data Dari BPN nya oke klo udah klik ENTER")
    for j in range (1):
      self.click("#harta-bergerak-btn-create")
      self.sleep(2)
      self.click("#harta-bergerak-dropdown-asset-type")
      self.click("#harta-bergerak-dropdown-asset-type_0")
      self.input("#harta-bergerak-input-text-brand", "Transportasi")
      self.input("#harta-bergerak-input-text-model", "Model")
      self.click("#harta-bergerak-input-calendar-production_year")
      self.click(pilihtahun)
      self.input("#harta-bergerak-input-text-registration_police_number", "D 4517 ATU")
      self.click(tab2selanjutnya)
      self.click('#harta-bergerak-dropdown-evidence_type')
      self.click('#harta-bergerak-dropdown-evidence_type_0')
      self.click("#harta-bergerak-input-checkbox-atas-nama-pn_yang_bersangkutan")
      # self.click("#harta-bergerak-input-checkbox-atas-nama-pasangan_anak")
      # self.click("#harta-bergerak-input-checkbox-atas-nama-lainnya")
      # self.click("#harta-bergerak-dropdown-couple_children")
      # self.click("#harta-bergerak-dropdown-couple_children_0")
      # self.input('#harta-bergerak-input-text-other_info', 'nama orang')

      self.click("#harta-bergerak-input-checkbox-asal-usul-hasil_sendiri")

      TanggalTransaksi2 = "#harta-bergerak-input-calendar-transaction_date"
      keterangan2       = "#harta-bergerak-input-text-asset_description"
      namapihk22        = "#harta-bergerak-input-text-name"
      alamatpihk22      ="#harta-bergerak-input-text-address"
      modalsavebtn2     = '#harta-bergerak-button-modal-save'
      list_checkbox2    = ["#harta-bergerak-input-checkbox-asal-usul-warisan"]
                      # '#harta-bergerak-input-checkbox-asal-usul-hibah_dengan_akta',
                      # '#harta-bergerak-input-checkbox-asal-usul-hibah_tanpa_akta',
                      # '#harta-bergerak-input-checkbox-asal-usul-hadiah',
                      # '#harta-bergerak-input-checkbox-asal-usul-lainnya']

      for checkbox_id2 in list_checkbox2:
        self.click(checkbox_id2)
        self.click(TanggalTransaksi2)
        self.click(kliktanggal)
        self.input(BesarNilai,nilaiuang)
        self.input(keterangan2,"Asal Usul Harta")
        self.input(namapihk22,"Pemberi Harta")
        self.input(alamatpihk22,"Alamat Pemberi Harta")
        self.click(modalsavebtn2)
     
      self.click(tab2selanjutnya)
      self.click("#harta-bergerak-dropdown-utilization")
      self.click("#harta-bergerak-dropdown-utilization_0")
      self.input("input[placeholder='Masukkan Nilai Perolehan']", nilaiuang)
      self.input("input[placeholder='Masukkan Nilai Esitimasi Saat Pelaporan']", nilaiuang)
      self.click("#harta-bergerak-input-calendar-early_acquisition_year")
      self.click(pilihtahun)
      self.click(modalsavebtn2)
      self.sleep(3)
  def harta_bergeraklainnya(self):
    for k in range (1):
      self.click("#harta-bergerak-lainnya-btn-create")
      self.sleep(2)
      self.click("#harta-bergerak-lainnya-dropdown-asset-type")
      self.click("#harta-bergerak-lainnya-dropdown-asset-type_0")
      self.input("input[placeholder='Masukkan Jumlah']","10")
      self.input("#harta-bergerak-lainnya-input-text-unit","unit")
      self.input("#harta-bergerak-lainnya-input-text-description","Keterangan Data Harta Bergerak Lainnya")
      self.click("#harta-bergerak-lainnya-input-calendar-early_acquisition_year")
      self.click(pilihtahun)
      self.click("#harta-bergerak-lainnya-input-checkbox-asal-usul-hasil_sendiri")
      TanggalTransaksi3   = "#harta-bergerak-lainnya-input-calendar-transaction_date"
      keterangan3         = "#harta-bergerak-lainnya-input-text-asset_description"
      namapihk23          = "#harta-bergerak-lainnya-input-text-name"
      alamatpihk23        = "#harta-bergerak-lainnya-input-text-address"
      modalsavebtn3       = '#harta-bergerak-lainnya-button-modal-save'

      list_checkbox3      = ["#harta-bergerak-lainnya-input-checkbox-asal-usul-warisan"]
                        # '#harta-bergerak-lainnya-input-checkbox-asal-usul-hibah_dengan_akta',
                        # '#harta-bergerak-lainnya-input-checkbox-asal-usul-hibah_tanpa_akta',
                        # '#harta-bergerak-lainnya-input-checkbox-asal-usul-hadiah',
                        # '#harta-bergerak-lainnya-input-checkbox-asal-usul-lainnya']

      for checkbox_id3 in list_checkbox3:
        self.click(checkbox_id3)
        self.click(TanggalTransaksi3)
        self.click(kliktanggal)
        self.input(BesarNilai,nilaiuang)
        self.input(keterangan3,"Asal Usul Harta")
        self.input(namapihk23,"Pemberi Harta")
        self.input(alamatpihk23,"Alamat Pemberi Harta")
        self.click(modalsavebtn3)
      
      self.input("input[placeholder='Masukkan Nilai Perolehan']", nilaiuang)
      self.input("input[placeholder='Masukkan Nilai Estimasi Saat Laporan']",nilaiuang)
      self.click("#harta-bergerak-lainnya-button-modal-create")
      self.sleep(3)
  def harta_suratberharga(self):
    tab4selanjutnya = "#surat-berharga-button-selanjutnya"
    for l in range(1):
      self.click('#surat-berharga-btn-create')
      self.sleep(2)
      self.input("#surat-berharga-input-text-account_number","497066923")
      self.type(file_input, file_path)
      self.click('#surat-berharga-dropdown-asset-type')
      self.click('#surat-berharga-dropdown-asset-type_0')
      self.click(tab4selanjutnya)
      self.input("#surat-berharga-input-text-publisher_name","Penerbit/perusahaan")
      self.input("#surat-berharga-input-text-custodian","sekuritas/custodian")
      self.click("#surat-berharga-input-checkbox-atas-nama-pn_yang_bersangkutan")
      # self.click("#surat-berharga-input-checkbox-atas-nama-pasangan_anak")
      # self.click("#surat-berharga-input-checkbox-atas-nama-lainnya")
      # self.click("#surat-berharga-dropdown-child_couple")
      # self.click("#surat-berharga-dropdown-child_couple_0")
      # self.input('#surat-berharga-input-text-other_description', 'nama orang')
      self.click("#surat-berharga-input-checkbox-asal-usul-hasil_sendiri")
      TanggalTransaksi4 = "#surat-berharga-input-calendar-transaction_date"
      keterangan4       = "#surat-berharga-input-text-asset_description"
      namapihk24        = "#surat-berharga-input-text-name"
      alamatpihk24      ="#surat-berharga-input-text-address"
      modalsavebtn4     = '#surat-berharga-button-modal-save'

      list_checkbox4    = ["#surat-berharga-input-checkbox-asal-usul-warisan"]
                          # '#surat-berharga-input-checkbox-asal-usul-hibah_dengan_akta',
                          # '#surat-berharga-input-checkbox-asal-usul-hibah_tanpa_akta',
                          # '#surat-berharga-input-checkbox-asal-usul-hadiah',
                          # '#surat-berharga-input-checkbox-asal-usul-lainnya']

      for checkbox_id4 in list_checkbox4:
        self.click(checkbox_id4)
        self.click(TanggalTransaksi4)
        self.click(kliktanggal)
        self.input(BesarNilai,nilaiuang)
        self.input(keterangan4,"Asal Usul Harta")
        self.input(namapihk24,"Pemberi Harta")
        self.input(alamatpihk24,"Alamat Pemberi Harta")
        self.click(modalsavebtn4)

      self.click(tab4selanjutnya)
      self.input("input[placeholder='Masukkan Nilai Perolehan']",nilaiuang)
      self.input("input[placeholder='Masukkan Nilai Esitimasi Saat Pelaporan']",nilaiuang)
      self.click("#surat-berharga-input-calendar-early_acquisition_year")
      self.click(pilihtahun)
      self.click(modalsavebtn4)
      self.sleep(3)
  def harta_kassetarakas(self):
    tab3selanjutnya2 = "#harta-kas-button-selanjutnya"
    for m in range(1):
      self.click("#harta-kas-btn-create")
      self.sleep(2)
      self.click("#harta-kas-dropdown-asset-type")
      self.click("#harta-kas-dropdown-asset-type_1")
      self.type(file_input, file_path)
      self.input("#harta-kas-input-text-bank_name","KPK BANK")
      self.input("#harta-kas-input-text-number_account",telepon)
      self.click("#harta-kas-input-calendar-open_account_year")
      self.click(pilihtahun)
      self.click("#harta-kas-input-checkbox-atas-nama-pn_yang_bersangkutan")
      # self.click("#harta-kas-input-checkbox-atas-nama-pasangan_anak")
      # self.click("#harta-kas-input-checkbox-atas-nama-lainnya")
      # self.click("#harta-kas-dropdown-child_couple")
      # self.click("#harta-kas-dropdown-child_couple_0")
      # self.input('#harta-kas-input-text-on_another_name', 'nama orang')
      self.click("#harta-kas-input-checkbox-asal-usul-hasil_sendiri")
      TanggalTransaksi5 = "#harta-kas-input-calendar-transaction_date"
      keterangan5       = "#harta-kas-input-text-asset_description"
      namapihk25        = "#harta-kas-input-text-name"
      alamatpihk25      = "#harta-kas-input-text-address"
      modalsavebtn5     = '#harta-kas-button-modal-save'

      list_checkbox5    = ['#harta-kas-input-checkbox-asal-usul-lainnya']
                        # '#harta-kas-input-checkbox-asal-usul-hibah_dengan_akta',
                        # '#harta-kas-input-checkbox-asal-usul-hibah_tanpa_akta',
                        # '#harta-kas-input-checkbox-asal-usul-hadiah',
                        # "#harta-kas-input-checkbox-asal-usul-warisan"]

      for checkbox_id5 in list_checkbox5:
        self.click(checkbox_id5)
        self.click(TanggalTransaksi5)
        self.click(kliktanggal)
        self.input(BesarNilai,nilaiuang)
        self.input(keterangan5,"Asal Usul Harta")
        self.input(namapihk25,"Pemberi Harta")
        self.input(alamatpihk25,"Alamat Pemberi Harta")
        self.click(modalsavebtn5)
      self.click(tab3selanjutnya2)
      self.wait_for_element_clickable("#harta-kas-input-number-balance_value",timeout=20)
      self.type("#harta-kas-input-number-balance_value","25000000")
      self.click(modalsavebtn5)
      self.sleep(3)
  def harta_lainnya(self):
    for g in range(1):
      self.click("#harta-lainnya-btn-create")
      self.sleep(2)
      self.click('#harta-lainnya-dropdown-asset-type')
      self.click('#harta-lainnya-dropdown-asset-type_0')
      self.type(file_input, file_path)
      self.input("#harta-lainnya-input-text-description","keterangan Harta lainnya")
      self.click("#harta-lainnya-input-calendar-early_acquisition_year")
      self.click(pilihtahun)
      self.click("#harta-lainnya-input-checkbox-asal-usul-hasil_sendiri")
      TanggalTransaksi6 = "#harta-lainnya-input-calendar-transaction_date"
      keterangan6       = "#harta-lainnya-input-text-asset_description"
      namapihk26        = "#harta-lainnya-input-text-name"
      alamatpihk26      = "#harta-lainnya-input-text-address"
      modalsavebtn6     = '#harta-lainnya-button-modal-save'

      list_checkbox6    = ["#harta-lainnya-input-checkbox-asal-usul-warisan"]
                        # '#harta-lainnya-input-checkbox-asal-usul-hibah_dengan_akta',
                        # '#harta-lainnya-input-checkbox-asal-usul-hibah_tanpa_akta',
                        # '#harta-lainnya-input-checkbox-asal-usul-hadiah',
                        # '#harta-lainnya-input-checkbox-asal-usul-lainnya']

      for checkbox_id6 in list_checkbox6:
        self.click(checkbox_id6)
        self.click(TanggalTransaksi6)
        self.click(kliktanggal)
        self.input(BesarNilai,nilaiuang)
        self.input(keterangan6,"Asal Usul Harta")
        self.input(namapihk26,"Pemberi Harta")
        self.input(alamatpihk26,"Alamat Pemberi Harta")
        self.click(modalsavebtn6)

      self.input("input[placeholder='Masukkan Nilai Perolehan']",nilaiuang)
      self.input("input[placeholder='Masukkan Nilai Estimasi Saat Laporan']",nilaiuang)
      self.click("#harta-lainnya-button-modal-create")
      self.sleep(3) 
  def harta_hutang(self):
     for b in range (1):
      self.click("#hutang-btn-create")
      self.click("#hutang-dropdown-asset-type")
      self.click("#hutang-dropdown-asset-type_0")
      self.click("#hutang-input-checkbox-atas-nama-pn_yang_bersangkutan")
      # self.click("#hutang-input-checkbox-atas-nama-pasangan_anak")
      # self.click("#hutang-input-checkbox-atas-nama-lainnya")
      # self.click("#hutang-dropdown-child_couple")
      # self.click("#hutang-dropdown-child_couple_0")
      # self.input('#hutang-input-text-other_information', 'nama orang')
      self.input('#hutang-input-text-creditor_name', 'nama orang')
      self.input('#hutang-input-text-collateral', 'Bangunan Tinggi')
      # self.input("hutang-input-text-beginning_of_debt",nilaiuang)
      self.type("input[placeholder='Masukkan Nilai Awal Hutang']", "500000")
      self.type("input[placeholder='Masukkan Nilai Saldo Hutang']", "500000")
      # self.input("hutang-input-text-debt_balance",nilaiuang)
      self.click("#hutang-button-modal-create")
      self.sleep(3)  
  def lampiranfasilitas(self):
    for r in range(1):
      self.click("#btn-create-lampiran-fasilitas")
      self.sleep(2)
      self.click("#fasilitas-dropdown-jenis")
      self.click("#fasilitas-dropdown-jenis_0")
      self.input("//textarea","Keterangan Fasilitas")
      self.input("//input[@id='fasilitas-input-text-nama-pihak-pemberi-fasilitas']","Nama pemberi")
      self.input("#fasilitas-text-area-keterangan-lain","Keterangan Lainnya")
      self.click('#fasilitas-button-modal-save')
      self.sleep(3)