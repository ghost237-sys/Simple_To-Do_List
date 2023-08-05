from django.shortcuts import render,redirect
from .models import ToDoList,Item
from .forms import CreateNew
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def index(request,id):
    ls = ToDoList.objects.get(id=id)
    if ls in request.user.todolist.all():
        if request.method == "POST":
            if request.POST.get("save"):
                for item in ls.item_set.all():
                    if request.POST.get("c" + str(item.id)) == "clicked": 
                        item.Complete = True
                    else:
                        item.Complete = False

                    item.save()
            if request.POST.get("Clear"):
                ls.item_set.all().delete()
            if request.POST.get("Delete"):
                ls.delete()
                return HttpResponseRedirect('/view')

            elif request.POST.get("newItem"):
                txt = request.POST.get("new")
                if len(txt) > 2:
                    ls.item_set.create(Text=txt,Complete=False) 
                else:
                    messages.error(request,"Invalid item! Please enter a text with atleast 3 characters")
    
        return render(request,"list.html",{"ls":ls})
    return render(request,'home.html',{})




def view(request):
    return render(request,"view.html",{})    


def home(request):
    return render(request,"home.html",{})
    
@login_required
def create(request):
    if request.method == "POST":
        print(request.POST)
        form = CreateNew(request.POST)
        if form.is_valid():
            n = form.cleaned_data["name"]
            t = ToDoList(name=n)
            t.save()
            request.user.todolist.add(t)
            messages.success(request,f"ToDoList '{n}' has been created successfully")
            return HttpResponseRedirect('/%i' %t.id)
        else:
            messages.error(request,"Form is not valid. Please correct any errors.")
    else:
        print("hey")
        form = CreateNew()
    
    return render(request,'create.html',{"form":form} )