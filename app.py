from flask import Flask, render_template, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import pytz

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///messages.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  # Disable modification tracking
db = SQLAlchemy(app)

class Message(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(128), nullable=False)
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)

# Function to clear messages
def clear_messages():
    with app.app_context():
        db.session.query(Message).delete()
        db.session.commit()

# clear messages on startup
clear_messages()

@app.route('/')
def index():
    messages = Message.query.order_by(Message.timestamp.desc()).all()
    # Convert timestamps
    target_timezone = pytz.timezone('America/New_York') 
    for message in messages:
        # Ensure the timestamp is in UTC before converting
        message.timestamp = message.timestamp.replace(tzinfo=pytz.utc)
        message.timestamp = message.timestamp.astimezone(target_timezone)

    return render_template('index.html', messages=messages)

@app.route('/post', methods=['POST'])
def post_message():
    content = request.form.get('content')
    if not content or len(content) > 128:
        return jsonify({'status': 'error', 'message': 'Invalid message'})

    new_message = Message(content=content, timestamp=datetime.utcnow().replace(tzinfo=pytz.utc))
    db.session.add(new_message)
    db.session.commit()

    return jsonify({'status': 'success', 'message': 'Message posted'})

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=False)