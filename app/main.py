from fastapi import FastAPI
from app.routers.vendors import router as vendor_router
from app.routers.auth import router as auth_router
from app.routers.materials import router as material_router
app = FastAPI(
    title="SAP Procurement System",
    version="1.0.0"
)

app.include_router(auth_router)
app.include_router(vendor_router)
app.include_router(material_router)

@app.get("/")
def home():
    return {
        "message": "SAP Procurement System API is Running"
    }