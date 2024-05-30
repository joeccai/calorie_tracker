import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'your_secret_key'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'mysql+pymysql://username:password@hostname/dbname'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    MAIL_SERVER = 'email-smtp.us-east-1.amazonaws.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get('SES_SMTP_USERNAME')
    MAIL_PASSWORD = os.environ.get('SES_SMTP_PASSWORD')
