from django.shortcuts import render,redirect
from . models import Expense
from .forms import ExpenseForm
 
# Create your views here.
def index(request):
    """Main page for expense tracker"""
    exp=Expense.objects.order_by('date_added')
    context={'expenses':exp}
    return render(request,'exp_trc/index.html',context)

def create_expense(request):
    """Lets user create their own  expenses"""
    if request.method!='POST':
        form=ExpenseForm()
    else:
        form=ExpenseForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('exp_trc:index')
    context={'form':form}
    return render(request, 'exp_trc/new_expense.html', context)