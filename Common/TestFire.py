import pyrebase


def getdb():
    config = {
     #key here
    }
    firebase = pyrebase.initialize_app(config)
    db = firebase.database()

    return db


if __name__ == "__main__":
    getdb()
