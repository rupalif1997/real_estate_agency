from django.shortcuts import redirect, render
from django.urls import reverse
from .models import listings,Payment_tb
from .forms import ListingForm
from django.contrib.auth.decorators import login_required
import razorpay
from django.utils import timezone

# Create your views here.

def listing_list(request):
    listing=listings.objects.all()
    context={ "listing": listing}
    return render(request,"listings.html", context) 

def listing_retrieve(request,id):
    listing= listings.objects.get(id=id)
    context={ "listing": listing,
             'isUserLoggedIn':  request.user.is_authenticated}
    return render(request,"listing.html", context)

@login_required
def listing_create(request):
    form= ListingForm()
    if request.method == "POST":
        form =ListingForm(request.POST, request.FILES)
        if form.is_valid():
            new_listing=form.save()
            
            return redirect("makepayment", listing_id=new_listing.id)
        
    context={"form":form}
    return render(request,"listing_create.html",context)
    
@login_required    
def listing_update(request,id):
    listing= listings.objects.get(id=id)
    form= ListingForm(instance=listing)
    
    if request.method == "POST":
        form =ListingForm(request.POST, instance=listing, files=request.FILES)
        if form.is_valid():
            form.save()
            
            return redirect("list/")
        
    context={"form":form}
    return render(request,"listing_update.html",context)


    
@login_required   
def listing_delete(request,id):
    listing= listings.objects.get(id=id)
    listing.delete()
    return redirect("/list/")






def makepayment(request, listing_id):
    # Fixed amount of 1000 INR
    fixed_amount = 1000

    # Get the current timestamp
    # current_time = timezone.now()

    # Create a Razorpay order
    client = razorpay.Client(auth=("rzp_test_a4ZXWOWwnsyyaF", "oKBc64i89fKN0JvESmUbR1qN"))
    receipt_id = f"listing_{listing_id}_{int(timezone.now().timestamp())}"
    data = {
        "amount": fixed_amount * 100,  # Amount is in paise
        "currency": "INR",
        "receipt": receipt_id,  
        "payment_capture": 1,  # Automatically capture payment after creation
    }

    payment = client.order.create(data=data)

    context = {
        'data': payment,
     
        'listing_id': listing_id,
    }

    if payment.get('status') == 'captured':
         
         return redirect('list')

    return render(request, 'pay.html', context)



def filter_listings(request):
    # Get filter parameters from the request.GET dictionary
    min_bedrooms = request.GET.get('min_bedrooms')
    max_price = request.GET.get('max_price')
    address = request.GET.get('address')
    
    # print(f"min_bedrooms: {min_bedrooms}, max_price: {max_price}, address: {address}")
    # Start with all listings
    filtered_listings = listings.objects.all()

    # Apply filters if they exist
    
    if address:
        filtered_listings = filtered_listings.filter(address__icontains=address)
    
    if min_bedrooms:
        filtered_listings = filtered_listings.filter(num_bedrooms=min_bedrooms)

    if max_price:
        filtered_listings = filtered_listings.filter(price__lte=max_price)

    

    return render(request, 'filtered_listing.html', {'listings': filtered_listings})

