import os
import pyrebase


def initialize_firebase():
    try:
        config = {
            "apiKey": os.getenv("API_KEY"),
            "authDomain": os.getenv("AUTH_DOMAIN"),
            "databaseURL": os.getenv("DATABASE_URL"),
            "storageBucket": os.getenv("STORAGE_BUCKET"),
        }
        firebase = pyrebase.initialize_app(config)
        return firebase.auth()
    except Exception:
        raise Exception(
            "Firebase configuration credentials not found or invalid. Please check your environment variables."
        )
