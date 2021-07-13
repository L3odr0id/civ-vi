import firebase_admin
from firebase_admin import credentials
from firebase_admin import db


# Loads the parsed data into the Firebase DB
def pushToFirebase(data):
    # Fetch the service account key JSON file contents
    cred = credentials.Certificate('key/serviceAccountKey.json')

    # Initialize the app with a service account, granting admin privileges
    firebase_admin.initialize_app(cred, {
        'databaseURL': open('key/databaseURL.txt', 'r').read()
    })

    # As an admin, the app has access to read and write all data, regradless of Security Rules
    ref = db.reference('/table')
    ref.set(data)
