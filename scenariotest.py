from Administrator.Zombie import *
from Administrator.Master_Data import *

@mark.lkhpn
def testconfigandlogin():
	Log.info('Konfigurasi agar berjalan di setiap sistem operasi (mac dan Windos)')
	global driver
	driver = initDriver()
	Log.info('Memasukan User name dan Password di halaman Login')

@mark.lkhpn
def testtest():
  opsi = input('')~