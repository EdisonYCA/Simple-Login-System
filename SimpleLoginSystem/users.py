import pickle
# Dictionary containing a list of user information
database = {}


# Pickle database so new sign ups are permanently stored
def store_users():
    with open('database.pickle', 'wb') as data:
        pickle.dump(database, data, pickle.HIGHEST_PROTOCOL)


# read current pickled values into dictionary 'read'
def read_users():
    read = {}
    with open('database.pickle', 'rb') as data:
        read = pickle.load(data)
    return read
