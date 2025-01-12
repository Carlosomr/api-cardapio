import os
from urllib.parse import quote_plus

class Config:
    SECRET_KEY = os.getenv('SECRET_KEY', 'your_secret_key')
    DATABASE_USER = os.getenv('DATABASE_USER', 'postgres')
    DATABASE_PASSWORD = os.getenv('DATABASE_PASSWORD', 'Suporte0!@#$%¨&*(')
    DATABASE_HOST = os.getenv('DATABASE_HOST', 'indistinctly-infinite-narwhal.data-1.use1.tembo.io')
    DATABASE_PORT = os.getenv('DATABASE_PORT', '5432')
    DATABASE_NAME = os.getenv('DATABASE_NAME', 'postgres')

    DATABASE_URI = f"postgresql://{DATABASE_USER}:{quote_plus(DATABASE_PASSWORD)}@{DATABASE_HOST}:{DATABASE_PORT}/{DATABASE_NAME}"
    SQLALCHEMY_DATABASE_URI = DATABASE_URI
    SQLALCHEMY_TRACK_MODIFICATIONS = False
