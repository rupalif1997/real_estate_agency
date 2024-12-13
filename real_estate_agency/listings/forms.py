
from django.forms import ModelForm
from .models import listings
from django import forms

class ListingForm(ModelForm):
     def __init__(self, *args, **kwargs):
        super(ListingForm, self).__init__(*args, **kwargs)

        for field_name, field in self.fields.items():
            # Add Bootstrap classes to form fields
            field.widget.attrs['class'] = 'form-control'
         
        

     class Meta:
        model = listings
        fields =["contact","title","price","num_bedrooms","num_bathrooms","square_footage","address","image"]
        
         # Customize field names
        labels = {
           'contact':'Contact Number',
            'title': 'Property Type',
            'price': 'Asking Price',
            'num_bedrooms': 'Number of Bedrooms',
            'num_bathrooms': 'Number of Bathrooms',
            'square_footage': 'Built up Area(sq.feet)',
            'address': 'Listing Address',
            'image': 'Listing Image',
        }
        
        # Add placeholders
        widgets = {
           
            'contact': forms.TextInput(attrs={'placeholder': 'Add your contact number to get in touch with you','required': 'required'}),
            'title': forms.TextInput(attrs={'placeholder': 'Apartment, Independant house, Plot,etc.','required': 'required'}),
            'price': forms.TextInput(attrs={'placeholder': 'Enter listing price','required': 'required'}),
            'num_bedrooms': forms.TextInput(attrs={'placeholder': 'Enter number of bedrooms','required': 'required'}),
            'num_bathrooms': forms.TextInput(attrs={'placeholder': 'Enter number of bathrooms','required': 'required'}),
            'square_footage': forms.TextInput(attrs={'placeholder': 'Enter built up area','required': 'required'}),
            'address': forms.TextInput(attrs={'placeholder': 'Enter listing address','required': 'required'}),
            'image': forms.ClearableFileInput(attrs={'placeholder': 'Choose listing image','required': 'required'}),
        }
        
