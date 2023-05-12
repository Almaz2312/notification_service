from django.db import models

from distribution.models import Distribute
from client.models import Client


class Message(models.Model):
    created_datetime = models.DateTimeField(db_comment='distribution_time')
    status = models.BooleanField(default=False)
    distribution = models.ForeignKey(Distribute, on_delete=models.CASCADE,
                                     related_name='message_distribution')
    client = models.ForeignKey(Client, on_delete=models.DO_NOTHING,
                               related_name='message_client',
                               null=True, blank=True)
