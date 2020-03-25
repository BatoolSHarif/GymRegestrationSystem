from django.shortcuts import render,HttpResponse
from .forms import UserForm,SubscriptionForm,SubscriptionForm,VistisForm
from django.urls import reverse_lazy,reverse
from .models import UserInfo,Subscription,TransactionHistory,Vistis
from django.views.generic import CreateView,ListView,DeleteView
from datetime import date,datetime
from django.contrib import messages
from django.http import JsonResponse

# Create your views here.
class UserCreatView(CreateView):
    model = UserInfo
    template_name = "userhtml.html"
    success_url = reverse_lazy('user_url')
    fields = '__all__'
    def get_context_data(self,**kwargs):
        context = super(UserCreatView,self).get_context_data(**kwargs)
        context ['list_stu'] = UserInfo.objects.all()
        return context

def jsonview (request):
    x = UserInfo.objects.all().values()
    res_list = [dict(i) for i in x]
    res_list = []
    for i in x:
        res_list.append(dict(i))
    res_list
    return JsonResponse(list(x), safe=False)


class SubscriptionCreatView(CreateView):
    model = Subscription
    template_name = "subhtml.html"
    success_url = reverse_lazy('sub_url')
    fields = '__all__'
    def get_context_data(self,**kwargs):
        context = super(SubscriptionCreatView,self).get_context_data(**kwargs)
        context ['list_stu1'] = Subscription.objects.all()
        return context


class TransactionHistoryCreatView(CreateView):
    model = TransactionHistory
    template_name = "transaction.html"
    success_url = reverse_lazy('transaction_url')
    fields = '__all__'
    def get_context_data(self,**kwargs):
        context = super(TransactionHistoryCreatView,self).get_context_data(**kwargs)
        context ['list_stu'] = TransactionHistory.objects.all()
        return context
   

class VistisCreatView(CreateView):
    model = Vistis
    template_name = "visishtml.html"
    success_url = reverse_lazy('visit_url')
    fields = '__all__' 
    # form = VistisForm()
        # date = self.request.GET.get('date_time')
    # if Vistis.objects.filter(first_name=form.cleaned_data['first_name']).exists():
    #         print( 'The user Exisit')
    def get_context_data(self,**kwargs):
        context = super(VistisCreatView,self).get_context_data(**kwargs)
        context ['list_stu1'] = Vistis.objects.all()
        return context

def index(request):
    return render(request,'base.html')

