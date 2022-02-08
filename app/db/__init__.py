from os import getenv
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv
import requests
from bs4 import BeautifulSoup

load_dotenv()

engine = create_engine(getenv('DB_URL'), echo=True, pool_size=20, max_overflow=0)
Session = sessionmaker(bind=engine)
Base = declarative_base()

# db = Session()

# page = requests.get('https://apps.irs.gov/app/picklist/list/priorFormPublication.html')
# soup = BeautifulSoup(page.content, 'html.parser')

# links = soup.select('table tbody tr td.LeftCellSpacer a')
# sample10 = links[:10]
# for anchor in sample10:
#     print(anchor.text)
