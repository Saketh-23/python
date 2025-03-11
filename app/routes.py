from fastapi import APIRouter, UploadFile, File
import shutil
from app.workflow import process_files

router = APIRouter()

@router.post("/upload/")
async def upload_files(srs: UploadFile = File(...), er_diagram: UploadFile = File(...)):
    srs_filename = f"uploads/{srs.filename}"
    er_filename = f"uploads/{er_diagram.filename}"

    # Save uploaded files
    with open(srs_filename, "wb") as buffer:
        shutil.copyfileobj(srs.file, buffer)

    with open(er_filename, "wb") as buffer:
        shutil.copyfileobj(er_diagram.file, buffer)

    # Execute workflow
    result = process_files(srs_filename, er_filename)
    return {"message": "Processing started", "result": result}
