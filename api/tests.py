# Main Application File
import app as main

# Functions Needed to be Tested
from user import create, interests


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


def test():
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


# Invoke of Tester
test()


# Huge invoke test
for _ in range(100):
    test()
