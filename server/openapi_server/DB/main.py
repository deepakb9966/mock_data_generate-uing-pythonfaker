import firebase_admin
from firebase_admin import credentials, firestore
from firebase_admin import db
# cred = credentials.Certificate('secret key.json')
cred = credentials.Certificate("/home/deep/Desktop/mock_data_generator-main/server/openapi_server/DB/key.json")
firebase_admin.initialize_app(cred)

db = firestore.client()


