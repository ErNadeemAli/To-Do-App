from django.shortcuts import render,redirect
from django.contrib import messages

# import todo form and models
from .forms import TodoFrom
from .models import Todo

def home(request):
    item_list = Todo.objects.order_by('-date')
    if request.method=='POST':
        form=TodoFrom(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    form=TodoFrom()

    page={
        'forms':form,
        'list':item_list,
    }
    return render(request, 'home.html', context=page)

def remove(request,id):
    item=Todo.objects.get(id=id)
    item.delete()
    messages.info(request,'item removed !!')
    return redirect('/')