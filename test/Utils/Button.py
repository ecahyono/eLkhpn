import sys
import platform
import random

if platform.system() == 'Darwin':
    sys.path.append(environ.get("MACPARENTDIR")) 
elif platform.system() == 'Windows':
    sys.path.append(environ.get("WINPARENTDIR"))

#Master Agama 
Tambahagama = "agama-button-page-create"
Simpaneditagama = "agama-button-edit"
simpantambahagama = "agama-button-create"