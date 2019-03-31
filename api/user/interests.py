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

    # Ensure proper ID was grabbed
    assert(doc_ref.id == args['user'])

    data = doc_ref.get().to_dict()
    previous_interests = data['user_likes']
    print("DEBUG: Previous Interests are {0}".format(previous_interests))

    # Add new interest
    #TODO Add values/specifics
    previous_interests[args['interest']['name']] = args['interest']['level']

    doc_ref.set(data)

    print("DEBUG: New Interests are {0}".format(previous_interests))

    # If reached this point, all was successful
    package = {
        'success':True
    }
    return jsonify(package)

def remove_interest(args):
    """
    Remove User Interest
    """
    doc_ref = database.db.collection(u'users').document(args['user'])

    # Ensure proper ID was grabbed
    assert(doc_ref.id == args['user'])

    data = doc_ref.get().to_dict()
    previous_interests = data['user_likes']
    print("DEBUG: Previous Interests are {0}".format(previous_interests))

    # Remove Interest
    del previous_interests[args['interest']['name']]

    doc_ref.update(data)

    print("DEBUG: New Interests are {0}".format(previous_interests))

    # If reached this point, all was successful
    package = {
        'success':True
    }
    return jsonify(package)
