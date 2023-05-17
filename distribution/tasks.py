import datetime

from celery import shared_task
from client import models

from distribution.utils import send_sms, create_message_model


# Time limit is set to 1 hour
@shared_task(time_limit=3600)
def send_message(distribution_list):
    distribution_model = distribution_list[0]
    user_clients = models.Client.objects.filter(tag=distribution_model["tag_filter"],
                                                code=distribution_model["operator_filter"])

    if not user_clients:
        return None

    for user in user_clients:
        message = create_message_model(distribution_model, user)
        response = send_sms(distribution_model, user, message)

        if response.status_code == 200:
            distribution_model.ending_datetime = datetime.datetime.now()
            distribution_model.save()
            message.status = True
            message.save()
