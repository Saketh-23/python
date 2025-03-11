from app.database import SessionLocal
from app.models import ExtractedData
import json

def store_extracted_data(srs_filename, er_filename, api_schema, db_schema):
    db = SessionLocal()
    entry = ExtractedData(
        srs_filename=srs_filename,
        er_filename=er_filename,
        api_schema=json.dumps(api_schema),
        db_schema=json.dumps(db_schema),
    )
    db.add(entry)
    db.commit()
    db.close()
