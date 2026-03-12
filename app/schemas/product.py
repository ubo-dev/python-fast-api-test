import uuid
from pydantic import BaseModel, ConfigDict
from sqlalchemy import true

from app.models.enums.product_type import ProductType


class ProductBase(BaseModel):
    name: str
    product_type: ProductType
        
class ProductRequest(ProductBase):
    pass

class ProductRead(ProductBase):
    id: uuid.UUID
    
    model_config = ConfigDict(from_attributes=True)

class AddToCartRequest():
    product_id: uuid.UUID