import pytz
from django.db import models
from django.core.validators import RegexValidator


class Operator(models.Model):
    code = models.IntegerField()


class Tag(models.Model):
    tag = models.CharField(max_length=64)


class Client(models.Model):
    TIMEZONES = tuple(zip(pytz.all_timezones, pytz.all_timezones))
    PHONE_VALIDATOR = RegexValidator(regex=r'^7[0-9]{10}$',
                                     message="Phone number must start with 7 and be 11 digits long.")

    phone_number = models.CharField(max_length=11, validators=[PHONE_VALIDATOR])
    code = models.ForeignKey(Operator, on_delete=models.DO_NOTHING,
                             null=True, blank=True)
    tag = models.ForeignKey(Tag, on_delete=models.DO_NOTHING,
                            null=True, blank=True)
    timezone = models.CharField(max_length=100, choices=TIMEZONES,
                                default='UTC')
