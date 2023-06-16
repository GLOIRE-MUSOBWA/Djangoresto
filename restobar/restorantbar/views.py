from django.shortcuts import redirect,render
from restorantbar.models import table
from restorantbar.models import reservation
from restorantbar.forms import Restorantbarform
from restorantbar.forms import Restorantbarforms
# from restorantbar.models import selectiontab
def tab(request):
    if request.method=='POST':
        form=Restorantbarform(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect("/show")
            except:
                pass
            
    else:
     form=Restorantbarform()
    return render( request,'index.html',{'form':form}) 
def show(request):
    restorant=table.objects.all()
    return render(request,'show.html',{'restorant':restorant})
def edit(request,id):
    restorantbar=table.objects.get(id=id)
    return render(request,'edit.html',{'restorantbar':restorantbar})
def update(request,id):
    restorantbar=table.objects.get(id=id)
    form=Restorantbarform(request.POST,instance=restorantbar)
    if form.is_valid():
        form.save()
        return redirect("/show")
    return render(request,'edit.html',{'restorantbar':restorantbar})
def destroy(request,id):
    restorantbar=table.objects.get(id=id)
    restorantbar.delete()
    return redirect("/show")

# reservatios operations
def reserver(request):
    if request.method=='POST':
        form= Restorantbarforms(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect("/reservation")
            except:
                pass
            
    else:
     form= Restorantbarforms()
    return render( request,'reservation.html',{'form':form}) 

def select(request):
    restaurant=reservation.objects.all()
    return render(request,'reservations.html',{'restaurant':restaurant})

def editreservation(request,id):
    restaurant=reservation.objects.get(id=id)
    return render(request,'editreservation.html',{'restaurant':restaurant})

def updatereservation(request,id):
    restaurant=reservation.objects.get(id=id)
    form= Restorantbarforms(request.POST,instance=restaurant)
    if form.is_valid():
        form.save()
        return redirect("/reservations")
    return render(request,'editreservation.html',{'restaurant':restaurant})

def destroyreservation(request,id):
    restaurantbar=reservation.objects.get(id=id)
    restaurantbar.delete()
    return redirect("/reservations")

def selectionernumtab(request):
    result=table.objects.all()
    return render(request,"reservation.html",{"table":result})  
