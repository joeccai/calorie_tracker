from flask import Flask, request, jsonify
from models import db, bcrypt, User, DailyCalories, Goal
from config import Config
from flask_mail import Mail, Message
import boto3
from datetime import datetime

app = Flask(__name__)
app.config.from_object(Config)

db.init_app(app)
bcrypt.init_app(app)
mail = Mail(app)

@app.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    hashed_password = bcrypt.generate_password_hash(data['password']).decode('utf-8')
    new_user = User(username=data['username'], email=data['email'], password=hashed_password)
    db.session.add(new_user)
    db.session.commit()
    return jsonify({'message': 'User registered successfully'})

@app.route('/login', methods=['POST'])
def login():
    # Implement login logic
    pass

@app.route('/add_calories', methods=['POST'])
def add_calories():
    data = request.get_json()
    new_calories = DailyCalories(user_id=data['user_id'], date=datetime.strptime(data['date'], '%Y-%m-%d'), calories=data['calories'])
    db.session.add(new_calories)
    db.session.commit()
    return jsonify({'message': 'Calories added successfully'})

@app.route('/set_goal', methods=['POST'])
def set_goal():
    data = request.get_json()
    new_goal = Goal(user_id=data['user_id'], daily_calorie_goal=data['daily_calorie_goal'], start_date=datetime.strptime(data['start_date'], '%Y-%m-%d'), end_date=datetime.strptime(data['end_date'], '%Y-%m-%d'))
    db.session.add(new_goal)
    db.session.commit()
    return jsonify({'message': 'Goal set successfully'})

@app.route('/compare_periods', methods=['GET'])
def compare_periods():
    # Implement comparison logic
    pass

@app.route('/send_reminders', methods=['POST'])
def send_reminders():
    users = User.query.all()
    for user in users:
        msg = Message('Daily Calorie Reminder', sender='your_email@example.com', recipients=[user.email])
        msg.body = f"Hi {user.username}, don't forget to log your daily calories!"
        mail.send(msg)
    return jsonify({'message': 'Reminders sent successfully'})

if __name__ == '__main__':
    app.run(debug=True)
