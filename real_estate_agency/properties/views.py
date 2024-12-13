from datetime import timezone
from django.http import HttpResponse,JsonResponse
from django.shortcuts import render, redirect
from django.urls import reverse
# import razorpay
from django.core.mail import send_mail
from .models import Msg,Payment
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
# from listings.models import listings
from django.contrib import messages





@login_required
def create(request):
    
    if request.method == 'POST':
        # listing_id = request.POST.get('listing_id')
        # customer_id = request.POST.get('customer_id')
        # Assuming the form has the same field names as in the Customer model
        first_name = request.POST['first_name']
        last_name =request.POST['last_name'] 
        contact=request.POST['contact']
        email = request.POST['email']
        address = request.POST['address']
        city = request.POST['city']
        apartment_size = request.POST['apartment_size']
        
        # Create a new Customer instance and save it to the database
        m = Msg.objects.create(
            
            first_name=first_name,
            last_name=last_name,
            contact=contact,
            email=email,
            address=address,
            city=city,
            apartment_size=apartment_size,
            user=request.user,
            # listing_id=listing_id ,
            # customer_id=customer_id
            
        )
        
        m.save()
        

        return redirect('/dashboard') 
        # return redirect('dashboard',{'lising_id':listing_id})

    else:
        # print("request is: ",request.method)
        return render(request,'customer_detail.html')
    

##### Dashboard 

def dashboard(request):
    # listing_id = request.GET.get('listing_id')
    m=Msg.objects.all()
    print(m)
       
    context = {
        'data': m,
        # 'listing_id':listing_id
        }
    # return HttpResponse("Data fetch successfully....")
    return render(request,'dashboard.html',context)
   

def delete(request,rid) :
    print("Id of record to be deleted: "+rid)
    m=Msg.objects.filter(id=rid)
    m.delete()
    
    return redirect('/dashboard')

def edit(request,rid):
    
    if request.method=="POST":
        first_name = request.POST['first_name']
        last_name =request.POST['last_name'] 
        contact=request.POST['contact']
        email = request.POST['email']
        address = request.POST['address']
        city = request.POST['city']
        apartment_size = request.POST['apartment_size']

        m=Msg.objects.filter(id=rid)
        m.update(first_name=first_name,
            last_name=last_name,
            contact=contact,
            email=email,
            address=address,
            city=city,
            apartment_size=apartment_size
        )
        
       
        
        return redirect("/dashboard")
    else:
         message = Msg.objects.get(id=rid)
         context = {'data': message}
         return render(request, 'edit.html', context)


 
 
def user_register(request):
    if request.method == 'POST':
        uname = request.POST['uname']
        upass = request.POST['upass']
        ucpass = request.POST['ucpass']
        context={}
        if uname=="" or upass=="" or ucpass=="":
            context['errmsg']="Feilds cannot be empty.."
            return render(request,'register.html',context)
        elif upass != ucpass:
            context['errmsg']="Password and confirm password didn't match.."
            return render(request,'register.html',context)
        else:  
            try:  
                u = User.objects.create(username=uname, password=upass,email=uname)
                u.set_password(upass)       #encrypt format
                u.save()
                context['success']="User created successfully"
                return render(request, 'register.html',context)
            except Exception:
                context['errmsg']="User with same username already present.."
                return render(request,'register.html',context)
    else:
        return render(request,'register.html')
    
    
def user_login(request):
    if request.method == 'POST':
        uname = request.POST['uname']
        upass = request.POST['upass']
        context={}
        if uname=="" or upass=="":
            context['errmsg']="Fields cannot be empty.."
            return render(request,'login.html',context)
        else:
            u=authenticate(username=uname,password=upass)
            #print(u)
            if u is not None:
                login(request,u)    # start the session
                return redirect('/list/')
            else:
                context['errmsg']="Invalid username and password.."
                return render(request,'login.html',context)            
    else:
     return render(request,'login.html')
       
def user_logout(request):
    logout(request)
    return redirect('/home')

def home(request):
    return render(request, 'base.html')

def about(request):
    return render(request, 'aboutus.html')


def send_email(request,pid):
    # Assuming you have a Customer model, replace it with your actual model
    customer = Msg.objects.get(id=pid)

    if request.user == customer.user:
        # Prepare the email content with customer information
        email_content = f"Customer Information who are interested in buying property:\n\n" \
                        f"First Name: {customer.first_name}\n" \
                        f"Last Name: {customer.last_name}\n" \
                        f"Contact: {customer.contact}\n" \
                        f"Email: {customer.email}\n" \
                        f"Address: {customer.address}\n" \
                        f"City preffered: {customer.city}\n" \
                        f"Apartment Size: {customer.apartment_size}\n"

        # Send email to admin
        if request.user.is_authenticated and request.user == customer.user:
         send_mail(
            'Customer Information who are interested in buying property',
            email_content,
            'rupalif1997@gmail.com',  # your email address
            ['rupalif1997@gmail.com'],  # admin's email address
            fail_silently=False,
        )
        messages.success(request, 'Email sent successfully!')
        # context={}
        # context['success']="Email sent successfully!!"
        return redirect('/dashboard')  
    else:
        messages.success(request, 'Email not sent')
        return redirect('/dashboard')  