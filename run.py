from app.main import app  # ✅ Import FastAPI app explicitly
import uvicorn

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000, reload=True)
