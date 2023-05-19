import os.path

import requests
from twilio.rest import Client
from django.conf import settings

from message.models import Message


def send_sms(distribution_model, user, message):
    api = 'https://probe.fbrq.cloud/v1/send'

    msgid = message.get("id")

    endpoint = os.path.join(api, str(msgid))

    headers = {
        "Authorization": settings.AUTHORIZATION
    }
    data = {"id": distribution_model["id"],
            "phone": user["phone_number"],
            "text": distribution_model["text"]}

    response = requests.post(endpoint, json=data, headers=headers)
    return response


def create_message_model(distribution_model, user):
    message = Message(created_datetime=distribution_model["sending_datetime"],
                      distribution=distribution_model["id"],
                      client=user.id)
    message.save()
    return message
