
import uuid
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.models.product import Product


class ProductRepository:
    
    def __init__(self, db: AsyncSession):
        self.db = db
        
    async def get_by_id(self, id: uuid):
        result = await self.db.execute(
            select(Product).where(Product.id == id)
        )
        return result.scalar_one_or_none()
        
    async def create(self, product: Product) -> Product:
        self.db.add(product)
        await self.db.commit()
        await self.db.refresh(product)
        return product
        