from app import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(120), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    hashed_password = db.Column(db.String(120), unique=False, nullable=False)
    # TODO: Add salt to hash for password
    # salt = db.Column(db.String(120), unique=False, nullable=False)

    def __init__(self, username=None, email=None, hashed_password=None, session_id=None):
        self.username = username
        self.email = email
        self.hashed_password = hashed_password
        self.session_id = session_id

