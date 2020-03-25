from django.db import models
from datetime import date,datetime
# from .forms import VistisForm 
# Create your models here.

class UserInfo(models.Model):
    first_name = models.CharField(max_length=25)
    last_name =  models.CharField(max_length=25)
    phone_num =  models.IntegerField (default = '079 xxxx xx')
    health_prob = models.BooleanField(null=True)
    def __str__(self):
        return self.first_name
#---------------------------------------------------------------------

class Subscription(models.Model):
    from_date = models.DateField(default=datetime.now())
    to_date =  models.DateField(default=datetime.now()) 
    customer = models.ForeignKey(to='UserInfo',on_delete=models.PROTECT)
    def __str__(self):
        return self.customer.first_name
#---------------------------------------------------------------------

class TransactionHistory(models.Model):
    payment = models.IntegerField(null=True,blank=True)
    first_name = models.ForeignKey(to='UserInfo',on_delete=models.PROTECT)
    def __str__(self):
        return self.first_name.first_name
#---------------------------------------------------------------------

class Vistis(models.Model):
    date_time =  models.DateTimeField(default=datetime.now())
    first_name = models.ForeignKey(to='UserInfo',on_delete=models.PROTECT)
    to_date = models.ForeignKey(to='Subscription',on_delete=models.PROTECT)
    # def end_subscription (self):
    #     today = date.today()
    #     end = today - self.to_date.to_date
    #     if end == 0 :
    #         return end
    #     else:
    #         self.save()
    def __str__(self):
        return self.first_name.first_name
