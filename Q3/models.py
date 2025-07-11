# paste teachers models.py in here

from flask_login import UserMixin
import pymongo

# init SQLAlchemy so we can use it later in our models
connection = pymongo.MongoClient('mongodb://localhost:27017')
db = connection['fitwell']

# connect to MongoDB
# my collection is called userDetails
connection = pymongo.MongoClient('mongodb://localhost:27017')
db = connection['Qns2CatalogDB']



class User(UserMixin):
    def __init__(self, email, record):
        self.email = email
        self.record = record

    def get_email(self):
        return self.email

    def get_id(self):
        return self.email

    def get_record(self):
        return self.record

class fitwellUser():

    def __init__(self, email, password, NRIC):
        db.userDetails.insert_one({'email': email, 'password': password, 'nric': NRIC})

    def get_user_byId(email):
        filter = {}
        filter['email'] = email

        aCursor = db.userDetails.find(filter).limit(1)

        if aCursor.count() == 1:
            return User(email=email, record=aCursor.next())
        else: 
            return None