from django.shortcuts import render,redirect,get_object_or_404
from .forms import addressform
from .models import address

# Create your views here.
def add_address(request):
    form = addressform()
    if request.method == "POST":
        form_data =  addressform(request.POST)
        if form_data.is_valid():
            v = form_data.save(commit=False)
            v.user = request.user
            v.save()
            return redirect('address_list')
    return render(request,'add_address.html',{'form':form})

def address_list(request):
    Address = address.objects.all()
    return render(request,'address_list.html',{'address':Address})

# def update_address(request,pk):
#     Address = address.objects.get(id = pk)
#     if request.method == "POST":
#             Address.name = request.POST['fullname']
#             Address.mobile = request.POST['mobile']
#             Address.address_line = request.POST['address_line']
#             Address.city = request.POST['city']
#             Address.state = request.POST['state']
#             Address.pincode = request.POST['pincode']
#             Address.save()
#             return redirect('address_list')
#     return render(request,'update_address.html',{'address':Address})

def update_address(request,pk):
        data = address.objects.get(id = pk)
        if request.method == "POST":
           form_data =  addressform(request.POST,instance=data)
           if form_data.is_valid():
               v = form_data.save(commit=False)
               v.user = request.user
               v.save()
               return redirect('address_list')
        else:
            form = addressform(instance= data)

        return render(request,'update_address.html',{'form':form})

def delete_address(request,pk):
    data = address.objects.get(id = pk).delete()
    return redirect('address_list')