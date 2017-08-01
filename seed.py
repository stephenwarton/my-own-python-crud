from models import Users
from models import Reviews
from app import db

user1 = Users('simba@lionking.com', 'mufasa')
user2 = Users('hello@goodbye.com', 'lateralligator')
review1 = Reviews('apple review', 'pretty nice', 1)
review2 = Reviews('banana', 'not yellow enough', 1)
review3 = Reviews('popcorn', 'good amount of salt', 2)
review4 = Reviews('review for chips', 'nice and crunchy', 1)
review5 = Reviews('tortilla chips', 'wish i had some salsa', 2)

db.session.add(user1)
db.session.add(user2)
db.session.add(review1)
db.session.add(review2)
db.session.add(review3)
db.session.add(review4)
db.session.add(review5)
db.session.commit()
