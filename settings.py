import os
from os.path import join, dirname
from dotenv import load_dotenv

load_dotenv(verbose=True)

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

USERNAME = os.getenv('USERNAME')
PASSWORD = os.getenv('PASSWORD')

# The repository to add this issue to
REPO_OWNER = os.getenv('REPO_OWNER')
REPO_NAME = os.getenv('REPO_NAME')

TITLE = os.getenv('TITLE')
BODY = os.getenv('BODY')

if os.getenv('LABELS'):
  LABELS = os.getenv('LABELS').split(',')
else:
  LABELS = ''
