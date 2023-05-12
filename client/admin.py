from django.contrib import admin

from client.models import Tag, Operator, Client

admin.site.register(Tag)
admin.site.register(Operator)
admin.site.register(Client)