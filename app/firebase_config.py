import firebase_admin
from firebase_admin import credentials, firestore
import os

FIREBASE_KEY_PATH = os.getenv("FIREBASE_KEY_PATH", "firebase_config.py")

# Load credentials
cred = credentials.Certificate("firebase_config.py")
firebase_admin.initialize_app(cred)

# Firestore client
db = firestore.client()
