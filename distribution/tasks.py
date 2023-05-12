import datetime

from celery import shared_task
from client import models

from distribution.utils import send_sms, create_message_model


# Time limit is set to 1 hour
@shared_task(time_limit=3600)
def send_message(distribution_model):
    user_clients = models.Client.objects.filter(tag=distribution_model.get("tag_filter"),
                                                code=distribution_model.get("operator_filter"))

    for user in user_clients:
        send_sms(distribution_model, user)
        create_message_model(distribution_model, user)
        distribution_model.ending_datetime = datetime.datetime.now()
        distribution_model.save()
