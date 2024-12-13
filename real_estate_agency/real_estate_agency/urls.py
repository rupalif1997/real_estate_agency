"""
URL configuration for real_estate_agency project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from listings.views import filter_listings, listing_list,listing_retrieve,listing_create,listing_update,listing_delete,makepayment
from properties import views




urlpatterns = [
    path('admin/', admin.site.urls),
    # path('', include('properties.urls')),
    path('list/', listing_list),
    path('listings/<id>', listing_retrieve),
    path('listings/<id>/update', listing_update,name='listing_update'),
    path('add_listing/', listing_create),
    path('listings/<id>/delete_2', listing_delete,name='listing_delete'),
    path('customer', views.create),
   
    path('dashboard', views.dashboard),
    path('delete/<rid>',views.delete),
    path('edit/<rid>',views.edit),
    
    path('home', views.home, name='home'),
    path('about', views.about, name='about'),
    path('filter/', filter_listings, name='filter_listings'),
    path('register',views.user_register,name='register'),
    path('login',views.user_login, name='login'),
    path('logout',views.user_logout),
    # path('agents/', views.agents_list, name='agents_list'),
    path('makepayment/<int:listing_id>', makepayment, name='makepayment'),
    path('send_email/<pid>/', views.send_email),

    # path('initiate_payment/<int:listing_id>/<int:customer_id>/', views.initiate_payment, name='initiate_payment'),
]
    




if settings.DEBUG:
   urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
