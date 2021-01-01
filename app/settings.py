import os
from dotenv import load_dotenv

load_dotenv(verbose=True)

YOUTUBE_API_KEY = os.environ['YOUTUBE_API_KEY']
NHK_CHANNEL_ID = os.environ['NHK_CHANNEL_ID']

