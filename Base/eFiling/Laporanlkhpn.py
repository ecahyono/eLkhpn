from seleniumbase import *
import time
import pyautogui
import sys

sys.path.append('C:/Users/user/Documents/TRCH/KPK/eLkhpn')
from config.userlogin import user
from config.faker import *

userlogin = "1809015306934505"

class test_efiling(user):
  def test_Laporan (self):
    self.open ("https://frontend.elhkpn.devel.torche-indonesia.com")
    self.loginapp(userlogin, "Martanegara@68")
    try:
      buttonedit = "#filling-button-row-edit-0"
      self.wait_for_element_present(buttonedit)
      self.click(buttonedit)
    except:
      butonnew = "#create-new-lhkpn"
      self.click(butonnew)
      self.wait(1)
      self.click('[aria-label="Pilih Status"]')
      self.wait(1)
      self.click((f'[aria-label="{pilihstatuslaporan}"]'))
      self.input("#filling-calendar-tanggal-pelaporan", tglinput)
      self.click('#filling-button-modal-next')

    time.sleep(4)
    self.type(file_input, file_path)
    self.input('#datapribadis-inputtext-page-npwp', userlogin)
    self.click('#btn-next-stp1')
    self.click('#datapribadis-input-text-page-alamat')
    self.input('#datapribadis-inputtext-page-kode-pos','40151')
    self.click('#btn-prev-stp1')

    # Step 4
    self.click("#efil-stp-4")
    time.sleep(4)
    pilihtahun = 'span[data-pc-section="year"]:contains("2020")'

    ######Tanah/Bangunan######
    butonselanjutnya = "#tanah-bangunan-button-selanjutnya"
    ######Tanah/Bangunan######
    # self.click("#tanah-bangunan-btn-ambil-data-dari-bpn")
    # input("EDIT SENDIRI Data Dari BPN nya oke klo udah klik ENTER")
    for i in range(3):
      self.click("#tanah-bangunan-btn-create")
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
      TanggalTransaksi = "#tanah-bangunan-input-calendar-transaction_date"
      kliktanggal = 'td[aria-label="1"]'
      BesarNilai = "#tanah-bangunan-input-text-release_value"
      keterangan = "#tanah-bangunan-input-text-asset_description"
      namapihk2 = "#tanah-bangunan-input-text-name"
      alamatpihk2 ="#tanah-bangunan-input-text-address"
      modalsavebtn = '#tanah-bangunan-button-modal-save'
      #Warisan
      self.click("#tanah-bangunan-input-checkbox-asal-usul-warisan")
      self.click(TanggalTransaksi)
      self.click(kliktanggal)
      self.input(BesarNilai,"5000000")
      self.input(keterangan,"Asal Usul Harta")
      self.input(namapihk2,"Pemberi Harta")
      self.input(alamatpihk2,"Alamat Pemberi Harta")
      self.click(modalsavebtn)
      # #hibahdengan harta
      # self.click('#tanah-bangunan-input-checkbox-asal-usul-hibah_dengan_akta')
      # self.click(TanggalTransaksi)
      # self.click(kliktanggal)
      # self.input(BesarNilai,"5000000")
      # self.input(keterangan,"Asal Usul Harta")
      # self.input(namapihk2,"Pemberi Harta")
      # self.input(alamatpihk2,"Alamat Pemberi Harta")
      # self.click(modalsavebtn)
      # #Hibah tanpa Akta
      # self.click('#tanah-bangunan-input-checkbox-asal-usul-hibah_tanpa_akta')
      # self.click(TanggalTransaksi)
      # self.click(kliktanggal)
      # self.input(BesarNilai,"5000000")
      # self.input(keterangan,"Asal Usul Harta")
      # self.input(namapihk2,"Pemberi Harta")
      # self.input(alamatpihk2,"Alamat Pemberi Harta")
      # self.click(modalsavebtn)
      # #Hadiah
      # self.click('#tanah-bangunan-input-checkbox-asal-usul-hadiah')
      # self.click(TanggalTransaksi)
      # self.click(kliktanggal)
      # self.input(BesarNilai,"5000000")
      # self.input(keterangan,"Asal Usul Harta")
      # self.input(namapihk2,"Pemberi Harta")
      # self.input(alamatpihk2,"Alamat Pemberi Harta")
      # self.click(modalsavebtn)
      # #Lainnya
      # self.click('#tanah-bangunan-input-checkbox-asal-usul-lainnya')
      # self.click(TanggalTransaksi)
      # self.click(kliktanggal)
      # self.input(BesarNilai,"5000000")
      # self.input(keterangan,"Asal Usul Harta")
      # self.input(namapihk2,"Pemberi Harta")
      # self.input(alamatpihk2,"Alamat Pemberi Harta")
      # self.click(modalsavebtn)
      self.click(butonselanjutnya)
      self.click("#tanah-bangunan-input-checkbox-pemanfaatan-tempat_tinggal")
      self.click("#tanah-bangunan-input-checkbox-pemanfaatan-disewakan")
      self.click("#tanah-bangunan-input-checkbox-pemanfaatan-pertanian")
      self.click("#tanah-bangunan-input-checkbox-pemanfaatan-lainnya")
      self.input("#tanah-bangunan-input-text-acquisition_value", "2500000")
      self.input("#tanah-bangunan-input-text-report_value", "2500000")
      self.click("#tanah-bangunan-input-calendar-acquisition_year")
      self.click(pilihtahun)
      self.click(modalsavebtn)
      time.sleep(5)
    
    ######Alat Transportasi/Mesin######
    self.click('#tab-alat-transportasi-mesin')
    ######Alat Transportasi/Mesin######

    tab2selanjutnya = "#harta-bergerak-button-selanjutnya"
    # self.click("#harta-bergerak-btn-ambil-data-dari-bapenda")
    # input("EDIT SENDIRI Data Dari BPN nya oke klo udah klik ENTER")

    for j in range (2):
      self.click("#harta-bergerak-btn-create")
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
      kliktanggal2 = 'td[aria-label="1"]'
      BesarNilai2 = "#harta-bergerak-input-text-release_value"
      keterangan2 = "#harta-bergerak-input-text-asset_description"
      namapihk22 = "#harta-bergerak-input-text-name"
      alamatpihk22 ="#harta-bergerak-input-text-address"
      modalsavebtn2 = '#harta-bergerak-button-modal-save'

      #Warisan
      self.click("#harta-bergerak-input-checkbox-asal-usul-warisan")
      self.click(TanggalTransaksi2)
      self.click(kliktanggal2)
      self.input(BesarNilai2,"5000000")
      self.input(keterangan2,"Asal Usul Harta")
      self.input(namapihk22,"Pemberi Harta")
      self.input(alamatpihk22,"Alamat Pemberi Harta")
      self.click(modalsavebtn2)
      # ##hibahdengan harta
      # self.click('#harta-bergerak-input-checkbox-asal-usul-hibah_dengan_akta')
      # self.click(TanggalTransaksi2)
      # self.click(kliktanggal2)
      # self.input(BesarNilai2,"5000000")
      # self.input(keterangan2,"Asal Usul Harta")
      # self.input(namapihk22,"Pemberi Harta")
      # self.input(alamatpihk22,"Alamat Pemberi Harta")
      # self.click(modalsavebtn2)
      # #Hibah tanpa Akta
      # self.click('#harta-bergerak-input-checkbox-asal-usul-hibah_tanpa_akta')
      # self.click(TanggalTransaksi2)
      # self.click(kliktanggal2)
      # self.input(BesarNilai2,"5000000")
      # self.input(keterangan2,"Asal Usul Harta")
      # self.input(namapihk22,"Pemberi Harta")
      # self.input(alamatpihk22,"Alamat Pemberi Harta")
      # self.click(modalsavebtn2)
      # #Hadiah
      # self.click('#harta-bergerak-input-checkbox-asal-usul-hadiah')
      # self.click(TanggalTransaksi2)
      # self.click(kliktanggal2)
      # self.input(BesarNilai2,"5000000")
      # self.input(keterangan2,"Asal Usul Harta")
      # self.input(namapihk22,"Pemberi Harta")
      # self.input(alamatpihk22,"Alamat Pemberi Harta")
      # self.click(modalsavebtn2)
      # #Lainnya
      # self.click('#harta-bergerak-input-checkbox-asal-usul-lainnya')
      # self.click(TanggalTransaksi2)
      # self.click(kliktanggal2)
      # self.input(BesarNilai2,"5000000")
      # self.input(keterangan2,"Asal Usul Harta")
      # self.input(namapihk22,"Pemberi Harta")
      # self.input(alamatpihk22,"Alamat Pemberi Harta")
      # self.click(modalsavebtn2)
      self.click(tab2selanjutnya)
      self.click("#harta-bergerak-dropdown-utilization")
      self.click("#harta-bergerak-dropdown-utilization_0")
      self.input("#harta-bergerak-input-text-acquisition_value", "2500000")
      self.input("#harta-bergerak-input-text-report_value", "2500000")
      self.click("#harta-bergerak-input-calendar-early_acquisition_year")
      self.click(pilihtahun)
      self.click(modalsavebtn2)
      time.sleep(5)

    ######Alat Transportasi/Mesin######
    self.click('#tab-tanah-bergerak-lainnya')
    ######Alat Transportasi/Mesin######

    tab3selanjutnya2 = "#harta-bergerak-lainnya-button-selanjutnya"
    # self.click("#harta-bergerak-btn-ambil-data-dari-bapenda")
    # input("EDIT SENDIRI Data Dari BPN nya oke klo udah klik ENTER")

    for k in range (2):
      self.click("#harta-bergerak-lainnya-btn-create")
      self.click("#harta-bergerak-lainnya-dropdown-asset-type")
      self.click("#harta-bergerak-lainnya-dropdown-asset-type_0")
      self.input("#harta-bergerak-lainnya-input-text-amount","10")
      self.input("#harta-bergerak-lainnya-input-text-unit","unit")
      self.input("#harta-bergerak-lainnya-input-text-description","Keterangan Data Harta Bergerak Lainnya")
      self.click("#harta-bergerak-lainnya-input-calendar-early_acquisition_year")
      self.click(pilihtahun)
      self.click("#harta-bergerak-lainnya-input-checkbox-asal-usul-hasil_sendiri")
      TanggalTransaksi3 = "#harta-bergerak-lainnya-input-calendar-transaction_date"
      kliktanggal3 = 'td[aria-label="1"]'
      BesarNilai3 = "#harta-bergerak-lainnya-input-text-release_value"
      keterangan3 = "#harta-bergerak-lainnya-input-text-asset_description"
      namapihk23 = "#harta-bergerak-lainnya-input-text-name"
      alamatpihk23 ="#harta-bergerak-lainnya-input-text-address"
      modalsavebtn3 = '#harta-bergerak-lainnya-button-modal-save'
      #Warisan
      self.click("#harta-bergerak-lainnya-input-checkbox-asal-usul-warisan")
      self.click(TanggalTransaksi3)
      self.click(kliktanggal3)
      self.input(BesarNilai3,"5000000")
      self.input(keterangan3,"Asal Usul Harta")
      self.input(namapihk23,"Pemberi Harta")
      self.input(alamatpihk23,"Alamat Pemberi Harta")
      self.click(modalsavebtn3)
      # ##hibahdengan harta
      # self.click('#harta-bergerak-lainnya-input-checkbox-asal-usul-hibah_dengan_akta')
      # self.click(TanggalTransaksi3)
      # self.click(kliktanggal3)
      # self.input(BesarNilai3,"5000000")
      # self.input(keterangan3,"Asal Usul Harta")
      # self.input(namapihk23,"Pemberi Harta")
      # self.input(alamatpihk23,"Alamat Pemberi Harta")
      # self.click(modalsavebtn3)
      # #Hibah tanpa Akta
      # self.click('#harta-bergerak-lainnya-input-checkbox-asal-usul-hibah_tanpa_akta')
      # self.click(TanggalTransaksi3)
      # self.click(kliktanggal3)
      # self.input(BesarNilai3,"5000000")
      # self.input(keterangan3,"Asal Usul Harta")
      # self.input(namapihk23,"Pemberi Harta")
      # self.input(alamatpihk23,"Alamat Pemberi Harta")
      # self.click(modalsavebtn3)
      # #Hadiah
      # self.click('#harta-bergerak-lainnya-input-checkbox-asal-usul-hadiah')
      # self.click(TanggalTransaksi3)
      # self.click(kliktanggal3)
      # self.input(BesarNilai3,"5000000")
      # self.input(keterangan3,"Asal Usul Harta")
      # self.input(namapihk23,"Pemberi Harta")
      # self.input(alamatpihk23,"Alamat Pemberi Harta")
      # self.click(modalsavebtn3)
      # #Lainnya
      # self.click('#harta-bergerak-lainnya-input-checkbox-asal-usul-lainnya')
      # self.click(TanggalTransaksi3)
      # self.click(kliktanggal3)
      # self.input(BesarNilai3,"5000000")
      # self.input(keterangan3,"Asal Usul Harta")
      # self.input(namapihk23,"Pemberi Harta")
      # self.input(alamatpihk23,"Alamat Pemberi Harta")
      # self.click(modalsavebtn3)
      self.input("#harta-bergerak-lainnya-input-text-acquisition_value", "2500000")
      self.input("//input[@id='harta-bergerak-lainnya-input-text-report_value']","2500000")
      # self.input("#harta-bergerak-lainnya-input-text-report_value","2500000")
      self.click("#harta-bergerak-lainnya-button-modal-create")
      time.sleep(4)

    ######Alat surat Berhargan######
    self.click('#tab-surat-berharga')
    ######Alat surat Berhargan######
    tab3selanjutnya = "#surat-berharga-button-selanjutnya"
    
    for l in range(3):
      self.click('#surat-berharga-btn-create')
      self.input("#surat-berharga-input-text-account_number","497066923")
      self.type(file_input, file_path)
      self.click('#surat-berharga-dropdown-asset-type')
      self.click('#surat-berharga-dropdown-asset-type_0')
      self.click(tab3selanjutnya)
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
      kliktanggal4 = 'td[aria-label="1"]'
      BesarNilai4 = "#surat-berharga-input-text-release_value"
      keterangan4 = "#surat-berharga-input-text-asset_description"
      namapihk24 = "#surat-berharga-input-text-name"
      alamatpihk24 ="#surat-berharga-input-text-address"
      modalsavebtn4 = '#surat-berharga-button-modal-save'
      #Warisan
      self.click("#surat-berharga-input-checkbox-asal-usul-warisan")
      self.click(TanggalTransaksi4)
      self.click(kliktanggal4)
      self.input(BesarNilai4,"5000000")
      self.input(keterangan4,"Asal Usul Harta")
      self.input(namapihk24,"Pemberi Harta")
      self.input(alamatpihk24,"Alamat Pemberi Harta")
      self.click(modalsavebtn4)
      # ##hibahdengan harta
      # self.click('#surat-berharga-input-checkbox-asal-usul-hibah_dengan_akta')
      # self.click(TanggalTransaksi4)
      # self.click(kliktanggal4)
      # self.input(BesarNilai4,"5000000")
      # self.input(keterangan4,"Asal Usul Harta")
      # self.input(namapihk24,"Pemberi Harta")
      # self.input(alamatpihk24,"Alamat Pemberi Harta")
      # self.click(modalsavebtn4)
      # #Hibah tanpa Akta
      # self.click('#surat-berharga-input-checkbox-asal-usul-hibah_tanpa_akta')
      # self.click(TanggalTransaksi4)
      # self.click(kliktanggal4)
      # self.input(BesarNilai4,"5000000")
      # self.input(keterangan4,"Asal Usul Harta")
      # self.input(namapihk24,"Pemberi Harta")
      # self.input(alamatpihk24,"Alamat Pemberi Harta")
      # self.click(modalsavebtn4)
      # #Hadiah
      # self.click('#surat-berharga-input-checkbox-asal-usul-hadiah')
      # self.click(TanggalTransaksi4)
      # self.click(kliktanggal4)
      # self.input(BesarNilai4,"5000000")
      # self.input(keterangan4,"Asal Usul Harta")
      # self.input(namapihk24,"Pemberi Harta")
      # self.input(alamatpihk24,"Alamat Pemberi Harta")
      # self.click(modalsavebtn4)
      # #Lainnya
      # self.click('#surat-berharga-input-checkbox-asal-usul-lainnya')
      # self.click(TanggalTransaksi4)
      # self.click(kliktanggal4)
      # self.input(BesarNilai4,"5000000")
      # self.input(keterangan4,"Asal Usul Harta")
      # self.input(namapihk24,"Pemberi Harta")
      # self.input(alamatpihk24,"Alamat Pemberi Harta")
      # self.click(modalsavebtn4)
      self.click(tab3selanjutnya)
      self.input("#surat-berharga-input-text-acquisition_value","2500000")
      self.input("#surat-berharga-input-text-report_value","2500000")
      self.click("#surat-berharga-input-calendar-early_acquisition_year")
      self.click(pilihtahun)
      self.click(modalsavebtn4)
      time.sleep(4)

    ######Alat surat Berhargan######
    self.click('#tab-kas-setara-kas')
    ######Alat surat Berhargan######
    tab3selanjutnya2 = "#harta-kas-button-selanjutnya"

    for m in range(3):
      self.click("#harta-kas-btn-create")
      self.click("#harta-kas-dropdown-asset-type")
      self.click("#harta-kas-dropdown-asset-type_0")
      self.type(file_input, file_path)
      self.input("#harta-kas-input-text-bank_name","KPK BANK")
      self.input("#harta-kas-input-text-number_account","45597909")
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
      kliktanggal5 = 'td[aria-label="1"]'
      BesarNilai5 = "#harta-kas-input-text-release_value"
      keterangan5 = "#harta-kas-input-text-asset_description"
      namapihk25 = "#harta-kas-input-text-name"
      alamatpihk25 ="#harta-kas-input-text-address"
      modalsavebtn5 = '#harta-kas-button-modal-save'
      #Warisan
      self.click("#harta-kas-input-checkbox-asal-usul-warisan")
      self.click(TanggalTransaksi5)
      self.click(kliktanggal5)
      self.input(BesarNilai5,"5000000")
      self.input(keterangan5,"Asal Usul Harta")
      self.input(namapihk25,"Pemberi Harta")
      self.input(alamatpihk25,"Alamat Pemberi Harta")
      self.click(modalsavebtn5)
      # ##hibahdengan harta
      # self.click('#harta-kas-input-checkbox-asal-usul-hibah_dengan_akta')
      # self.click(TanggalTransaksi5)
      # self.click(kliktanggal5)
      # self.input(BesarNilai5,"5000000")
      # self.input(keterangan5,"Asal Usul Harta")
      # self.input(namapihk25,"Pemberi Harta")
      # self.input(alamatpihk25,"Alamat Pemberi Harta")
      # self.click(modalsavebtn5)
      # #Hibah tanpa Akta
      # self.click('#harta-kas-input-checkbox-asal-usul-hibah_tanpa_akta')
      # self.click(TanggalTransaksi5)
      # self.click(kliktanggal5)
      # self.input(BesarNilai5,"5000000")
      # self.input(keterangan5,"Asal Usul Harta")
      # self.input(namapihk25,"Pemberi Harta")
      # self.input(alamatpihk25,"Alamat Pemberi Harta")
      # self.click(modalsavebtn5)
      # #Hadiah
      # self.click('#harta-kas-input-checkbox-asal-usul-hadiah')
      # self.click(TanggalTransaksi5)
      # self.click(kliktanggal5)
      # self.input(BesarNilai5,"5000000")
      # self.input(keterangan5,"Asal Usul Harta")
      # self.input(namapihk25,"Pemberi Harta")
      # self.input(alamatpihk25,"Alamat Pemberi Harta")
      # self.click(modalsavebtn5)
      # #Lainnya
      # self.click('#harta-kas-input-checkbox-asal-usul-lainnya')
      # self.click(TanggalTransaksi5)
      # self.click(kliktanggal5)
      # self.input(BesarNilai5,"5000000")
      # self.input(keterangan5,"Asal Usul Harta")
      # self.input(namapihk25,"Pemberi Harta")
      # self.input(alamatpihk25,"Alamat Pemberi Harta")
      # self.click(modalsavebtn5)
      self.click(tab3selanjutnya2)
      self.input("#harta-kas-input-text-balance_value","2500000")
      self.click(modalsavebtn5)
      time.sleep(4)
      
    ######Alat surat Berhargan######
    self.click('#tab-harta-lainnya')
    ######Alat surat Berhargan######

    for g in range(3):
      self.click("#harta-lainnya-btn-create")
      self.click('#harta-lainnya-dropdown-asset-type')
      self.click('#harta-lainnya-dropdown-asset-type_0')
      self.type(file_input, file_path)
      self.input("#harta-lainnya-input-text-description","keterangan Harta lainnya")
      self.click("#harta-lainnya-input-calendar-early_acquisition_year")
      self.click(pilihtahun)
      self.click("#harta-lainnya-input-checkbox-asal-usul-hasil_sendiri")
      TanggalTransaksi6 = "#harta-lainnya-input-calendar-transaction_date"
      kliktanggal6 = 'td[aria-label="1"]'
      BesarNilai6 = "#harta-lainnya-input-text-release_value"
      keterangan6 = "#harta-lainnya-input-text-asset_description"
      namapihk26 = "#harta-lainnya-input-text-name"
      alamatpihk26 ="#harta-lainnya-input-text-address"
      modalsavebtn6 = '#harta-lainnya-button-modal-save'
      #Warisan
      self.click("#harta-lainnya-input-checkbox-asal-usul-warisan")
      self.click(TanggalTransaksi6)
      self.click(kliktanggal6)
      self.input(BesarNilai6,"5000000")
      self.input(keterangan6,"Asal Usul Harta")
      self.input(namapihk26,"Pemberi Harta")
      self.input(alamatpihk26,"Alamat Pemberi Harta")
      self.click(modalsavebtn6)
      # ##hibahdengan harta
      # self.click('#harta-lainnya-input-checkbox-asal-usul-hibah_dengan_akta')
      # self.click(TanggalTransaksi6)
      # self.click(kliktanggal6)
      # self.input(BesarNilai6,"5000000")
      # self.input(keterangan6,"Asal Usul Harta")
      # self.input(namapihk26,"Pemberi Harta")
      # self.input(alamatpihk26,"Alamat Pemberi Harta")
      # self.click(modalsavebtn6)
      # #Hibah tanpa Akta
      # self.click('#harta-lainnya-input-checkbox-asal-usul-hibah_tanpa_akta')
      # self.click(TanggalTransaksi6)
      # self.click(kliktanggal6)
      # self.input(BesarNilai6,"5000000")
      # self.input(keterangan6,"Asal Usul Harta")
      # self.input(namapihk26,"Pemberi Harta")
      # self.input(alamatpihk26,"Alamat Pemberi Harta")
      # self.click(modalsavebtn6)
      # #Hadiah
      # self.click('#harta-lainnya-input-checkbox-asal-usul-hadiah')
      # self.click(TanggalTransaksi6)
      # self.click(kliktanggal6)
      # self.input(BesarNilai6,"5000000")
      # self.input(keterangan6,"Asal Usul Harta")
      # self.input(namapihk26,"Pemberi Harta")
      # self.input(alamatpihk26,"Alamat Pemberi Harta")
      # self.click(modalsavebtn6)
      # #Lainnya
      # self.click('#harta-lainnya-input-checkbox-asal-usul-lainnya')
      # self.click(TanggalTransaksi6)
      # self.click(kliktanggal6)
      # self.input(BesarNilai6,"5000000")
      # self.input(keterangan6,"Asal Usul Harta")
      # self.input(namapihk26,"Pemberi Harta")
      # self.input(alamatpihk26,"Alamat Pemberi Harta")
      # self.click(modalsavebtn6)
      self.input("#harta-lainnya-input-text-acquisition_value","2500000")
      self.input("#harta-lainnya-input-text-report_value","2500000")
      self.click("#harta-lainnya-button-modal-create")
      time.sleep(4)  

    ######HUTANG######
    self.click('#tab-hutang')
    ######HUTANG######
    for b in range (2):
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
      # self.input("hutang-input-text-beginning_of_debt","2500000")
      self.type("input[placeholder='Masukkan Nilai Awal Hutang']", "500000")
      self.type("input[placeholder='Masukkan Nilai Saldo Hutang']", "500000")
      # self.input("hutang-input-text-debt_balance","2500000")
      self.click("#hutang-button-modal-create")
      time.sleep(4)  

    # Step 5
    self.click("#efil-stp-5")
    time.sleep(4)
    klilpopup = "#penerimaan-button-modal-success-edit"
    pengeluaranpupop = "#pengeluaran-button-modal-success-edit"
    nilai = "5000000"
    h1_selector = '.text-2xl.font-semibold'

    #kolompn
    num_elements = 5
    for index in range(num_elements):
      idnyatd = f"#column-penerimaan-dari-pekerjaan-pn-{index}"
      idinput = f"#input-pn-penerimaan-dari-pekerjaan-{index}"

      self.click(idnyatd)
      self.type(idinput, nilai)
      self.click(h1_selector)
      self.click(klilpopup)
    num_elements1 = 5
    for index1 in range(num_elements1):
      idnyatd1 = f"#column-penerimaan-dari-pekerjaan-pasangan-{index1}"
      idinput1 = f"#input-pasangan-penerimaan-dari-pekerjaan-{index1}"

      self.click(idnyatd1)
      self.type(idinput1, nilai)
      self.click(h1_selector)
      self.click(klilpopup)
    #
    self.click('#tab-penerimaan-dari-usaha-dan-kekayaan')
    #
    num_elements2 = 5
    for index2 in range(num_elements2):
      idnyatd2 = f"#column-penerimaan-dari-usaha-dan-kekayaan-{index2}"
      idinput2 = f"#input-penerimaan-dari-usaha-dan-kekayaan-{index2}"

      self.click(idnyatd2)
      self.type(idinput2, nilai)
      self.click(h1_selector)
      self.click(klilpopup)
    #
    self.click("#tab-penerimaan-lainnya")
    #
    num_elements3 = 4
    for index3 in range(num_elements3):
      idnyatd3 = f"#column-penerimaan-lainnya-{index3}"
      idinput3 = f"#input-penerimaan-lainnya-{index3}"

      self.click(idnyatd3)
      self.type(idinput3, nilai)
      self.click(h1_selector)
      self.click(klilpopup)

    # Step 6
    self.click("#efil-stp-6")
    time.sleep(4)

    num_elements4 = 4
    for index4 in range(num_elements4):
      idnyatd4 = f"#column-pengeluaran-rutin-{index4}"
      idinput4 = f"#input-pengeluaran-rutin-{index4}"

      self.click(idnyatd4)
      self.type(idinput4, nilai)
      self.click(h1_selector)
      self.click(pengeluaranpupop)
    #
    self.click("#tab-pengeluaran-harta")
    #
    num_elements5 = 3
    for index5 in range(num_elements5):
      idnyatd5 = f"#column-pengeluaran-harta-{index5}"
      idinput5 = f"#input-pengeluaran-harta-{index5}"

      self.click(idnyatd5)
      self.type(idinput5, nilai)
      self.click(h1_selector)
      self.click(pengeluaranpupop)
    #
    self.click("#tab-pengeluaran-lainnya")
    #
    num_elements6 = 3
    for index6 in range(num_elements6):
      idnyatd5 = f"#column-pengeluaran-lainnya-{index6}"
      idinput6 = f"#input-pengeluaran-lainnya-{index6}"

      self.click(idnyatd5)
      self.type(idinput6, nilai)
      self.click(h1_selector)
      self.click(pengeluaranpupop)

    # Step 7
    # self.click("#efil-stp-7")
    # time.sleep(4)
    # Step 8
    self.click("#efil-stp-8")
    time.sleep(4)
    for r in range(3):
      self.click("#btn-create-lampiran-fasilitas")
      self.click("#fasilitas-dropdown-jenis")
      self.click("#fasilitas-dropdown-jenis_0")
      self.input("//textarea","Keterangan Fasilitas")
      self.input("//input[@id='fasilitas-input-text-nama-pihak-pemberi-fasilitas']","Nama pemberi")
      self.input("#fasilitas-text-area-keterangan-lain","Keterangan Lainnya")
      self.click('#fasilitas-button-modal-save')
      time.sleep(4)









    

    

    

      

    

