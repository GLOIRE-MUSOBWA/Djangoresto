from django.shortcuts import redirect,render
from restorantbar.models import table
from restorantbar.forms import Restorantbarform
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
   
