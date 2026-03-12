
from typing import List
import uuid
from pydantic import BaseModel

from app.models.product import Product


class CartBase(BaseModel):
    products: List[Product]
    user_id: uuid.UUID