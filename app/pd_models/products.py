from typing import Optional, List
from pydantic import BaseModel


class ProductUpdate(BaseModel):
    sku: Optional[str]
    name: Optional[str]
    price: Optional[float]
    brand: Optional[str]
    anonymous_views: Optional[int]
    name: Optional[str]

class ProductUpdateNotification(BaseModel):
    update_info: ProductUpdate
    id: int
    user_id: int
    emails: List[str]
