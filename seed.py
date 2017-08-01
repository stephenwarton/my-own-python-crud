from models import Users
from app import db

user1 = Users('simba@lionking.com', 'mufasa')
user2 = Users('hello@goodbye.com', 'lateralligator')

db.session.add(user1)
db.session.add(user2)
db.session.commit()
