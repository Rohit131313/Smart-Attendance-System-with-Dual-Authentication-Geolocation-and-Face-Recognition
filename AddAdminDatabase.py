import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
from dotenv import load_dotenv
import os
import json

load_dotenv() 

# Initialize Firebase
cred_dict = json.loads(os.getenv('FIREBASE_SERVICE_ACCOUNT_KEY_JSON'))
cred = credentials.Certificate(cred_dict)
firebase_admin.initialize_app(cred, {'databaseURL': os.getenv('DATABASE_URL')})


ref = db.reference('AdminLocation/')

data = {
    
}

for key, value in data.items():
    ref.child(key).set(value)
