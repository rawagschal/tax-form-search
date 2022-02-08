

from app.models import Form
from app.db import Session, Base, engine
 
# from bs4 import BeautifulSoup

Base.metadata.drop_all(engine)
Base.metadata.create_all(engine)

db = Session()

# SAMPLE DATA
db.add_all([
    Form(form_name='W-2', form_title='This year wages', min_year='1980', max_year='1990'),
    Form(form_name='X-4', form_title='how to do taxes', min_year='1990', max_year='2000'),
])

# ! HOW DO I DO THIS SO IT'S NOT IN A SEEDS FILE? 
# app/__init__.py maybe?
# IRS DATA (currently returning all data per row)
# page = requests.get('https://apps.irs.gov/app/picklist/list/priorFormPublication.html')
# soup = BeautifulSoup(page.content, 'html.parser')
# links = soup.get_text('td', {'class': 'LeftCellSpacer'})
# form_number = soup.get_text(links, 'a')
# print(form_number)

db.commit()

db.close()

