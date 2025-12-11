from django.shortcuts import render
from . models import Expense
# Create your views here.
def index(request):
    """Main page for expense tracker"""
    exp=Expense.objects.order_by('date_added')
    context={'expenses':exp}
    return render(request,'exp_trc/index.html',context)

