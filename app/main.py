from fastapi import FastAPI
from app.routers.goods_receipts import router as goods_receipt_router
from app.routers.purchase_orders import router as purchase_order_router
from app.routers.auth import router as auth_router
from app.routers.vendors import router as vendor_router
from app.routers.materials import router as material_router
from app.routers.purchase_requisitions import (
    router as purchase_requisition_router,
)

app = FastAPI(
    title="SAP Procurement System",
    version="1.0.0",
)

app.include_router(auth_router)
app.include_router(vendor_router)
app.include_router(material_router)
app.include_router(purchase_requisition_router)
app.include_router(purchase_order_router)
app.include_router(goods_receipt_router)


@app.get("/")
def home():
    return {
        "message": "SAP Procurement System API is Running"
    }