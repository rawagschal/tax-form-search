from app.db import Base
from sqlalchemy import Column, Integer, String


class Form(Base):
    __tablename__ = 'forms'
    form_name = Column(String(50), primary_key=True)
    form_title = Column(String(50), nullable=False)
    min_year = Column(Integer, nullable=False)
    max_year = Column(Integer, nullable=False)
