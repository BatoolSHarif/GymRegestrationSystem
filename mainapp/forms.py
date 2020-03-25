from django import forms
from django.forms.models import ModelForm
from .models import UserInfo,Subscription,TransactionHistory,Vistis


# Create your tests here.
class UserForm(ModelForm):
    class Meta:
        model = UserInfo
        exclude = []
#---------------------------------------------------------------------
class SubscriptionForm(ModelForm):
    class Meta:
        model = Subscription
        exclude = []
#---------------------------------------------------------------------

class SubscriptionForm(ModelForm):
    class Meta:
        model = TransactionHistory
        exclude = []
#---------------------------------------------------------------------

class VistisForm(ModelForm):
    class Meta:
        model = Vistis
        exclude = []