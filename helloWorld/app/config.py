class Config:
    SQLALCHEMY_DATABASE_URI = 'mysql://root:root@localhost/demo_1'
    SECRET_KEY = 'many random bytes'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_ECHO = True