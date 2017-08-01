# dependencies
from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy

# app config
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://localhost/pythoncrud'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

import models


# routes
@app.route('/api/v1/users', methods=['GET'])
def index():
    all_data = []
    users = models.Users.query.all()
    for user in users:
        all_data.append({
            'email': user.email,
            'password': user.password
        })
    return jsonify(all_data)


if __name__ == '__main__':
    app.debug = True
    app.run()
