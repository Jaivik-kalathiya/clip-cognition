import json
import firebase_admin
from firebase_admin import credentials, firestore

def load_environment():
    """Load environment variables and initialize Firebase"""
    # Load API keys
    env = json.load(open('./api.json'))
    
    # Initialize Firebase
    cred = credentials.Certificate("./secret.json")
    firebase_admin.initialize_app(cred)
    store = firestore.client()
    
    return env, store