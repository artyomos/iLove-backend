#Database test

from time import time
import random, string
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
from flask import jsonify

class NoInput(Exception):
    pass

# Use the application default credentials
cred = credentials.ApplicationDefault()
firebase_admin.initialize_app(cred, {
  'projectId': 'lahacks-2019',
})

db = firestore.client()

#Problem: Users with same name will cause overwrite of data.
def addUser(name):
    """
    Add User
    """
    doc_ref = db.collection(u'users').document()
    key = doc_ref.id

    print("Created Reference for user: {0} [Key: {1}]".format(name, key))
    
    data = {
        u'name': name,
        u'creation_date': time(),
        u'user_likes': {}
    }
    doc_ref.set(data)

    package = {
        "id" : key
    }
    return jsonify(package)

def main(requests):
    if requests:
        json = requests.get_json()
        if 'name' in json:
            name = json['name']
            if name:
                print("DEBUG: Processing Request")
                return addUser()
            else:
                #TODO make status code response instead
                raise NoInput("Name was Empty in Request")
    else:
        #TODO make status code response instead
        raise NoInput("Header was Empty in Request")
