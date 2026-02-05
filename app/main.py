from fastapi import FastAPI, Depends, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session
from app.api import api_router

# app instance
app = FastAPI(
    title="My FastAPI App",
    description="Backend API for SaaS application",
    version="1.0.0",
)

app.include_router(api_router)
# -------------------------
# CORS Middleware
# -------------------------
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # change in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# -------------------------
# Root Route
# -------------------------
@app.get("/")
def health_check():
    return {
        "status": "success",
        "message": "FastAPI server is running 🚀"
    }

# -------------------------
# Example API Route
# -------------------------
@app.get("/ping")
def ping():
    return {"message": "pong"}

# -------------------------
# Global Exception Handler
# -------------------------
@app.exception_handler(Exception)
async def global_exception_handler(request, exc):
    return JSONResponse(
        status_code=500,
        content={"error": "Internal Server Error"},
    )
