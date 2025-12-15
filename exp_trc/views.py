from django.shortcuts import render,redirect,get_object_or_404
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

def read_specific_expense(request,expense_id):
    """Reads a specific expense properly"""
    exp=Expense.objects.get(id=expense_id)
    context={'expense':exp}
    return render(request,'exp_trc/read_expense.html',context)

def update_specific_expense(request,expense_id):
    """Editing/Updating an specific expense"""
    exp=Expense.objects.get(id=expense_id)
    
    if request.method!='POST':
        #initial request;prefill form with the current datas.
        form=ExpenseForm(instance=exp)
    else:
        #post data submitted; process the data
        form=ExpenseForm(instance=exp,data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('exp_trc:index')
    
    context={'expense':exp,'form':form}
    return render(request,'exp_trc/update_expense.html',context)


def delete_specific_expense(request,expense_id):
    """Deletes a specific expense"""
    exp=get_object_or_404(Expense, id=expense_id)
    exp.delete()
    return redirect('exp_trc:index')