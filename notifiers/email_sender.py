from typing import Any

from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail

from settings import SENDGRID_API_KEY, FROM_EMAIL


def send_emails(message):
    sg = SendGridAPIClient(SENDGRID_API_KEY)
    response = sg.send(message)
    return {
        'status': response.status_code,
        'body': response.body,
        'headers': response.headers
    }

def create_html_message(model_name: str, model_id: int, user_id: int, updated_data: dict) -> str:
    header: str = f'<h3>The {model_name} with id {model_id} has been updated by user with id {user_id}, making the following changes:</h3>'
    updates: str = '<ul>'
    for key, value in updated_data.items():
        if value is not None:
            updates += f'<li>{key}: {value}</li>'
    updates += '</ul>'
    return f'{header} {updates}'

def create_email_message(model_name: str, notification_data: Any):
    html_message = create_html_message(
        model_name,
        notification_data.id,
        notification_data.user_id,
        notification_data.update_info.dict()
    )
    message = Mail(
        from_email=FROM_EMAIL,
        to_emails=notification_data.emails,
        subject='Admin Notification',
        html_content=html_message
    )
    return message
