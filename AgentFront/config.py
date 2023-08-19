import os

SECRET_KEY = os.urandom(24)

# 配置mysql数据库
HOSTNAME = '127.0.0.1'
PORT = '3306'
DATABASE = 'idea_bank'
USERNAME = 'root'
PASSWORD = '110110'

# 配置数据库的连接地址
DB_URI = 'mysql+pymysql://' + USERNAME + ':' + PASSWORD + '@' + HOSTNAME \
                                        + ':' + PORT + '/' + DATABASE + "?charset=utf8mb4"
SQLALCHEMY_DATABASE_URI = DB_URI
SQLALCHEMY_TRACK_MODIFICATIONS = True
REDIS_URL = 'redis://localhost:6379/0'
