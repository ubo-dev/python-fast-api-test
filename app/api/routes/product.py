
from fastapi import APIRouter, Depends
from pytest import Session

from app.api.deps import get_db
from app.schemas.product import ProductRequest
from app.service.product_service import ProductService


router = APIRouter()

@router.post("/add")
async def add_product(product_request: ProductRequest, db: Session = Depends(get_db)):
    service = ProductService(db)
    return await service.add_product(product_request)