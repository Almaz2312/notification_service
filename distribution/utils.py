import os.path

import requests
from twilio.rest import Client
from django.conf import settings

from message.models import Message


# def send_sms(distribution_model, user):
#     client = Client(settings.TWILIO_SID, settings.TWILIO_AUTH_TOKEN, http_client=settings.TWILIO_HTTP_PROXY)
#     sms = client.messages.create(
#             body=distribution_model.get("text"),
#             from_=settings.TWILIO_PHONE_NUMBER,
#             to='+' + str(user.phone_number)
#         )
#     return sms


def send_sms(distribution_model, user, message):
    api = 'https://probe.fbrq.cloud/v1/send'

    msgid = message.get("id")

    endpoint = os.path.join(api, str(msgid))

    headers = {
        "Authorization": settings.AUTHORIZATION
    }
    data = {"id": distribution_model.get("id"),
            "phone": user.get("phone_number"),
            "text": distribution_model.get("text")}

    response = requests.post(endpoint, json=data, headers=headers)
    return response


def create_message_model(distribution_model, user):
    message = Message(created_datetime=distribution_model.get("sending_datetime"),
                      distribution=distribution_model.get("id"),
                      client=user.id)
    message.save()
    return message
