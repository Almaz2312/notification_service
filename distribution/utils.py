from twilio.rest import Client
from django.conf import settings

from message.models import Message


def send_sms(distribution_model, user):
    client = Client(settings.TWILIO_SID, settings.TWILIO_AUTH_TOKEN, http_client=settings.TWILIO_HTTP_PROXY)
    sms = client.messages.create(
            body=distribution_model.get("text"),
            from_=settings.TWILIO_PHONE_NUMBER,
            to='+' + str(user.phone_number)
        )
    return sms


def create_message_model(distribution_model, user):
    message = Message(created_datetiem=distribution_model.get("sending_datetime"),
                      distribution=distribution_model.get("id"),
                      client=user.id)
    message.save()
    return message
