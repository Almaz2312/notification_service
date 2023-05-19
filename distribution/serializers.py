from django.utils import timezone
from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from distribution.models import Distribute
from client.models import Operator, Tag


class DistributeSerializer(serializers.ModelSerializer):
    operator_filter = serializers.PrimaryKeyRelatedField(queryset=Operator.objects.all(), required=False)
    tag_filter = serializers.PrimaryKeyRelatedField(queryset=Tag.objects.all(), required=False)

    class Meta:
        model = Distribute
        exclude = ('ending_datetime',)

    def validate(self, attrs):
        sending_datetime = attrs.get("sending_datetime")
        if sending_datetime is None:
            sending_datetime = self.instance.sending_datetime

        if timezone.now() > sending_datetime:
            raise ValidationError('Sending time can not be earlier than current time')

        return super().validate(attrs)
