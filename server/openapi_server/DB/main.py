import os

import firebase_admin
from firebase_admin import credentials, firestore
# from firebase_admin import db
# cred = credentials.Certificate('secret key.json')
script_dir = os.path.dirname(__file__)
file_path = os.path.join(script_dir, 'key.json')
print(script_dir,"dfhfgfdh")
cred = credentials.Certificate(file_path)
firebase_admin.initialize_app(cred)

db = firestore.client()


