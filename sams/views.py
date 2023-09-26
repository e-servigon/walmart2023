from django.shortcuts import render,redirect
from .models import Vendor,Product,ExtendedData
from .forms import CreateVendorForm , CreateProductsForm, CreateUserForm,UserProfileForm
from django.utils import timezone
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
 
# Create your views here.
@login_required
def home (request):
    #Hola
    return render(request,'home.html',{})

@login_required
def vendor (request):
    vendor_list=Vendor.objects.all()
    data_context={'vendor_list':vendor_list} #todo lo que quieres que te pinte el html
    vendor_form = CreateVendorForm ()
    data_context['vendor_form']=vendor_form
    if request.method == 'POST':
        vendor_form = CreateVendorForm (request.POST)
        print(vendor_form.errors)#para ver en consola que errores puede haber 
        print(request.POST)
        if vendor_form.is_valid():
            try: 
                vendor_validate=Vendor.objects.get(vendor_name = request.POST.get('vendor_name'))
                if vendor_validate is not None:
                    data_context['vendor_exist']=True
            except:
                vendor_form.save()
    return render (request,'vendor.html',data_context)

@login_required
def product (request):
    product_list= Product.objects.filter(deleted_date__isnull = True) #  te trae una lista de objetos que cumplan con esa condicion
    data_context={'product_list':product_list} #todo lo que quieres que te pinte el html
    product_form = CreateProductsForm ()
    data_context['product_form']=product_form
    if request.method == 'POST':
        product_form = CreateProductsForm (request.POST,request.FILES)
        print(product_form.errors)#para ver en consola que errores puede haber 
        print(request.POST)
        if product_form.is_valid():
            try: 
                product_validate=Product.objects.get(product_sku = request.POST.get('product_sku'))
                if product_validate is not None:
                    data_context['product_exist']=True
            except:
                product_form.save()
    return render (request,'product.html',data_context)

@login_required
def deleteproduct(request,product_id):
    product = Product.objects.get(pk=product_id)
    data_context ={'product':product}
    if request.method =='POST':
        print(request.POST)
        if 'yes' in request.POST:
            product.deleted_date = timezone.now ()
            product.save()
            return redirect('home') #redirect te relinkea apartir de ese alias. al darle guardar te regrese al home 
    return render(request,'delete_product.html',data_context)

def createuser(request):
    user_form = CreateUserForm()
    user_profile=UserProfileForm()
    data_context = {'user_form':user_form,'user_profile_form':user_profile}
    if request.method=='POST':
        print(request.POST)
        user_form=CreateUserForm(request.POST)
        user_profile=UserProfileForm(request.POST)
        if user_form.is_valid():
            user_form.save()
            user_to_profile = User.objects.get(username=request.POST.get('username'))
            user_extended_data = ExtendedData.objects.create(user=user_to_profile,user_type=request.POST.get('user_type'))
            user_extended_data.save()
            return redirect('login')
    return render(request,'create_user.html',data_context)
        
       

        



