from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from backend.routes.predict import router as predict_router   # fixed
from fastapi.staticfiles import StaticFiles
import os

app = FastAPI(title="Heart Disease Prediction API")

# CORS middleware config - adjust origins if needed
origins = [
    "http://localhost:8080",
    "http://127.0.0.1:8080",
    "http://localhost",        # for local file testing maybe
    "http://127.0.0.1",        # add these for more coverage
    "file://",                 # optional: allow local file access (sometimes needed)
    "*",                       # (dev only) allow all origins to avoid issues
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,  # For dev, you can use ["*"] to allow all origins
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include prediction router
app.include_router(predict_router)

@app.get("/api")
def read_root():
    return {"message": "Heart Disease Prediction API is running"}

# Setup frontend static files mount
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))  # Demo/
FRONTEND_DIR = os.path.join(BASE_DIR, "frontend")

# Mount frontend at /frontend so it does NOT override the root path or docs
app.mount("/", StaticFiles(directory=FRONTEND_DIR, html=True), name="frontend")
# Now the frontend is accessible at the root path, and API docs at /docs
