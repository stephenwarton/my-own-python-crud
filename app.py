# dependencies
from flask import Flask, jsonify, request, json, render_template
from flask_sqlalchemy import SQLAlchemy

# app config
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://localhost/pythoncrud'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

import models


# routes
@app.route('/api/v1/users', methods=['GET'])
def users():
    all_data = []
    users = models.Users.query.all()
    for user in users:
        all_data.append({
            'email': user.email,
            'password': user.password
        })
    return jsonify(all_data)


@app.route('/api/v1/reviews', methods=['GET'])
def reviews():
    all_data = []
    reviews = models.Reviews.query.all()
    for review in reviews:
        all_data.append({
            'title': review.title,
            'description': review.description,
            'user_id': review.user_id
        })
    return jsonify(all_data)


@app.route('/api/v1/users/<user_id>')
def getUserById(user_id):
    user = models.Users.query.filter_by(id=user_id).first_or_404()
    return jsonify({'id': user.id, 'email': user.email, 'password': user.password})


@app.route('/api/v1/reviews/<review_id>')
def getReviewById(review_id):
    review = models.Reviews.query.filter_by(id=review_id).first_or_404()
    return jsonify({'id': review.id, 'title': review.title, 'description': review.description, 'user_id': review.user_id})


if __name__ == '__main__':
    app.debug = True
    app.run()
