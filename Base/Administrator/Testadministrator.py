from Target.Administratormain import *
from Target.MasterData import *
from Target.Listdataadministrator import *

global driver 
global forkatkun
# init driver by os
@mark.feLKHPN
def testing():
  Log.info('Konfigurasi agar berjalan di setiap sistem operasi (mac dan Windos)')
  driver = initDriver()
  
  forkatkun = input('Pilih Master yang akan DItambah dieksekusi \n'
        '1. Menu\n'
        '2. Role\n'
        '3. User\n'
        '4. Aktivitas\n'
        '5. Master Data\n'
        '6. Setting\n'
        '7. MonitoringAI\n'
        '8. Pengumuman\n'
        '9. API Pengumuman\n'
        '10. API Instansi\n'
        '11. FAQ\n'
        'Masukan Nomer yang tersedia =>: '  
  )
  if forkatkun == '1':
    masterAgama(driver)    
  elif forkatkun == '2':
    masterPendidikan(driver)
  elif forkatkun == '3':
    masterProvinsi(driver)    
  elif forkatkun == '4':
    masterKabupatenKota(driver)    
  elif forkatkun == '5':
    opsitestingmasterdata(driver)    
  elif forkatkun == '6':
    masterInstansi(driver)    
  elif forkatkun == '7':
    masterUnitkerja(driver)    
  elif forkatkun == '8':
    masterSubUnitKerja(driver)    
  elif forkatkun == '9':
    masterJabatan(driver)    
  elif forkatkun == '10':
    masterEselon(driver)    
  elif forkatkun == '11':
    masterAsalUsulHarta(driver)    
  elif forkatkun == '12':
    masterPemanfaatan(driver)    
  elif forkatkun == '13':
    masterGolonganHarta(driver)    
  elif forkatkun == '14':
    masterJenisBukti(driver)    
  elif forkatkun == '15':
    masterJenisPelepasanHarta(driver)    
  elif forkatkun == '16':
    masterRiwayat(driver)    
  