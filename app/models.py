from sqlalchemy import Column, Integer, String, Text
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class ExtractedData(Base):
    __tablename__ = "extracted_data"

    id = Column(Integer, primary_key=True, index=True)
    srs_filename = Column(String, index=True)
    er_filename = Column(String, index=True)
    api_schema = Column(Text)  # JSON stored as text
    db_schema = Column(Text)   # JSON stored as text
