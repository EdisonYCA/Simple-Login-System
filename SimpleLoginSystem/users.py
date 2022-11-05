import pickle
# Dictionary containing a list of user information
database = {"edison1278": "123", "micheal1278": "124", "jeremy1278": "125"}


def store_users():
    # Pickle database so members can be remembered
    with open('database.pickle', 'wb') as data:
        pickle.dump(database, data, pickle.HIGHEST_PROTOCOL)


def read_users():
    with open('database.pickle', 'rb') as data:
        read = pickle.load(data)
