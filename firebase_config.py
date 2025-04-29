import firebase_admin
from firebase_admin import credentials, firestore

# Load credentials
cred = credentials.Certificate("config/firebase_key.json")
firebase_admin.initialize_app(cred)

# Firestore client
db = firestore.client()
