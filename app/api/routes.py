from fastapi import APIRouter

from app.pd_models.products import ProductUpdateNotification
from app.notifiers.email_sender import send_emails, create_email_message


router = APIRouter()

@router.post('/email/product/')
def email_product_update(notification_data: ProductUpdateNotification):
    try:
        message = create_email_message('product', notification_data)
        response = send_emails(message)
        return response
    except Exception as e:
        return {
            'status': 500,
            'error': str(e)
        }
