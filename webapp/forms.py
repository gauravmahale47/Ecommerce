from django import forms
from .models import *

class ProductForm(forms.ModelForm):
    Product_Name = forms.CharField(label="Product Name", widget=forms.TextInput(attrs={'placeholder':'Enter Product Name', 'class':'border border-dark text-dark form-control mb-2'}))
    Color = forms.CharField(label = 'Color', widget=forms.TextInput(attrs={'placeholder':'Color', 'class':'border border-dark text-dark form-control mb-2'}))
    Full_Description = forms.CharField(label='Description', widget=forms.Textarea(attrs={'rows':5,'placeholder':'Product Description', 'class':'border border-dark text-dark form-control mb-2'}))
    Price = forms.FloatField(widget=forms.NumberInput(attrs={'placeholder':'Product Price', 'class':'border border-dark text-dark form-control mb-2'}))
    Product_Image = forms.ImageField(label='Product Image', widget=forms.ClearableFileInput(attrs={'class':'border border-dark text-dark form-control mb-2'}))
    Categories = (('Select','Select'),('Clothing','Clothing'),('Electronics','Electronics'),('Shoes','Shoes'),('Watches','Watches'),('Jewellery','Jewellery'),('Health and Beauty','Health and Beauty'),('Kid"s and Babies','Kid"s and Babies'),('Sports','Sports'),('Home and Garden','Home and Garden'))

    Category = forms.ChoiceField(label='Category', widget = forms.Select(attrs={'class':'border border-dark text-dark form-control mb-2'}),choices=Categories)
    class Meta:
        model = Product
        fields = "__all__"

