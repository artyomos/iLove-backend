#Database test


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
    doc_ref = db.collection(u'users')
    data = {
        u'name': name,
        u'user_likes': {}
    }
    request = doc_ref.add(data)

addUser('Apple')
def main(requests):
    if requests:
        print("DEBUG: Found Request")
        json = requests.get_json()
        if 'name' in json:
            print("DEBUG: Processing Request")
            addUser(json['name'])

    users_ref = db.collection(u'users')
    docs = users_ref.get()

    for doc in docs:
        print(u'{} => {}'.format(doc.id, doc.to_dict()))
