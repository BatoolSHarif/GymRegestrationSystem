from django.contrib import admin
from .models import models

# Register your models here.
from mainapp.models import UserInfo
admin.site.register(UserInfo)

from mainapp.models import Subscription
admin.site.register(Subscription)

from mainapp.models import TransactionHistory
admin.site.register(TransactionHistory)

from mainapp.models import Vistis
admin.site.register(Vistis)