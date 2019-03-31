import database
from flask import jsonify
from firebase_admin import firestore
from time import time

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

    interest_db = database.db.collection(
        u'interests').document(args['interest']['name'])
    interest_data = interest_db.get().to_dict()
    # If already defined interest
    try:
        interest_data['users'][args['user']] = time()
    except TypeError:
        # Otherwise define and add user
        interest_data = {
            'users': {
                args['user']: time()
            }
        }

    # Update size of total_users
    interest_data['total_users'] = len(interest_data['users'])
    interest_db.set(interest_data)

    data = doc_ref.get().to_dict()
    previous_interests = data['user_likes']
    if database.DEBUG:
        print("DEBUG: Previous Interests are {0}".format(previous_interests))

    # Add new interest
    # TODO Add values/specifics
    previous_interests[args['interest']['name']] = args['interest']['level']

    doc_ref.set(data)

    if database.DEBUG:
        print("DEBUG: New Interests are {0}".format(previous_interests))

    # If reached this point, all was successful
    package = {
        'interests': previous_interests,
        'success': True
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
        'success': True
    }
    return jsonify(package)


def remove_interest(args):
    """
    Remove User Interest
    """
    doc_ref = database.db.collection(u'users').document(args['user'])
    interest_db = database.db.collection(
        u'interests').document(args['interest']['name'])
    interest_data = interest_db.get().to_dict()
    try:
        del interest_data['users'][args['user']]
    except KeyError:
        # If user doesn't exists in that interest don't worry about it
        print("Warning: User was not in this interest - Possible Client-side Error")
        pass

    # Update size of total_users
    interest_data['total_users'] = len(interest_data['users'])
    interest_db.set(interest_data)

    data = doc_ref.get().to_dict()
    previous_interests = data['user_likes']
    if database.DEBUG:
        print("DEBUG: Previous Interests are {0}".format(previous_interests))

    # Remove Interest
    del previous_interests[args['interest']['name']]

    doc_ref.update(data)

    if database.DEBUG:
        print("DEBUG: New Interests are {0}".format(previous_interests))

    # If reached this point, all was successful
    package = {
        'interests': previous_interests,
        'success': True
    }
    return jsonify(package)

def get_popular(number):
    interest_db = database.db.collection(
        u'interests').order_by(u'total_users', direction=firestore.Query.DESCENDING).limit(number).get()
    interest_data = [{d.id:d.to_dict()} for d in interest_db]

    # Functions to sort data
    for datapoint in interest_data:
        for key in datapoint.keys():
            del datapoint[key]['users']

    return interest_data

print(get_popular(10))

def get_user_popular(args):
    pass
