from django.db import models
from client.models import Operator, Tag


class Distribute(models.Model):
    sending_datetime = models.DateTimeField()
    text = models.TextField()
    operator_filter = models.ForeignKey(Operator, on_delete=models.DO_NOTHING,
                                        null=True, blank=True)
    tag_filter = models.ForeignKey(Tag, on_delete=models.DO_NOTHING,
                                   null=True, blank=True)
    ending_datetime = models.DateTimeField(null=True, blank=True)
