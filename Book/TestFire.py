import pyrebase


def getdb():

    config = {
        #enter config here
    }

    firebase = pyrebase.initialize_app(config)
    auth = firebase.auth()
    db = firebase.database()

    return db

def getstore():
    config = {
        #enter config here
    }
    firebase = pyrebase.initialize_app(config)
    auth = firebase.auth()
    storage = firebase.storage()

    return storage

if __name__ == "__main__":
    getdb()
    getstore()