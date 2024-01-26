from seleniumbase import BaseCase
import sys
import os
from dotenv import load_dotenv
load_dotenv()

python_path = os.environ.get("PYTHONPATH")
sys.path.append(python_path)
from config.userlogin import user
from config.faker import *
from Base.eAudit.Pemeriksaan.tiaptabpemeriksaan import tiaptabpemeriksaan
class hasilanalisis(user, tiaptabpemeriksaan):
  def test_hasilanalisis(self):
    self.loginapp("checking", "Martanegara@68")
    self.open('https://frontend.elhkpn.devel.torche-indonesia.com/administrator/e-audit/pemeriksaan')
    tom = input('Ingin Hasil Analisis yang mana? index ke berapa?=>>>>>')
    idtmhanalis = f'audit-button-action-hasil-analisis-{tom}'
    self.click(f'#{idtmhanalis}')
    self.sleep(5)

    #tabharta
    self.click