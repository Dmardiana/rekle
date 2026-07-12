from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api.v1.api import api_router
from app.api.v1.endpoints import scan
from app.core.config import settings
from fastapi.staticfiles import StaticFiles

app = FastAPI(title="REKLE Backend")

# ─────────────────────────────────────────────
# CORS (Pilihan B)
# ─────────────────────────────────────────────
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost",
        "capacitor://localhost",  # <--- Ini origin resmi dari APK Android kamu
        "http://192.168.100.26",
        "http://192.168.100.26:5173",
        "http://192.168.100.26:8000"
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ─────────────────────────────────────────────
# ROUTERS
# ─────────────────────────────────────────────
app.include_router(api_router, prefix="/api/v1")
app.include_router(scan.router, prefix="/api/v1")
app.mount("/uploads", StaticFiles(directory="uploads"), name="uploads")

@app.get("/")
def read_root():
    return {
        "message": "Welcome to REKLE backend"
    }