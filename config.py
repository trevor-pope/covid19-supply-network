DATABASE_URL = "mysql+pymysql://root:password@localhost:3306/covid_supply"

class Config(object):
    """Base config, uses staging database server."""
    DEBUG = False
    TESTING = False
    MYSQL_DATABASE_USER = 'root'
    MYSQL_DATABASE_PASSWORD = 'password'
    MYSQL_DATABASE_DB = 'covid_supply'
    MYSQL_DATABASE_HOST = 'localhost'
    SQLALCHEMY_DATABASE_URI = f'mysql+pymysql://{MYSQL_DATABASE_USER}:{MYSQL_DATABASE_PASSWORD}@{MYSQL_DATABASE_HOST}/{MYSQL_DATABASE_DB}'
