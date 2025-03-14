from fastapi import FastAPI
from app.routes import router

app = FastAPI(title="SRS & ER Parser")

# Include Routes
app.include_router(router)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8001)
