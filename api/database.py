#Database test

from time import time
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

# Use the application default credentials
cred = credentials.ApplicationDefault()
firebase_admin.initialize_app(cred, {
  'projectId': 'lahacks-2019',
})

db = firestore.client()

#Problem: Users with same name will cause overwrite of data.
def addUser(name):
    """
    Add User/Change data in User Class
    """
    doc_ref = db.collection(u'users').document()
    key = doc_ref.id
    data = {
        u'name': name,
        u'creation_date': time(),
        u'user_likes': {}
    }
    print("Created Reference for user: {0} [Key: {1}]".format(name, key))
    request = doc_ref.set(data)
    return key

addUser('Apple')
def main(requests):
    if requests:
        print("DEBUG: Found Request")
        json = requests.get_json()
        if 'name' in json:
            print("DEBUG: Processing Request")
            return addUser(json['name'])
