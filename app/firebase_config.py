import firebase_admin
from firebase_admin import credentials, firestore
import os

FIREBASE_KEY_PATH = os.getenv("FIREBASE_KEY_PATH", "firebase_key.json")

# Load credentials
cred = credentials.Certificate("config/firebase_key.json")
firebase_admin.initialize_app(cred)

# Firestore client
db = firestore.client()
