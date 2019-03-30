from time import time
from flask import jsonify
from firebase_admin import firestore
import database

#Problem: Users with same name will cause overwrite of data.
def addUser(name):
    """
    Add User
    """
    doc_ref = database.db.collection(u'users').document()
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
