from Target.Administratormain import *
from Target.MasterData import *

# init driver by os
@mark.feLKHPN
def testconfigandlogin():
	Log.info('Konfigurasi agar berjalan di setiap sistem operasi (mac dan Windos)')
	global driver, pathData
	driver = initDriver()
	pathData = loadDataPath()
	Log.info('Memasukan User name dan Password di halaman Login')

@mark.feLKHPN
def testlitmas():
  Log.info('Menambah Data Register Pendampingan')
  driver.get('https://frontend-e-lhkpn.dev.torche.id/administrator')

@mark.feLKHPN
def testfiltertable():
  global forkatkun

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
    masterAgama(driver)    
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
  