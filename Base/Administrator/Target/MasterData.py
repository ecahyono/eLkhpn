from Target.Administratormain import *
from Target.Listdataadministrator import *

txtmasterAgama                = 'Mengakses masterAgama'
txtmasterPendidikan           = 'Mengakses masterAgama'
txtmasterProvinsi             = 'Mengakses masterAgama'
txtmasterKabupatenKota        = 'Mengakses masterAgama'
txtmasterMataUang             = 'Mengakses masterAgama'
txtmasterInstansi             = 'Mengakses masterAgama'
txtmasterUnitkerja            = 'Mengakses masterAgama'
txtmasterSubUnitKerja         = 'Mengakses masterAgama'
txtmasterJabatan              = 'Mengakses masterAgama'
txtmasterEselon               = 'Mengakses masterAgama'
txtmasterAsalUsulHarta        = 'Mengakses masterAgama'
txtmasterPemanfaatan          = 'Mengakses masterAgama'
txtmasterGolonganHarta        = 'Mengakses masterAgama'
txtmasterJenisBukti           = 'Mengakses masterAgama'
txtmasterJenisPelepasanHarta  = 'Mengakses masterAgama'
txtmasterRiwayat              = 'Mengakses masterAgama'

global forkatkun
def opsitestingmasterdata(driver):
  Log.info('Konfigurasi agar berjalan di setiap sistem operasi (mac dan Windos)')
  forkatkun = input('Pilih Master yang akan DItambah dieksekusi \n'
        '1. masterAgama\n'
        '2. masterPendidikan\n'
        '3. masterProvinsi\n'
        '4. masterKabupatenKota\n'
        '5. masterMataUang\n'
        '6. masterInstansi\n'
        '7. masterUnitkerja\n'
        '8. masterSubUnitKerja\n'
        '9. masterJabatan\n'
        '10. masterEselon\n'
        '11. masterAsalUsulHarta\n'
        '12. masterPemanfaatan\n'
        '13. masterGolonganHarta\n'
        '14. masterJenisBukti\n'
        '15. masterJenisPelepasanHarta\n'
        '16. masterRiwayat\n'
        'Masukan Nomer yang tersedia =>: '  
  )
  if forkatkun == '1':
    Log.info(txtmasterAgama)
    masterAgama               = "https://frontend-e-lhkpn.dev.torche.id/administrator/master/agama"
    driver.get(masterAgama)
    turu(driver)
    addbuttonagama = WebDriverWait(driver, 45).until(EC.element_to_be_clickable((By.ID, 'agama-button-page-create')))
    addbuttonagama.click()
    turu(driver)
    fieldnamaagama = WebDriverWait(driver, 45).until(EC.element_to_be_clickable((By.ID, 'agama-input-text-nama')))
    fieldnamaagama.send_keys(namaagama)
    turu(driver)
    #submitagama
    driver.find_element(By.ID, 'agama-button-create').click()   
  elif forkatkun == '2':
    Log.info(txtmasterPendidikan)
    masterPendidikan(driver)
  elif forkatkun == '3':
    Log.info(txtmasterProvinsi)
    masterProvinsi(driver)    
  elif forkatkun == '4':
    Log.info(txtmasterKabupatenKota)
    masterKabupatenKota(driver)    
  elif forkatkun == '5':
    Log.info(txtmasterMataUang)
    masterMataUang(driver)    
  elif forkatkun == '6':
    Log.info(txtmasterInstansi)
    masterInstansi(driver)    
  elif forkatkun == '7':
    Log.info(txtmasterUnitkerja)
    masterUnitkerja(driver)    
  elif forkatkun == '8':
    Log.info(txtmasterSubUnitKerja)
    masterSubUnitKerja(driver)    
  elif forkatkun == '9':
    Log.info(txtmasterJabatan)
    masterJabatan(driver)    
  elif forkatkun == '10':
    Log.info(txtmasterEselon)
    masterEselon(driver)    
  elif forkatkun == '11':
    Log.info(txtmasterAsalUsulHarta)
    masterAsalUsulHarta(driver)    
  elif forkatkun == '12':
    Log.info(txtmasterPemanfaatan)
    masterPemanfaatan(driver)    
  elif forkatkun == '13':
    Log.info(txtmasterGolonganHarta)
    masterGolonganHarta(driver)    
  elif forkatkun == '14':
    Log.info(txtmasterJenisBukti)
    masterJenisBukti(driver)    
  elif forkatkun == '15':
    Log.info(txtmasterJenisPelepasanHarta)
    masterJenisPelepasanHarta(driver)    
  elif forkatkun == '16':
    Log.info(txtmasterRiwayat)
    masterRiwayat(driver)    
 
def masterPendidikan(driver):
  masterPendidikan          = "https://frontend-e-lhkpn.dev.torche.id/administrator/master"
  driver.get(masterPendidikan)
def masterProvinsi(driver):
  masterProvinsi            = "https://frontend-e-lhkpn.dev.torche.id/administrator/master"
  driver.get(masterProvinsi)
def masterKabupatenKota(driver):
  masterKabupatenKota       = "https://frontend-e-lhkpn.dev.torche.id/administrator/master"
  driver.get(masterKabupatenKota)
def masterMataUang(driver):
  masterMataUang            = "https://frontend-e-lhkpn.dev.torche.id/administrator/master"
  driver.get(masterMataUang)
def masterInstansi(driver):
  masterInstansi            = "https://frontend-e-lhkpn.dev.torche.id/administrator/master"
  driver.get(masterInstansi)
def masterUnitkerja(driver):
  masterUnitkerja           = "https://frontend-e-lhkpn.dev.torche.id/administrator/master"
  driver.get(masterUnitkerja)
def masterSubUnitKerja(driver):
  masterSubUnitKerja        = "https://frontend-e-lhkpn.dev.torche.id/administrator/master"
  driver.get(masterSubUnitKerja)
def masterJabatan(driver):
  masterJabatan             = "https://frontend-e-lhkpn.dev.torche.id/administrator/master"
  driver.get(masterJabatan)
def masterEselon(driver):
  masterEselon              = "https://frontend-e-lhkpn.dev.torche.id/administrator/master" 
  driver.get(masterEselon)
def masterAsalUsulHarta(driver):
  masterAsalUsulHarta       = "https://frontend-e-lhkpn.dev.torche.id/administrator/master"
  driver.get(masterAsalUsulHarta)
def masterPemanfaatan(driver):
  masterPemanfaatan         = "https://frontend-e-lhkpn.dev.torche.id/administrator/master"
  driver.get(masterPemanfaatan)
def masterGolonganHarta(driver):
  masterGolonganHarta       = "https://frontend-e-lhkpn.dev.torche.id/administrator/master"
  driver.get(masterGolonganHarta)
def masterJenisBukti(driver):
  masterJenisBukti          = "https://frontend-e-lhkpn.dev.torche.id/administrator/master"
  driver.get(masterJenisBukti)
def masterJenisPelepasanHarta(driver):
  masterJenisPelepasanHarta = "https://frontend-e-lhkpn.dev.torche.id/administrator/master"
  driver.get(masterRiwayat)
def masterRiwayat(driver):
  masterRiwayat             = "https://frontend-e-lhkpn.dev.torche.id/administrator/master"
  driver.get(masterRiwayat)