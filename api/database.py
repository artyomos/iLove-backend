import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

# Use the application default credentials
cred = credentials.ApplicationDefault()
firebase_admin.initialize_app(cred, {
  'projectId': 'lahacks-2019',
})

db = firestore.client()

# Toggle True to see debug statements
DEBUG = False
