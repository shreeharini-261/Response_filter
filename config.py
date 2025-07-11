import os
class Config:
    # Simple hardcoded secret key for testing
    SECRET_KEY = 'dev-test-key-123'  # This can be any simple string for testing
    
    # MySQL connection - replace 'damn' with your actual MySQL root password
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:damn@localhost/flask_demo'
    SQLALCHEMY_TRACK_MODIFICATIONS = False