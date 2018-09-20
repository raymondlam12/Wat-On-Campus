import os

SECRET_KEY = 'A93wiqp8Jqnei983Ji82P0192NuqheNJi938J'

MYSQL_USER = 'root' #os.environ['MYSQL_USER']
MYSQL_PASSWORD = 'password' #os.environ['MYSQL_PASSWORD']
SQLALCHEMY_DATABASE_URI = 'mysql://{}:{}@localhost/testing_db'.format(MYSQL_USER, MYSQL_PASSWORD)
SQLALCHEMY_TRACK_MODIFICATIONS = False

GOOGLE_MAPS_API_KEY = os.environ['GOOGLE_MAPS_API_KEY']

