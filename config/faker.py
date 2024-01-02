from faker import Faker
import random
from datetime import datetime, timedelta

fake = Faker('id_ID')

file_input = "input[type=file]" 
file_path = "C:/Users/user/Documents/TRCH/KPK/eLkhpn/assets/image/barcode.jpg"
kliktanggal = 'td[aria-label="1"]'

jumlah = fake.random_int(min=200, max=1000)
textfield = fake.text()[:30]
alamat = fake.address()[:30]
nik	= fake.msisdn()+"5"f"{1:09}"
nama = fake.name() 
telepon = fake.phone_number()


nilaiuang = fake.random_int(min=2000000, max=10000000)

jenislaporan = ['Periodik','Khusus']
pilihjenislaporan = random.choice(jenislaporan)
statuslaporan = ['Calon Penyelenggara Negara','Awal Menjabat','Akhir Menjabat']
pilihstatuslaporan = random.choice(statuslaporan)

tanggal_sekarang = datetime.now()
tanggal_sebelumnya = tanggal_sekarang - timedelta(days=60)
tglinput = tanggal_sebelumnya.strftime('%d/%m/%Y') 

pilihtahun = 'span[data-pc-section="year"]:contains("2020")'
kliktanggal = 'td[aria-label="1"]'
BesarNilai = "input[placeholder='Masukkan Besar Nilai']"