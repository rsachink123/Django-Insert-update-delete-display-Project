from django.shortcuts import render
from .forms import ProductForm,UpdateForm,DeleteForm
from .models import Product
from django.http.response import HttpResponse
from django.shortcuts import get_object_or_404

from django.http.response import HttpResponse
def home(request):
    return render(request, 'product_home.html')

def insert(request):
    if request.method=='POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse('Data Inserted')
        else:
            return HttpResponse('Data is not Inserted')
    else:
        form = ProductForm()
        return render(request, 'product_insert.html',{'form':form})


def display(request):
    data = Product.objects.all()
    return render(request, 'product_display.html', {'data':data})



def update(request):
    if request.method=='POST':
        form = UpdateForm(request.POST)
        if form.is_valid():
            pid = form.cleaned_data['productid']
            id = int(pid)
            #pcost = form.cleaned_data['productcost']
            pcost = request.POST.get('productcost','')
            cost = float(pcost)
            dbuser = Product.objects.filter(productid=id)
            if not dbuser:
                data = "<h1>Invalid Product</h1>"\
                    "<a href='./'>Go to Homepage</a>"
                return HttpResponse(data)
            else:
                dbuser.update(productcost=cost)
                data = "<h1>Product has been updated successfully.</h1>"\
                    "<a href='./'>Go to Homepage</a>"
                return HttpResponse(data)
        else:
            print(form.errors)
    else:
        form = UpdateForm()
        return render(request,'update.html',{'form':form})

def delete(request):
    if request.method=='POST':
        form = DeleteForm(request.POST)
        if form.is_valid():
            pid = int(form.cleaned_data['productid'])
            dbuser  = Product.objects.get(productid=pid)
            if not dbuser:
                data = "<h1>Invalid Product</h1>" \
                       "<a href='./'>Go to Homepage</a>"
                return HttpResponse('data')
            else:
                dbuser.delete()
                data = "<h1>Product was deleted successfully</h1>" \
                    "<a href='./'>Go to homepage</a>"
                return HttpResponse(data)
        else:
            return render(request,'delete1.html')
            #print(form.errors)

    else:
        form = DeleteForm()
        return render(request,'delete.html',{'form':form})

