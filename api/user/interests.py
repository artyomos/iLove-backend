import database
from flask import jsonify
from firebase_admin import firestore

'''
Args Stuff
args = {
    'user': user,
    'interest': {
        'name': user_interest,
        'level': level_of_interest
    }
}
'''
def add_interest(args):
    """
    Add User Interest
    """
    doc_ref = database.db.collection(u'users').document(args['user'])


    data = doc_ref.get().to_dict()
    previous_interests = data['user_likes']
    if database.DEBUG: print("DEBUG: Previous Interests are {0}".format(previous_interests))

    # Add new interest
    #TODO Add values/specifics
    previous_interests[args['interest']['name']] = args['interest']['level']

    doc_ref.set(data)

    if database.DEBUG: print("DEBUG: New Interests are {0}".format(previous_interests))

    # If reached this point, all was successful
    package = {
        'interests': previous_interests,
        'success':True
    }
    return jsonify(package)

def get_interest(args):
    """
    Return User Interest
    """
    doc_ref = database.db.collection(u'users').document(args['user'])

    data = doc_ref.get().to_dict()
    previous_interests = data['user_likes']

    package = {
        'interests': previous_interests,
        'success':True
    }
    return jsonify(package)


def remove_interest(args):
    """
    Remove User Interest
    """
    doc_ref = database.db.collection(u'users').document(args['user'])

    data = doc_ref.get().to_dict()
    previous_interests = data['user_likes']
    if database.DEBUG: print("DEBUG: Previous Interests are {0}".format(previous_interests))

    # Remove Interest
    del previous_interests[args['interest']['name']]

    doc_ref.update(data)

    if database.DEBUG: print("DEBUG: New Interests are {0}".format(previous_interests))

    # If reached this point, all was successful
    package = {
        'interests': previous_interests,
        'success':True
    }
    return jsonify(package)
