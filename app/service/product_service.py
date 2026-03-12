
from pytest import Session

from app.models.product import Product
from app.repository.product_repository import ProductRepository
from app.schemas.product import ProductRequest


class ProductService:
    
    def __init__(self, db: Session):
        self.repository = ProductRepository(db)
        
    async def add_product(self, product_request: ProductRequest):
        
        product = Product(
            name = product_request.name,
            product_type = product_request.product_type
        )
        
        return await self.repository.create(product)