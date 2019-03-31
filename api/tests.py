# Main Application File
import main
import csv

# Functions Needed to be Tested
from user import create, interests
from flask import jsonify
import random

def check_value(test_name, expected_value, received_value):
    try:
        assert(expected_value == received_value)
        print("PASSED: {0}".format(test_name))
        return 1
    except AssertionError:
        print("FAILED: {0}".format(test_name))
        print("Received: {0}".format(received_value))
        print("Expected: {0}".format(expected_value))
        return 0


# Globals for Keeping Track of Test Success/Failure
total = 0
success = 0


def increment(result):
    global success
    global total
    if result:
        success += 1
    total += 1

### Flask Testing Function ###

# Test of api (actual http request) functions
def api_test():
    with main.app.app_context():
        # Test of Total_Interests Function
        data = {
            'limit':3
        }
        print('Test of Total_Interests: {0}'.format(main.total_interests(jsonify(data)).get_json()))

        ### Test of API versions of Test

        # Test of User Register
        data = {
            'name':'Test User'
        }

        user = main.create_user(jsonify(data)).get_json()
        print('Test of User API: {0}'.format(user))

        # Test of Interest API
        data = {
        "id":user['id'],
        "type": "add",
        "interest": {
          "name":"Riolu",
          "level":100
          }
        }
        # Test of ADD Interests API
        print('Test of Add Interest: {0}'.format(main.interests_api(jsonify(data)).get_json()))
        # Test of GET Interests API
        data['type'] = 'get'
        print('Test of Get Interest: {0}'.format(main.interests_api(jsonify(data)).get_json()))
        # Test of REMOVE Interests API
        data['type'] = 'remove'
        print('Test of Remove Interest: {0}'.format(main.interests_api(jsonify(data)).get_json()))

        print("All Functions Tests Completed (Check for Passing)")

# api_test()

# Note: Run Old_Test for verifiable results
def test(max_tests=0):
    with main.app.app_context():
        print("Executing Extraneous Tests ({0} Total!!)\nNote that Interests can be duplicate!".format(max_tests))

        # List of possible interests for the sample dummies
        with open('hobbies.csv') as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            possible_interests = csv_reader.__next__()

        # List of possible names (First name only)
        with open('names.csv') as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            possible_names = csv_reader.__next__()

        # Old Interests
        #possible_interests = ['animal watching', 'doggos', 'cats', 'sergals', 'dolphins', 'Apple Inc.', 'Google', 'Python', 'C++', 'Java', 'Art', 'Cinematography', 'Programming', 'Death']
        # Old Names
        #possible_names = ['Jeremiah', 'Dereck', 'Adam', 'Steve', 'Susan', 'Oreo', 'Andy', 'Artyom', 'Jessie', 'Alex', 'Jonathan', 'Kevin', 'Majira']

        for i in range(max_tests):
            name = random.choice(possible_names)
            print("Test {0}: Added User {1}".format(i+1, name))
            user = create.addUser(name).get_json()
            for _ in range(random.randint(5, 100)):
                interest = random.choice(possible_interests)
                level = random.randint(-10, 1000)
                package = {
                    'user': user['id'],
                    'interest': {
                        'name': interest,
                        'level': level
                    }
                }
                print("Test {0}: Added Interest {1} with Interest Level {2}".format(i+1, interest, level))
                interests.add_interest(package)

        print("Completed all tests! :)")

def legacy_test():
    with main.app.app_context():
        user = create.addUser("Anubis").get_json()

        # Make sure correct value is received
        increment(check_value("Creation of User 'Anubis'",
                              "Created Reference for user: Anubis", user['debug']))

        # Add Interest Package
        package = {
            'user': user['id'],
            'interest': {
                'name': 'huskies',
                'level': 9999999
            }
        }
        given = interests.add_interest(package).get_json()

        increment(check_value("Adding of Huskies :)", {
                  'huskies': 9999999}, given['interests']))

        # Add Another Package to Test User
        package = {
            'user': user['id'],
            'interest': {
                'name': 'pokemon',
                'level': 100
            }
        }
        given = interests.add_interest(package).get_json()

        increment(check_value("Adding of Pokemon", {
                  'huskies': 9999999, 'pokemon': 100}, given['interests']))

        # Add One More Interest
        package = {
            'user': user['id'],
            'interest': {
                'name': 'useless',
                'level': 1
            }
        }
        given = interests.add_interest(package).get_json()

        increment(check_value("Adding of Dummy Interest", {
                  'huskies': 9999999, 'pokemon': 100, 'useless': 1}, given['interests']))

        # Remove Previously added Interest
        given = interests.remove_interest(package).get_json()

        increment(check_value("Removal of Dummy Interest", {
                  'huskies': 9999999, 'pokemon': 100}, given['interests']))

        print("{0}/{1} Tests Passed".format(success, total))

# Old Test Function
#legacy_test()


# Invoke of Tester
test(1000)
