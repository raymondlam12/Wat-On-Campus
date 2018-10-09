from app import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(120), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    hashed_password = db.Column(db.String(120), unique=False, nullable=False)
    # TODO: Add salt to hash for password
    # salt = db.Column(db.String(120), unique=False, nullable=False)
    events = db.relationship('Event', backref='user', lazy=True)

    def __init__(self, username=None, email=None, hashed_password=None):
        self.username = username
        self.email = email
        self.hashed_password = hashed_password

    def serialize_user(self):
        return {
            "username": self.username,
            "email": self.email
        }

class Event(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    description = db.Column(db.Text(), unique=False, nullable=False)
    title = db.Column(db.String(120), unique=False, nullable=False)
    location = db.Column(db.String(120), unique=False, nullable=False)
    date = db.Column(db.String(120), unique=False, nullable=False)

    def __init__(self, user_id=None, description=None, title=None, location=None, date=None):
        self.user_id = user_id
        self.description = description
        self.title = title
        self.location = location
        self.date = date

    def serialize_event(self):
        return {
            "user_id": self.user_id,
            "description": self.description,
            "title": self.title,
            "location": self.location,
            "date": self.date
        }
