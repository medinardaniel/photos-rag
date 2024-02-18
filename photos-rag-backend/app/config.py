# config.py
import os
from dotenv import load_dotenv

class Config:
    DEBUG = False

    # get the current directory
    basedir = os.path.abspath(os.path.dirname(__file__))
    # specify the path to the .env file
    load_dotenv(os.path.join(basedir, '.env'))
    # load the environment variables from the .env file
    OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')
    MONGODB_URI = os.getenv('MONGO_URI')

    S3_BUCKET = os.getenv('S3_BUCKET')

class DevelopmentConfig(Config):
    DEBUG = True
